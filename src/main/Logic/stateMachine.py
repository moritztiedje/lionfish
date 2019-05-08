from enum import Enum
from random import random


class StateTypes(Enum):
    FINAL_STATE = 0
    CHOICE_STATE = 1
    AUTO_PROCEED_STATE = 2


class ResultTypes(Enum):
    SUCCESS = 0
    FAIL = 1
    GAME_OVER = 2


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


class GameOverState(State):
    def __init__(self, text):
        super().__init__(StateTypes.FINAL_STATE, text)
        self.result = ResultTypes.GAME_OVER


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

    def get_success_chance(self):
        return self.__success_chance


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


class SkillCheckState(State):
    def __init__(self, text, skill, difficulty):
        super().__init__(StateTypes.AUTO_PROCEED_STATE, text)
        self.__skill = skill
        self.__difficulty = difficulty
        self.__success_chance = None
        self.__success_state = None
        self.__fail_state = None

    def get_skill(self):
        return self.__skill

    def get_difficulty(self):
        return self.__difficulty

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

    def set_success_chance(self, chance):
        """
        :type chance: float
        """
        self.__success_chance = chance

    def get_next_state(self):
        """
        :rtype: State
        """
        random_number = random()
        if random_number <= self.__success_chance:
            return self.__success_state
        else:
            return self.__fail_state


class StateMachineResult:
    def __init__(self, text, selection, result):
        self.text = text
        self.selection = selection
        self.result_type = result


class StateMachine:
    def __init__(self, initial_state, game_state):
        """
        :type initial_state: State
        :type game_state: src.main.Model.gameState.GameState
        """
        self.__current_state = initial_state
        self.__text = ""
        self.__game_state = game_state

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
            choices = []
            selection_texts = self.__current_state.get_selections()
            for selection_index in range(len(selection_texts)):
                selectable_state = self.__current_state.get_next_state(selection_index)
                text = selection_texts[selection_index]
                if isinstance(selectable_state, AttemptState):
                    success_chance = selectable_state.get_success_chance()
                    choices.append(Choice(text, success_chance))
                elif isinstance(selectable_state, SkillCheckState):
                    skill = selectable_state.get_skill()
                    difficulty = selectable_state.get_difficulty()
                    success_chance = self.__calculate_success_chance(skill, difficulty)
                    selectable_state.set_success_chance(success_chance)
                    choices.append(Choice(text + ' (' + str(skill) + ' check: ' + str(difficulty) + ')', success_chance))
                else:
                    choices.append(Choice(text, None))
            return StateMachineResult(self.__text, choices, None)
        elif self.__current_state.type == StateTypes.AUTO_PROCEED_STATE:
            self.__current_state = self.__current_state.get_next_state()
            return self.run_until_next_result()

    def __calculate_success_chance(self, skill, difficulty):
        """
        :type skill: src.main.constants.PlayerSkills
        :type difficulty: int
        :rtype: float
        """
        skill_level = self.__game_state.get_player().get_absolute_skill_level(skill)
        difference = skill_level - difficulty
        if difference > 2:
            return 1.0
        if difference is 2:
            return 0.95
        elif difference is 1:
            return 0.85
        elif difference is 0:
            return 0.7
        elif difference is -1:
            return 0.5
        elif difference is -2:
            return 0.25
        elif difference is -3:
            return 0.1
        elif difference < -3:
            return 0.0


class Choice:
    def __init__(self, text, success_chance):
        self.text = text
        self.success_chance = success_chance
