class TextAdventureState:
    def __init__(self):
        self.__old_selections = []
        self.__current_selection = TextAdventureSelection(
                "You entered this area.",
                "leave",
                "keep going",
                "run away"
        )

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


class TextAdventureSelection:
    def __init__(self, text, *options):
        """
        :type text: str
        :type options: bytearray of str
        """
        self.text = text
        self.options = options
