import pygame
import math

GREEN = (38, 122, 44)

class Zombie:
    def __init__(self, health, camPosX, camPosY, player):
        self.moveSpeed = 0.5
        self.senseRange = 5000
        self.health = health
        #self.xPos = camPosX + 110
        #self.yPos = camPosY
        self.xPos = 100
        self.xPos = 100
        self.player = player

    def drawEntity(self, game_display, camPosX, camPosY):
        pygame.draw.rect(game_display, GREEN, [camPosX + self.xPos, camPosY + self.yPos, 10, 10])

    def move(self):
        if math.sqrt((self.player.xPos - self.xPos) ** 2 + (self.player.yPos - self.yPos) ** 2) < self.senseRange:
            yDelta = (self.player.yPos - self.yPos)
            xDelta = (self.player.xPos - self.xPos)
            self.xPos += xDelta
            self.yPos += yDelta
            '''if (self.xPos < playerXPos):
                self.xPos += self.moveSpeed * movementSlope
                self.yPos -= self.moveSpeed
            elif (self.xPos > playerXPos):
                self.xPos -= self.moveSpeed * movementSlope
                self.yPos += self.moveSpeed
'''
