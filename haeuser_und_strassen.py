#!/usr/bin/python
# -*- coding: utf-8 -*-
#--------------------------------------
#
# Author : Joerg Pfruender
# Apache License 2.0
# 
# Dank an Matt Hawkins fuer die Anleitung http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

def haus():
  pPos = mc.player.getTilePos()
  # boden
  mc.setBlocks(pPos.x+1,pPos.y-1,pPos.z+1,pPos.x+9,pPos.y-1,pPos.z+9,block.BRICK_BLOCK)
  # Vorderseite
  mc.setBlocks(pPos.x+1,pPos.y,pPos.z+1,pPos.x+9,pPos.y+2,pPos.z+1,block.BRICK_BLOCK)
  # Rueckseite
  mc.setBlocks(pPos.x+1,pPos.y,pPos.z+9,pPos.x+9,pPos.y+2,pPos.z+9,block.BRICK_BLOCK) #eigentlich x+1?
  # linke Seite
  mc.setBlocks(pPos.x+1,pPos.y,pPos.z+1,pPos.x+9,pPos.y+2,pPos.z+9,block.BRICK_BLOCK)
  # rechte Seite
  mc.setBlocks(pPos.x+1,pPos.y,pPos.z+1,pPos.x+9,pPos.y+2,pPos.z+9,block.BRICK_BLOCK)
  # in der Mitte Luft
  mc.setBlocks(pPos.x+2,pPos.y,pPos.z+2,pPos.x+8,pPos.y+2,pPos.z+8,block.AIR)
  # flaches Dach aus Glas
  #mc.setBlocks(pPos.x+1,pPos.y+3,pPos.z+1,pPos.x+9,pPos.y+3,pPos.z+9,block.GLASS)

  # schraeges Dach aus "Ziegeln"
  mc.setBlocks(pPos.x,pPos.y+3,pPos.z,pPos.x,pPos.y+3,pPos.z+10,block.REDSTONE_ORE)
  mc.setBlocks(pPos.x+10,pPos.y+3,pPos.z,pPos.x+10,pPos.y+3,pPos.z+10,block.REDSTONE_ORE)
  mc.setBlocks(pPos.x+1,pPos.y+3,pPos.z+1,pPos.x+1,pPos.y+3,pPos.z+9,block.BRICK_BLOCK)
  mc.setBlocks(pPos.x+9,pPos.y+3,pPos.z+1,pPos.x+9,pPos.y+3,pPos.z+9,block.BRICK_BLOCK)

  mc.setBlocks(pPos.x+1,pPos.y+3,pPos.z+1,pPos.x+9,pPos.y+3,pPos.z+1,block.BRICK_BLOCK)
  mc.setBlocks(pPos.x+1,pPos.y+3,pPos.z+9,pPos.x+9,pPos.y+3,pPos.z+9,block.BRICK_BLOCK)


  mc.setBlocks(pPos.x+1,pPos.y+4,pPos.z,pPos.x+1,pPos.y+4,pPos.z+10,block.REDSTONE_ORE)
  mc.setBlocks(pPos.x+9,pPos.y+4,pPos.z,pPos.x+9,pPos.y+4,pPos.z+10,block.REDSTONE_ORE)
  mc.setBlocks(pPos.x+2,pPos.y+4,pPos.z+1,pPos.x+8,pPos.y+4,pPos.z+1,block.BRICK_BLOCK)
  mc.setBlocks(pPos.x+2,pPos.y+4,pPos.z+9,pPos.x+8,pPos.y+4,pPos.z+9,block.BRICK_BLOCK)


  mc.setBlocks(pPos.x+2,pPos.y+5,pPos.z,pPos.x+2,pPos.y+5,pPos.z+10,block.REDSTONE_ORE)
  mc.setBlocks(pPos.x+8,pPos.y+5,pPos.z,pPos.x+8,pPos.y+5,pPos.z+10,block.REDSTONE_ORE)
  mc.setBlocks(pPos.x+3,pPos.y+5,pPos.z+1,pPos.x+7,pPos.y+5,pPos.z+1,block.BRICK_BLOCK)
  mc.setBlocks(pPos.x+3,pPos.y+5,pPos.z+9,pPos.x+7,pPos.y+5,pPos.z+9,block.BRICK_BLOCK)


  mc.setBlocks(pPos.x+3,pPos.y+6,pPos.z,pPos.x+3,pPos.y+6,pPos.z+10,block.REDSTONE_ORE)
  mc.setBlocks(pPos.x+7,pPos.y+6,pPos.z,pPos.x+7,pPos.y+6,pPos.z+10,block.REDSTONE_ORE)
  mc.setBlocks(pPos.x+4,pPos.y+6,pPos.z+1,pPos.x+6,pPos.y+6,pPos.z+1,block.BRICK_BLOCK)
  mc.setBlocks(pPos.x+4,pPos.y+6,pPos.z+9,pPos.x+6,pPos.y+6,pPos.z+9,block.BRICK_BLOCK)


  mc.setBlocks(pPos.x+4,pPos.y+7,pPos.z,pPos.x+4,pPos.y+7,pPos.z+10,block.REDSTONE_ORE)
  mc.setBlocks(pPos.x+6,pPos.y+7,pPos.z,pPos.x+6,pPos.y+7,pPos.z+10,block.REDSTONE_ORE)
  mc.setBlocks(pPos.x+5,pPos.y+7,pPos.z+1,pPos.x+5,pPos.y+7,pPos.z+1,block.BRICK_BLOCK)
  mc.setBlocks(pPos.x+5,pPos.y+7,pPos.z+9,pPos.x+5,pPos.y+7,pPos.z+9,block.BRICK_BLOCK)


  mc.setBlocks(pPos.x+5,pPos.y+8,pPos.z,pPos.x+5,pPos.y+8,pPos.z+10,block.REDSTONE_ORE)

  # Fenster in Vorderseite
  mc.setBlocks(pPos.x+2,pPos.y+1,pPos.z+1,pPos.x+3,pPos.y+1,pPos.z+1,block.GLASS)
  mc.setBlocks(pPos.x+7,pPos.y+1,pPos.z+1,pPos.x+8,pPos.y+1,pPos.z+1,block.GLASS)
  mc.setBlocks(pPos.x+5,pPos.y,pPos.z+1,pPos.x+5,pPos.y+1,pPos.z+1,block.DOOR_WOOD)
  
  # Fenster in linker Seite
  mc.setBlocks(pPos.x+1,pPos.y+1,pPos.z+3,pPos.x+1,pPos.y+1,pPos.z+4,block.GLASS)
  mc.setBlocks(pPos.x+1,pPos.y+1,pPos.z+6,pPos.x+1,pPos.y+1,pPos.z+7,block.GLASS)
  
  # Fenster in rechter Seite
  mc.setBlocks(pPos.x+9,pPos.y+1,pPos.z+3,pPos.x+9,pPos.y+1,pPos.z+4,block.GLASS)
  mc.setBlocks(pPos.x+9,pPos.y+1,pPos.z+6,pPos.x+9,pPos.y+1,pPos.z+7,block.GLASS)
  
  # Fenster in Rückseite
  mc.setBlocks(pPos.x+2,pPos.y+1,pPos.z+9,pPos.x+3,pPos.y+1,pPos.z+9,block.GLASS)
  mc.setBlocks(pPos.x+7,pPos.y+1,pPos.z+9,pPos.x+8,pPos.y+1,pPos.z+9,block.GLASS)
  mc.setBlocks(pPos.x+5,pPos.y,pPos.z+9,pPos.x+5,pPos.y+1,pPos.z+9,block.GLASS)

  return "Haus fertig"

# "Himmelrichtungen" sind ausgedacht.

def strasse_nach_sueden():
  pPos = mc.player.getTilePos()
  mc.setBlocks(pPos.x-2, pPos.y-1, pPos.z-50, pPos.x+2, pPos.y-1, pPos.z, block.COAL_ORE)
  mc.setBlocks(pPos.x-2, pPos.y, pPos.z-50, pPos.x+2, pPos.y, pPos.z, block.AIR)
  mc.setBlocks(pPos.x-2, pPos.y, pPos.z-50, pPos.x-2, pPos.y, pPos.z, block.FENCE)
  mc.setBlocks(pPos.x+2, pPos.y, pPos.z-50, pPos.x+2, pPos.y, pPos.z, block.FENCE)
  return "Strasse fertig"

def strasse_nach_osten():
  pPos = mc.player.getTilePos()
  mc.setBlocks(pPos.x, pPos.y-1, pPos.z-2, pPos.x-50, pPos.y-1, pPos.z+2, block.COAL_ORE)
  mc.setBlocks(pPos.x, pPos.y, pPos.z-2, pPos.x-50, pPos.y+4, pPos.z+2, block.AIR)
  mc.setBlocks(pPos.x, pPos.y, pPos.z-2, pPos.x-50, pPos.y, pPos.z-2, block.FENCE)
  mc.setBlocks(pPos.x, pPos.y, pPos.z+2, pPos.x-50, pPos.y, pPos.z+2, block.FENCE)
  return "Strasse fertig"

def strasse_nach_norden():
  pPos = mc.player.getTilePos()
  mc.setBlocks(pPos.x-2, pPos.y-1, pPos.z, pPos.x+2, pPos.y-1, pPos.z+50, block.COAL_ORE)
  mc.setBlocks(pPos.x-2, pPos.y, pPos.z, pPos.x+2, pPos.y+4, pPos.z+50, block.AIR)
  mc.setBlocks(pPos.x-2, pPos.y, pPos.z, pPos.x-2, pPos.y, pPos.z+50, block.FENCE)
  mc.setBlocks(pPos.x+2, pPos.y, pPos.z, pPos.x+2, pPos.y, pPos.z+50, block.FENCE)
  return "Strasse fertig"

# mc.postToChat(strasse_nach_norden())

