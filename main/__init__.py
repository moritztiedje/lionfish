import pygame
from main.tileMap import arrayFromFile

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
gameOver = False
border = pygame.image.load('../artwork/images/border.png')
water = pygame.image.load('../artwork/images/water.png')
area_map = arrayFromFile('./dummyMap')

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    gameDisplay.fill(white)

    for x in range(0, int(len(area_map)/2)):
        for y in range(0, len(area_map[x*2])):
            if area_map[x*2][y] == 1:
                gameDisplay.blit(border, (x * 208, y * 104))
            if area_map[x*2][y] == 0:
                gameDisplay.blit(water, (x * 208, y * 104))
        for y in range(0, len(area_map[x*2 + 1])):
            if area_map[x*2 + 1][y] == 1:
                gameDisplay.blit(border, (x * 208 + 104, 52 + y * 104))
            if area_map[x*2 + 1][y] == 0:
                gameDisplay.blit(water, (x * 208 + 104, 52 + y * 104))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
