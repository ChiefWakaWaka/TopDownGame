import numpy as np
import random

class maprender:
    def __init__(self):
        self.roomCnt = 3 #Locked for now

    def createMap(self):
        roomCnt = self.roomCnt
        mapsize = roomCnt * 3

        map = np.ones((mapsize, mapsize))
        walkX, walkY = int((mapsize - 1 )/ 2), int((mapsize - 1) / 2)
        i = 0
        while i < roomCnt - 1:
            map[walkX][walkY] = 2
            randNum = random.randint(0,3)
            if randNum == 0:
                walkX += 1
                map[walkX][walkY] = 3
                walkX += 1

            if randNum == 1:
                walkX -= 1
                map[walkX][walkY] = 3
                walkX -= 1

            if randNum == 2:
                walkY += 1
                map[walkX][walkY] = 4
                walkY += 1

            if randNum == 3:
                walkY -= 1
                map[walkX][walkY] = 4
                walkY -= 1

            if map[walkX][walkY] != 2:
                map[walkX][walkY] = 2
                i+=1

        while np.sum(map, axis=0)[0] == len(map) and np.sum(map, axis=1)[0] == len(map):
            map = np.delete(map, 0, axis = 0)
            map = np.delete(map, 0, axis = 1)

        while np.sum(map, axis=0)[0] == len(map[0]):
            map = np.delete(map, 0, axis = 0)

        while np.sum(map, axis=1)[0] == len(map):
            map = np.delete(map, 0, axis = 1)

        return map
