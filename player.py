"""
File for player functions (move, attack, etc.)
"""
import game
import pygame
from pygame.locals import *
from pytmx.util_pygame import load_pygame

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("tile PNGs\\blueWizard.png")
        self.x = x
        self.y = y
        #self.speed
    
    def draw(self, XYpos, screen):
        screen.blit(self.image, XYpos)
    
    def getMapProperties(self, x, y):
        xTile = x // 16
        yTile = y // 16
        
        wallProp = game.Game().tmxdata.get_tile_properties(xTile, yTile, 0)
        stairProp = game.Game().tmxdata.get_tile_properties(xTile, yTile, 1)
        #print("got wall props")
        if wallProp is None and stairProp is None:
            wallProp = {"solid":0, "stairs":0}
            stairProp = {"solid":0, "stairs":0}
        return (wallProp, stairProp)
    
    def move(self, x, y, keyPressed, tmxdata):
        if keyPressed[ord("a")]: # check what key was pressed
            westTile = self.getMapProperties(x-2, y+11) #find the tile next to the player and get its properties
            if westTile[0]['solid'] == 0: # if not solid keep moving, stop otherwise
                x += -10
        if keyPressed[ord("d")]:
            eastTile = self.getMapProperties(x+22, y+11)
            if eastTile[0]['solid'] == 0:
                x += 10
        if keyPressed[ord("w")]:
            northTile = self.getMapProperties(x, y-2)
            if northTile[0]['solid'] == 0:
                y += -10
        if keyPressed[ord("s")]:
            southTile = self.getMapProperties(x+2, y+22)
            if southTile[0]['solid'] == 0:
                y += 10
        return(x, y)
    
    
    # def attack():
    #     pass