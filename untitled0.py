# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 09:56:55 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
import random


mc = Minecraft.create()

x,y,z = mc.player.getPos()


for i in range(5,20,5):
    print(i)
while True:
   x = x + random.uniform(-20,20)
   z = z + random.uniform(-20,20)
   y = y + 100
   mc.spawnEntity(x,y,z,100)
   time.sleep(0.1)