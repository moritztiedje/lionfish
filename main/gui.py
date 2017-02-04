import pygame


class GUI:
    def __init__(self, display_width, display_height):
        pygame.init()
        self.__game_display = pygame.display.set_mode((display_width, display_height))

        self.__border = pygame.image.load('../artwork/images/border.png')
        self.__water = pygame.image.load('../artwork/images/water.png')
        self.__white = (255, 255, 255)

    def display(self, area_map):
        self.__game_display.fill(self.__white)

        is_even_line = True
        for x in range(0, len(area_map)):
            for y in range(0, len(area_map[x])):
                if is_even_line:
                    coordinate = (x * 104, y * 104)
                else:
                    coordinate = (x * 104, y * 104 + 52)

                if area_map[x][y] == 1:
                    self.__game_display.blit(self.__border, coordinate)
                if area_map[x][y] == 0:
                    self.__game_display.blit(self.__water, coordinate)

            is_even_line = not is_even_line
