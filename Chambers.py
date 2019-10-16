import pygame

GRAY = (30, 30, 30)
LIGHT_GRAY = (60, 60, 60)
LIGHTER_GRAY = (70, 70, 70)
LIGHTEST_GRAY = (100, 100, 100)

class Room():
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos

    def drawEntity(self, game_display, camPosX, camPosY):
        pygame.draw.rect(game_display, GRAY, [camPosX + self.xPos * 500, camPosY + self.yPos * 500, 500, 500])

    def drawMap(self, game_display):
        pygame.draw.rect(game_display, LIGHT_GRAY, [10 + self.xPos * 20, 10 + self.yPos * 20, 20, 20])

class HorizTunnel():
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos

    def drawEntity(self, game_display, camPosX, camPosY):
        pygame.draw.rect(game_display, LIGHTER_GRAY, [camPosX + self.xPos * 500, camPosY + 125 + self.yPos * 500, 500, 250])

    def drawMap(self, game_display):
        pygame.draw.rect(game_display, LIGHTEST_GRAY, [10 + self.xPos * 20, 15 + self.yPos * 20, 20, 10])

class VertTunnel():
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos

    def drawEntity(self, game_display, camPosX, camPosY):
        pygame.draw.rect(game_display, LIGHTER_GRAY, [camPosX + 125 +self.xPos * 500, camPosY + self.yPos * 500, 250, 500])

    def drawMap(self, game_display):
        pygame.draw.rect(game_display, LIGHTEST_GRAY, [15 + self.xPos * 20, 10 + self.yPos * 20, 10, 20])
