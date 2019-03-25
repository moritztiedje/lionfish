import pygame

from src.main.GUI.BaseComponents.button import Button
from src.main.GUI.View.image import Image
from src.main.GUI.View.panels.areaMapPanel import AreaMapPanel
from src.main.GUI.View.panels.menuPanel import MenuPanel
from src.main.GUI.View.panels.textAdventurePanel import TextAdventurePanel
from src.main.GUI.View.panels.worldMapPanel import WorldMapPanel
from src.main.Model.gameStateChangeEvent import GameStateChangeEvent, GameStateChangeEventTypes
from src.main.Util.point import Point
from src.main.constants import Panels


class PanelsManager:
    def __init__(self, game_window):
        """
        :type game_window: main.gameWindow.GameWindow
        """
        self.__panels = {
            Panels.AreaMap: self.__build_area_map_view(game_window),
            Panels.WorldMap: self.__build_world_map_view(game_window),
            Panels.MainMenuBar: self.__build_main_menu_view(game_window),
            Panels.TextAdventureBox: self.__build_text_adventure_panel(game_window)
        }

    def __build_area_map_view(self, game_window):
        world_map_button = Button(Point(game_window.get_width() - 130, game_window.get_height() - 40),
                                  Point(game_window.get_width() - 50, game_window.get_height() - 10),
                                  Image(0, 0, '../../artwork/images/worldButton.png'),
                                  self.__set_world_map_active)
        area_map_view = AreaMapPanel(game_window)
        area_map_view.register_button(world_map_button)
        return area_map_view

    def __build_main_menu_view(self, game_window):
        main_menu_button = Button(Point(game_window.get_width() - 40, game_window.get_height() - 40),
                                  Point(game_window.get_width() - 10, game_window.get_height() - 10),
                                  Image(0, 0, '../../artwork/images/menu/gear.png'),
                                  self.__quit_game)
        zoom_in_button = Button(Point(game_window.get_width() - 40, game_window.get_height() - 80),
                                Point(game_window.get_width() - 10, game_window.get_height() - 50),
                                Image(0, 0, '../../artwork/images/menu/magnify.png'),
                                self.__camera_zoom_in)
        zoom_out_button = Button(Point(game_window.get_width() - 40, game_window.get_height() - 120),
                                 Point(game_window.get_width() - 10, game_window.get_height() - 90),
                                 Image(0, 0, '../../artwork/images/menu/reduce.png'),
                                 self.__camera_zoom_out)
        main_menu_view = MenuPanel(game_window)
        main_menu_view.register_button(main_menu_button)
        main_menu_view.register_button(zoom_in_button)
        main_menu_view.register_button(zoom_out_button)
        return main_menu_view

    @staticmethod
    def __build_world_map_view(game_window):
        return WorldMapPanel(game_window)

    @staticmethod
    def __quit_game():
        pygame.quit()
        quit()

    def __set_world_map_active(self):
        """
        :rtype: src.main.Model.gameStateChangeEvent.GameStateChangeEvent
        """
        return GameStateChangeEvent(GameStateChangeEventTypes.GoToWorldMap, None)

    def __camera_zoom_in(self):
        for view in self.__panels:
            if view.is_active():
                view.zoom_in()

    def __camera_zoom_out(self):
        for view in self.__panels:
            if view.is_active():
                view.zoom_out()

    def draw(self, game_state):
        """
        :type game_state: src.main.Model.gameState.GameState
        """
        for z_index in range(3):
            for panel_key in self.__panels.keys():
                if self.__panels[panel_key].has_z_index(z_index):
                    if game_state.is_panel_active(panel_key):
                        self.__panels[panel_key].activate()
                        self.__panels[panel_key].draw(game_state)
                    else:
                        self.__panels[panel_key].deactivate()

    def handle_mouse_event(self, mouse_event):
        """
        :type mouse_event: src.main.GUI.Controller.mouseEvent.MouseEvent
        """
        for panel_key in self.__panels:
            panel = self.__panels[panel_key]
            if panel.is_active():
                change_event = panel.handle_mouse_event(mouse_event)
                if change_event:
                    return change_event

    def __build_text_adventure_panel(self, game_window):
        return TextAdventurePanel(game_window)
