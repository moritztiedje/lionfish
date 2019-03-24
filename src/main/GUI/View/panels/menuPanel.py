from src.main.GUI.View.imageVault import MenuImageVault
from src.main.GUI.View.panels.panel import Panel


class MenuPanel(Panel):
    def _load_image_vault(self):
        return MenuImageVault()
