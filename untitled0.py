# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 09:56:55 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
import random


mc=Minecraft.create()

while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits > [0]
        x ,y ,z = hit.pos.x, hit.pos.y, hit.pos.z
        block=mc.getBlock(x,y,z,41)
        mc.postToChat("恭喜你獵到了"+str(block))
        