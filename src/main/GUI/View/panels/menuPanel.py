from src.main.GUI.View.imageVaults.menuImageVault import MenuImageVault
from src.main.GUI.View.panels.panel import Panel


class MenuPanel(Panel):
    def __init__(self, game_window):
        """
        :type game_window: src.main.GUI.View.gameWindow.GameWindow
        """
        super().__init__(game_window, 1)

    def _handle_mouse_event(self, mouse_event):
        pass

    def _load_image_vault(self):
        return MenuImageVault()
