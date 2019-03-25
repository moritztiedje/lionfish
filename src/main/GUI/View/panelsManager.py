import pygame

from src.main.GUI.BaseComponents.button import Button
from src.main.GUI.View.image import Image
from src.main.GUI.View.panels.areaMapPanel import AreaMapPanel
from src.main.GUI.View.panels.menuPanel import MenuPanel
from src.main.GUI.View.panels.textAdventurePanel import TextAdventurePanel
from src.main.GUI.View.panels.worldMapPanel import WorldMapPanel
from src.main.Util.point import Point


class PanelsManager:
    def __init__(self, game_window):
        """
        :type game_window: main.gameWindow.GameWindow
        """

        # The order of these views is equivalent to z-index
        self.__panels = [
            self.__build_area_map_view(game_window),
            self.__build_world_map_view(game_window),
            self.__build_main_menu_view(game_window),
            self.__build_text_adventure_panel(game_window),
        ]

        # TODO use enum here
        self.__panels[0].activate()
        self.__panels[2].activate()
        self.__panels[3].activate()

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
        # TODO: Use enums here
        self.__panels[0].deactivate()
        self.__panels[1].activate()

    def __camera_zoom_in(self):
        for view in self.__panels:
            if view.is_active():
                view.zoom_in()

    def __camera_zoom_out(self):
        for view in self.__panels:
            if view.is_active():
                view.zoom_out()

    def draw(self, game_state):
        for view in self.__panels:
            if view.is_active():
                view.draw(game_state)

    def handle_mouse_event(self, mouse_event):
        """
        :type mouse_event: src.main.GUI.Controller.mouseEvent.MouseEvent
        """
        for panel in self.__panels:
            if panel.is_active():
                panel.handle_mouse_event(mouse_event)

    def __build_text_adventure_panel(self, game_window):
        return TextAdventurePanel(game_window)
