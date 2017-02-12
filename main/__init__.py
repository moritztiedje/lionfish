import pygame

from main.GUI.button import Button
from main.GUI.point import Point
from main.GUI.view import AreaMapView
from main.tileMap import array_from_file
from main.GUI.gui import GUI
from main.gameState import GameState


display_width = 800
display_height = 600

game_state = GameState()
world_map_button = Button(Point(720, 570), Point(800, 600), pygame.image.load('../artwork/images/worldButton.png'), game_state.set_world_map_active)
window = GUI(display_width, display_height, world_map_button)

clock = pygame.time.Clock()
gameOver = False
area_map = array_from_file('./dummyMap')

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    window.trigger_control_logic(game_state)

    window.display(game_state)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
