class TextAdventureState:
    def __init__(self):
        self.__text = "You entered this area. It is a nice area. There is a comfy chair. You entered this area. It is a nice area. There is a comfy chair. You entered this area. It is a nice area. There is a comfy chair. You entered this area. It is a nice area. There is a comfy chair. You entered this area. It is a nice area. There is a comfy chair. You entered this area. It is a nice area. There is a comfy chair. You entered this area. It is a nice area. There is a comfy chair. You entered this area. It is a nice area. There is a comfy chair"
        self.__options = [
            "leave",
            "keep going",
        ]

    def get_text(self):
        """
        :rtype: str
        """
        return self.__text

    def get_options(self):
        """
        :rtype: bytearray of str
        """
        return self.__options
