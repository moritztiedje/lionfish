import pygame
from main.tileMap import arrayFromFile
from main.gui import GUI


display_width = 800
display_height = 600

window = GUI(display_width, display_height)
clock = pygame.time.Clock()
gameOver = False
area_map = arrayFromFile('./dummyMap')

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    window.display(area_map)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
