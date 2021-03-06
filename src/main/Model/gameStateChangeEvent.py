from enum import Enum


class GameStateChangeEvent:
    def __init__(self, event_type, payload):
        self.event_type = event_type
        self.payload = payload


class GameStateChangeEventTypes(Enum):
    InternalGUIChange = -1
    EnterArea = 0
    GoToWorldMap = 1
    SelectTextAdventureOption = 2
    CloseTextAdventure = 3
