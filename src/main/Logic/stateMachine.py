from enum import Enum


class StateTypes(Enum):
    FINAL_STATE = 0
    CHOICE_STATE = 1


class ResultTypes(Enum):
    SUCCESS = 0
    FAIL = 1


class State:
    def __init__(self, state_type, text):
        self.type = state_type
        self.text = text


class ProceedState(State):
    def __init__(self, text):
        super().__init__(StateTypes.FINAL_STATE, text)
        self.result = ResultTypes.SUCCESS


class FailState(State):
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


class StateMachineResult:
    def __init__(self, text, selection, result):
        self.text = text
        self.selection = selection
        self.result = result


class StateMachine:
    def __init__(self, initial_state):
        self.__current_state = initial_state

    def advance(self, selection):
        """
        :type selection: int
        :rtype: StateMachineResult
        """
        text = ""

        next_state = self.__current_state.get_next_state(selection)
        text += next_state.text
        if next_state.type == StateTypes.FINAL_STATE:
            return StateMachineResult(text, None, next_state.result)
        elif next_state.type == StateTypes.CHOICE_STATE:
            return StateMachineResult(text, next_state.get_selections(), None)
