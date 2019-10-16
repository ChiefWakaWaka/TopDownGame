import pygame

WHITE = (255, 255, 255)

class Character():
    def __init__(self, movespeed, camPosX, camPosY):
        self.movespeed = movespeed
        self.mapspeed = movespeed / 1000
        self.xPos = camPosX - 250
        self.yPos = camPosY - 250

    def drawEntity(self, game_display, camPosX, camPosY):
        pygame.draw.rect(game_display, WHITE, [295, 259, 10, 10])

    def drawMap(self, game_display):
        pygame.draw.rect(game_display, WHITE, [17.5 + self.xPos * self.mapspeed, 17.5 + self.yPos * self.mapspeed, 5, 5])
