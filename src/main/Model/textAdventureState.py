class TextAdventureState:
    def __init__(self, first_result):
        """
        :type first_result: src.main.Logic.stateMachine.StateMachineResult
        """
        self.__old_selections = []
        self.__current_selection = TextAdventureSelection(first_result.text, first_result.selection)
        self.__completed = False

    def get_current_selection(self):
        """
        :rtype: TextAdventureSelection
        """
        return self.__current_selection

    def get_old_selections(self):
        """
        :rtype: bytearray of TextAdventureSelection
        """
        return self.__old_selections

    def define_next_selection(self, selection):
        """
        :type selection: TextAdventureSelection
        """
        self.__old_selections.append(self.__current_selection)
        self.__current_selection = selection

    def is_completed(self):
        """
        :rtype: bool
        """
        return self.__completed

    def complete(self):
        self.__completed = True


class TextAdventureSelection:
    def __init__(self, text, options):
        """
        :type text: str
        :type options: list of TextAdventureOption
        """
        self.text = text
        self.options = options
