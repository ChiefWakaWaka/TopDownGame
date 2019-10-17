import pygame
from pygame.locals import *
import os
from maprender import *
from Chambers import *
from character import Character
from enemies import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
display_width = 600
display_height = 600

camPosX = display_width / 2
camPosY = display_height / 2

game_display = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Dungeon Crawler')
clock=pygame.time.Clock()

map = maprender()
maparray = map.createMap()
#print(maparray)
mapSprites = []

mapSearchX = 0
mapSearchY = 0

for i in range(len(maparray) * len(maparray[0])):
    if maparray[mapSearchX][mapSearchY] == 2:
        mapSprites.append(Room(mapSearchX, mapSearchY))
    if maparray[mapSearchX][mapSearchY] == 3:
        mapSprites.append(HorizTunnel(mapSearchX, mapSearchY))
    if maparray[mapSearchX][mapSearchY] == 4:
        mapSprites.append(VertTunnel(mapSearchX, mapSearchY))
    mapSearchX += 1
    if (mapSearchX == len(maparray)):
        mapSearchY += 1
        mapSearchX = 0

entityGroup = []
player = Character(25, camPosX, camPosY)
entityGroup.append(player)
mapSprites.append(player)

enemyGroup = []
for i in range(500):
    enemyGroup.append(Zombie(10, camPosX, camPosY, player))

def event_handler():
    for event in pygame.event.get():
        #print(event)
        if event.type == QUIT or (
             event.type == KEYDOWN and (
              event.key == K_ESCAPE or
              event.key == K_q
             )):
            pygame.quit()
            quit()

def keybinds():
    keys = pygame.key.get_pressed()
    global camPosX, camPosY
    if keys[pygame.K_w]:
        camPosY += player.movespeed
        player.yPos -= player.movespeed
    if keys[pygame.K_a]:
        camPosX += player.movespeed
        player.xPos -= player.movespeed
    if keys[pygame.K_s]:
        camPosY -= player.movespeed
        player.yPos += player.movespeed
    if keys[pygame.K_d]:
        camPosX -= player.movespeed
        player.xPos += player.movespeed
    if keys[pygame.K_r]:
        os.exec*()
#    print(player.xPos, player.yPos)
    #print(enemyGroup[0].xPos,enemyGroup[0].yPos)

def BGDraw():
    game_display.fill(BLACK)
    for obj in mapSprites:
        if obj != player:
            obj.drawEntity(game_display, camPosX, camPosY)

def EntityDraw():
    for obj in entityGroup:
        obj.drawEntity(game_display, camPosX, camPosY)

def DrawMap():
    for obj in mapSprites:
        obj.drawMap(game_display)

def EnemyDraw():
    for obj in enemyGroup:
        obj.drawEntity(game_display, camPosX, camPosY)
        obj.move()

while True:
    event_handler()
    keybinds()
    BGDraw()
    EntityDraw()
    EnemyDraw()
    DrawMap()
    #Mouse_x, Mouse_y = pygame.mouse.get_pos()
    pygame.display.update()
    clock.tick(60)
