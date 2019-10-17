import pygame

WHITE = (255, 255, 255)
RED = (100, 0, 0)

class Character():
    def __init__(self, movespeed, camPosX, camPosY):
        self.movespeed = movespeed
        self.mapspeed = movespeed / 1000
        self.xPos = camPosX - 250
        self.yPos = camPosY - 250

    def drawEntity(self, game_display, camPosX, camPosY):
        pygame.draw.rect(game_display, WHITE, [297.5, 297.5, 5, 5])
        Mouse_x, Mouse_y = pygame.mouse.get_pos()
        pygame.draw.circle(game_display, RED, [Mouse_x, Mouse_y], 5)

    def drawMap(self, game_display):
        pygame.draw.rect(game_display, WHITE, [17.5 + self.xPos * self.mapspeed, 17.5 + self.yPos * self.mapspeed, 5, 5])

    def collisionDetect(self, roomObjects):
        for obj in roomObjects:
            if self.xPos > obj.xPos * 500 and self.xPos < obj.xPos * 500 + 250:
                print('x true')
                if self.yPos > obj.yPos * 500 and self.yPos < obj.yPos * 500 + 250:
                    print('y true')
                return True
            else:
                return False
