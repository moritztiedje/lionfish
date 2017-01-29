import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
gameOver = False
border = pygame.image.load('../artwork/border.png')





def field(x, y):
    gameDisplay.blit(border, (x, y))

x =  (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
car_speed = 0

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    gameDisplay.fill(white)
    for x in range(0,8):
        for y in range(0,8):
            gameDisplay.blit(border, (- 100 + x*208,  - 100 + y*104))
            gameDisplay.blit(border, (- 100 + x*208 + 104, -100 + 52 + y*104))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()


