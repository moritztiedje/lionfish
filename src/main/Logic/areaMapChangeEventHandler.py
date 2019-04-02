from src.main.constants import Panels


class AreaMapChangeEventHandler:
    @staticmethod
    def enter_area(game_state, coordinate):
        """
        :type game_state: src.main.Model.gameState.GameState
        :type coordinate: src.main.GUI.BaseComponents.geometry.Point
        """
        area_map = game_state.get_area_map()
        player = game_state.get_player()
        if area_map.destination_accessible_from_origin(coordinate, player.get_position_in_area()):
            player.set_destination(coordinate)
            game_state.get_panel_state(Panels.TextAdventureBox).show()
            game_state.get_panel_state(Panels.AreaMap).deactivate()
            return True
