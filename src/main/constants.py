from enum import Enum

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

SQUARE_FIELD_WIDTH = 50
SQUARE_FIELD_HEIGHT = 50

HEXAGON_FIELD_WIDTH = 152
HEXAGON_FIELD_SIDE_WIDTH = 48
HEXAGON_FIELD_CENTER_WIDTH = 56
HEXAGON_FIELD_WIDTH_SPACING = HEXAGON_FIELD_WIDTH - HEXAGON_FIELD_SIDE_WIDTH

SPRITE_IN_HEXAGON_WIDTH = 40
SPRITE_IN_HEXAGON_HEIGHT = 40

HEXAGON_FIELD_HEIGHT = 104


class Panels(Enum):
    AreaMap = 0
    TextAdventureBox = 1
    WorldMap = 2
    MainMenuBar = 3
    GameOverPanel = 4


class AreaImageEnum(Enum):
    EMPTY = 1
    WATER = 2
    PLAYER = 90


class GameOverImageEnum(Enum):
    BACKGROUND = 0


class PlayerSkills(Enum):
    ENDURE = 0
    FORCE = 1
    FIGHT = 2
    SNEAK = 3
    MOVE = 4
    SHOOT = 5
    SCOUT = 6
    COMPREHEND = 7
    OCCULT_KNOWLEDGE = 8
    SENSE_EMOTION = 9
    MANIPULATE = 10
    HEAL = 11

    def __str__(self):
        if self is PlayerSkills.ENDURE:
            return 'endure'
        if self is PlayerSkills.FORCE:
            return 'force'
        if self is PlayerSkills.FIGHT:
            return 'fight'
        if self is PlayerSkills.SNEAK:
            return 'sneak'
        if self is PlayerSkills.MOVE:
            return 'move'
        if self is PlayerSkills.SHOOT:
            return 'shoot'
        if self is PlayerSkills.SCOUT:
            return 'scout'
        if self is PlayerSkills.COMPREHEND:
            return 'comprehend'
        if self is PlayerSkills.OCCULT_KNOWLEDGE:
            return 'occult knowledge'
        if self is PlayerSkills.SENSE_EMOTION:
            return 'sense emotion'
        if self is PlayerSkills.MANIPULATE:
            return 'manipulate'
        if self is PlayerSkills.HEAL:
            return 'heal'
