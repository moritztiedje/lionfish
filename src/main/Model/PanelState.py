class PanelState:
    def __init__(self, visible, active):
        self.__visible = visible
        self.__active = active

    def is_visible(self):
        return self.__visible

    def is_active(self):
        return self.__active

    def activate(self):
        self.__active = True

    def deactivate(self):
        self.__active = False

    def show(self):
        self.__active = True
        self.__visible = True

    def hide(self):
        self.__active = False
        self.__visible = False
