import pygame
import math
import random

GREEN = (38, 122, 44)

class Zombie:
    def __init__(self, health, camPosX, camPosY, player):
        self.moveSpeed = 0.01
        self.senseRange = 5000
        self.health = health
        self.xPos = camPosX + random.randint(-1000,1000)
        self.yPos = camPosY + random.randint(-1000,1000)
        #self.xPos = 100
        #self.xPos = 100
        self.player = player

    def drawEntity(self, game_display, camPosX, camPosY):
        pygame.draw.rect(game_display, GREEN, [self.xPos+camPosX-55, self.yPos+camPosY-91, 5, 5])

    def move(self):
        i = 2
        distance = math.sqrt((self.player.xPos - self.xPos) ** 2 + (self.player.yPos - self.yPos) ** 2)
        if distance < self.senseRange:
            yDelta = (self.player.yPos - self.yPos)
            xDelta = (self.player.xPos - self.xPos)
            if distance < 200:
                        i = 3
            if random.randint(0,i) == i:
                yDelta = (self.player.yPos - self.yPos)
                xDelta = (self.player.xPos - self.xPos)
                self.xPos += xDelta * self.moveSpeed
                self.yPos += yDelta * self.moveSpeed
            else:
                self.xPos += random.randint(-20,20) * self.moveSpeed
                self.yPos += random.randint(-20,20) * self.moveSpeed
