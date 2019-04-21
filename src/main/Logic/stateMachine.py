from enum import Enum
from random import random


class StateTypes(Enum):
    FINAL_STATE = 0
    CHOICE_STATE = 1
    AUTO_PROCEED_STATE = 2


class ResultTypes(Enum):
    SUCCESS = 0
    FAIL = 1


class State:
    def __init__(self, state_type, text):
        self.type = state_type
        self.text = text


class AdvanceState(State):
    def __init__(self, text):
        super().__init__(StateTypes.FINAL_STATE, text)
        self.result = ResultTypes.SUCCESS


class GoBackState(State):
    def __init__(self, text):
        super().__init__(StateTypes.FINAL_STATE, text)
        self.result = ResultTypes.FAIL


class ChoiceState(State):
    def __init__(self, text):
        super().__init__(StateTypes.CHOICE_STATE, text)
        self.__next_states = []
        self.__selections = []

    def add_next_state(self, selection_text, state):
        """
        :type state: State
        :type selection_text: str
        """
        self.__selections.append(selection_text)
        self.__next_states.append(state)

    def get_next_state(self, selection):
        """
        :type selection: int
        :rtype: State
        """
        return self.__next_states[selection]

    def get_selections(self):
        return self.__selections


class AttemptState(State):
    def __init__(self, text, success_chance):
        """
        :type text: str
        :type success_chance: float
        """
        super().__init__(StateTypes.AUTO_PROCEED_STATE, text)
        self.__success_chance = success_chance
        self.__success_state = None
        self.__fail_state = None

    def set_success_state(self, state):
        """
        :type state: State
        """
        self.__success_state = state

    def set_fail_state(self, state):
        """
        :type state: State
        """
        self.__fail_state = state

    def get_next_state(self):
        """
        :rtype: State
        """
        random_number = random()
        if random_number <= self.__success_chance:
            return self.__success_state
        else:
            return self.__fail_state


class ForwardingState(State):
    def __init__(self, text):
        super().__init__(StateTypes.AUTO_PROCEED_STATE, text)
        self.__next_state = None

    def set_next_state(self, state):
        """
        :type state: State
        """
        self.__next_state = state

    def get_next_state(self):
        return self.__next_state


class StateMachineResult:
    def __init__(self, text, selection, result):
        self.text = text
        self.selection = selection
        self.result = result


class StateMachine:
    def __init__(self, initial_state):
        self.__current_state = initial_state
        self.__text = ""

    def pick(self, selection):
        """
        :type selection: int
        :rtype: StateMachineResult
        """
        self.__current_state = self.__current_state.get_next_state(selection)
        self.__text = ""
        return self.run_until_next_result()

    def run_until_next_result(self):
        """
        :rtype: src.main.Logic.stateMachine.StateMachineResult
        """
        self.__text += self.__current_state.text
        if self.__current_state.type == StateTypes.FINAL_STATE:
            return StateMachineResult(self.__text, [], self.__current_state.result)
        elif self.__current_state.type == StateTypes.CHOICE_STATE:
            return StateMachineResult(self.__text, self.__current_state.get_selections(), None)
        elif self.__current_state.type == StateTypes.AUTO_PROCEED_STATE:
            self.__current_state = self.__current_state.get_next_state()
            return self.run_until_next_result()
