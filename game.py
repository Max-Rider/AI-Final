"""
Contains info to initialize the game (pygame init, screen init, map info/drawing, etc.)
"""
import player
import sys
import pygame
from pygame.locals import *
from pytmx.util_pygame import load_pygame

class Directions:
    NORTH = "North"
    SOUTH = 'South'
    EAST = 'East'
    WEST = 'West'
    STOP = 'Stop'
    
    LEFT = {NORTH: WEST,
            SOUTH: EAST,
            EAST:  NORTH,
            WEST:  SOUTH,
            STOP:  STOP}
    
    RIGHT = dict([(y, x) for x, y in list(LEFT.items())])

    REVERSE = {NORTH: SOUTH,
               SOUTH: NORTH,
               EAST: WEST,
               WEST: EAST,
               STOP: STOP}

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((640, 640)) # set screen size
        pygame.display.set_caption("Untitled Rogue-like Game") # set display caption
        self.clock = pygame.time.Clock() # create clock
        self.running = True # init running to true, change to false when exit button clicked
        self.tmxdata = load_pygame("rooms\\basic_room.tmx") # Load map from tmx file
        self.playerX = 320
        self.playerY = 500
    
    #game loop
    def runGame(self):
        print("run game")
        while self.running:
            #print("running")
            self.screen.fill((255,255,255)) # init screen to white
            keyPressed = pygame.key.get_pressed()
            mousePressed = pygame.mouse.get_pressed()
            mouseX, mouseY = pygame.mouse.get_pos()
            self.getEvents()
            self.drawMap()
            #player.Player().draw()
            pygame.display.update()
            
    
    # handle all events in game
    def getEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #print("exit game")
                self.running = False
                
    def drawMap(self):
        #print("draw map")
        for layer in self.tmxdata:
            for tiles in layer.tiles():
                xPixel = tiles[0] * 16
                yPixel = tiles[1] * 16
                mapImg = tiles[2]
                self.screen.blit(mapImg, (xPixel, yPixel))