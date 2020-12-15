""" 
This file is meant to be used to test various parts of the final game in static, mostly blank world.
The world is created using Tiled and pyTMX.

Features to test here include initial player movement, player attacking, enemy AI movement, and enemy attacking.
"""
import sys
import random
import pygame
from pygame.locals import *
from pytmx.util_pygame import load_pygame

#INITIALIZE GAME
pygame.init()
pygame.display.set_caption("Dungeon Crawler")
win = pygame.display.set_mode((640,640))
clock = pygame.time.Clock()
wizard = pygame.image.load("tile PNGs\\blueWizard.png") # Load player sprite
tmxdata = load_pygame("rooms\\basic_room.tmx") # Load map from tmx file


class player(object):
    #Initialization function 
    def __init__(self, x,y, width, height):
        self.x = x
        self.y = y
        self.width = width 
        self.height = height 
        self.vel = 5
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.walkCount = 0
        
        
    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
            #ADD SPRITES BASED ON WHICH DIRECTION ITS FACING
        if self.left:
            win.blit(wizard[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(wizard[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        elif self.up:
            win.blit(wizard[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        elif self.down:
            win.blit(wizard[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1


def getLocProperties(tmxdata, xPos, yPos):
    xTile = xPos // 16
    yTile = yPos // 16
    wallProp = tmxdata.get_tile_properties(xTile, yTile, 0)
    stairProp = tmxdata.get_tile_properties(xTile, yTile, 1)
    
    if wallProp is None: # set default properties if none are found
        wallProp = {"solid":0, "stairs":0}
        stairProp = {"solid":0, "stairs":0}
    return (wallProp, stairProp)
# end getLocProperties

def draw_map():

    """
    #tmxdata = load_pygame("rooms\\basic_room.tmx") # Load map from tmx file
    for layer in tmxdata:
        for tiles in layer.tiles():
            xPixelPos = tiles[0] * 16 #+ world_offset
            yPixelPos = tiles[1] * 16 #+ world_offset
            mapImg = tiles[2] #get img to draw from tmxdata
            win.blit(mapImg, (xPixelPos, yPixelPos)) #draw map to screen
    """
    win.blit(bg, (0,0))
    p1.draw(win)
    
    pygame.display.update()
# end draw_map()



#MAIN LOOP
p1 = player(320, 500, 64, 64)
running = True

while running: 
    win.fill((255,255,255)) # Screen starts white before doing anything else
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
            
    if keys[pygame.K_LEFT] and p1.x > p1.vel:
        p1.x -= p1.vel
        p1.left = True
        p1.right = False
    elif keys[pygame.K_RIGHT] and p1.x < 500 - p1.width - p1.vel:
        p1.x += p1.vel
        p1.right = True
        p1.left = False
    else:
        p1.right = False
        p1.left = False
        p1.walkCount = 0
        
    
    """
    if keys[ord("a")]: # check what key was pressed
        p1.westTile = getLocProperties(tmxdata, xPos-2, yPos+11) #find the tile next to the player and get its properties
        if p1.westTile[0]['solid'] == 0: # if not solid keep moving, stop otherwise
            xPos += -1
    if keys[ord("d")]:
        p1.eastTile = getLocProperties(tmxdata, xPos+22, yPos+11)
        if p1.eastTile[0]['solid'] == 0:
            xPos += 1
    if keys[ord("w")]:
        p1.northTile = getLocProperties(tmxdata, xPos, yPos-2)
        if p1.northTile[0]['solid'] == 0:
            yPos += -1
    if keys[ord("s")]:
        p1.southTile = getLocProperties(tmxdata, xPos+2, yPos+22)
        if p1.southTile[0]['solid'] == 0:
            yPos += 1
    
"""
    draw_map()
    
    
    
    
pygame.quit()




