from enum import Enum


class GameStateChangeEvent:
    def __init__(self, event_type, payload):
        self.event_type = event_type
        self.payload = payload


class GameStateChangeEventTypes(Enum):
    EnterArea = 0
    GoToWorldMap = 1
    SelectTextAdventureOption = 2
