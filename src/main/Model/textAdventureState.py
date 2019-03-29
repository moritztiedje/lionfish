class TextAdventureState:
    def __init__(self):
        self.__old_selections = []
        self.__initial_selection = TextAdventureSelection(
                "You entered this area.",
                "finish it",
                "look for stuff",
                "run like a rabbit"
        )
        self.__current_selection = self.__initial_selection

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

    def adventure_completed(self):
        self.__current_selection = self.__initial_selection
        self.__old_selections = []


class TextAdventureSelection:
    def __init__(self, text, *options):
        """
        :type text: str
        :type options: bytearray of str
        """
        self.text = text
        self.options = options
