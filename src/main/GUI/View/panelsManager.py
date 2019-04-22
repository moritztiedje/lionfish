from src.main.GUI.View.panels.areaMapPanel import AreaMapPanel
from src.main.GUI.View.panels.gameOverPanel import GameOverPanel
from src.main.GUI.View.panels.menuPanel import MenuPanel
from src.main.GUI.View.panels.textAdventurePanel import TextAdventurePanel
from src.main.GUI.View.panels.worldMapPanel import WorldMapPanel
from src.main.constants import Panels


class PanelsManager:
    def __init__(self, game_window):
        """
        :type game_window: main.gameWindow.GameWindow
        """
        self.__panels = {
            Panels.AreaMap: AreaMapPanel(game_window),
            Panels.WorldMap: WorldMapPanel(game_window),
            Panels.MainMenuBar: MenuPanel(game_window, self.__camera_zoom_in, self.__camera_zoom_out),
            Panels.TextAdventureBox: TextAdventurePanel(game_window),
            Panels.GameOverPanel: GameOverPanel(game_window)
        }

    def __camera_zoom_in(self):
        if self.__panels[Panels.AreaMap].is_active():
            self.__panels[Panels.AreaMap].zoom_in()
        if self.__panels[Panels.WorldMap].is_active():
            self.__panels[Panels.WorldMap].zoom_in()

    def __camera_zoom_out(self):
        if self.__panels[Panels.AreaMap].is_active():
            self.__panels[Panels.AreaMap].zoom_out()
        if self.__panels[Panels.WorldMap].is_active():
            self.__panels[Panels.WorldMap].zoom_out()

    def draw(self, game_state):
        """
        :type game_state: src.main.Model.gameState.GameState
        """
        for z_index in range(3):
            for panel_key in self.__panels:
                panel = self.__panels[panel_key]
                if panel.has_z_index(z_index):
                    if game_state.get_panel_state(panel_key).is_visible():
                        panel.load_images()
                        panel.draw(game_state)
                    else:
                        panel.discard_images()

        for panel_key in self.__panels:
            panel = self.__panels[panel_key]
            if game_state.get_panel_state(panel_key).is_active():
                panel.activate()
            else:
                panel.deactivate()

    def handle_mouse_event(self, mouse_event):
        """
        :type mouse_event: src.main.GUI.Controller.mouseEvent.MouseEvent
        """
        for panel in self.__panels.values():
            if panel.is_active():
                change_event = panel.handle_mouse_event(mouse_event)
                if change_event:
                    return change_event

    def handle_key_event(self, key_event):
        """
        :type key_event: src.main.GUI.Controller.keyEvent.KeyEventTypes
        """
        for panel in self.__panels.values():
            if panel.is_active():
                change_event = panel.handle_key_event(key_event)
                if change_event:
                    return change_event
