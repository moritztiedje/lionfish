from src.main.constants import Panels


class AreaMapChangeEventHandler:
    @staticmethod
    def enter_area(game_state, coordinate):
        """
        :type game_state: src.main.Model.gameState.GameState
        :type coordinate: src.main.GUI.BaseComponents.geometry.Point
        """
        area_map = game_state.get_area_map()
        if area_map.fields_are_connected(coordinate, game_state.get_player_position_in_area()):
            game_state.get_panel_state(Panels.TextAdventureBox).show()
            game_state.get_panel_state(Panels.AreaMap).deactivate()
