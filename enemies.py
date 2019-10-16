import pygame
import math

GREEN = (38, 122, 44)

class Zombie:
    def __init__(self, health, camPosX, camPosY):
        self.moveSpeed = 0.5
        self.senseRange = 500
        self.health = health
        self.xPos = camPosX + 110
        self.yPos = camPosY

    def drawEntity(self, game_display, camPosX, camPosY):
        pygame.draw.rect(game_display, GREEN, [camPosX + self.xPos, camPosY + self.yPos, 10, 10])

    def move(self, playerXPos, playerYPos):
        if math.sqrt((playerXPos - self.xPos) ** 2 + (playerYPos - self.yPos) ** 2) < self.senseRange:
            movementSlope = (playerYPos - self.yPos) / (playerXPos - self.xPos)
            if (self.xPos < playerXPos):
                self.xPos += self.moveSpeed * movementSlope
                self.yPos -= self.moveSpeed
            elif (self.xPos > playerXPos):
                self.xPos -= self.moveSpeed * movementSlope
                self.yPos += self.moveSpeed
