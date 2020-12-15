"""
    This file is to store the training methods used for the AI to find the best possible route to player and get better each time run
"""


import sys
import random
import pygame
import math
from rewardsArry import Rewards
from player import Player
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




class training_game:
    def __init__(self):
        self.screen = pygame.display.set_mode((640, 640)) # set screen size
        pygame.display.set_caption("Untitled Rogue-like Game") # set display caption
        self.clock = pygame.time.Clock() # create clock
        self.running = True # init running to true, change to false when exit button clicked
        self.tmxdata = load_pygame("rooms\\basic_room.tmx") # Load map from tmx file
        self.playerX = 320
        self.playerY = 500
    
    #game loop
    def runtrainig(self):
        print("run trainig")
        while self.running:
            #print("running")
            self.screen.fill((255,255,255))
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




# start draw_map()
def drawMap(self):
    #print("draw map")
    for layer in self.tmxdata:
        for tiles in layer.tiles():
            xPixel = tiles[0] * 16
            yPixel = tiles[1] * 16
            mapImg = tiles[2]
            self.screen.blit(mapImg, (xPixel, yPixel))




class training_method:
    
    # start of the training episode
    def startEpisode(self):
   
        self.lastState = None
        self.lastAction = None
        self.episodeRewards = 0.0
    
    # end of training episode
    def stopEpisode(self):
    
        if self.episodesSoFar < self.numTraining:
            self.accumTrainRewards += self.episodeRewards
        else:
            self.accumTestRewards += self.episodeRewards
        self.episodesSoFar += 1
    
    def __init__(self, actionFn = None, numTraining=100):


        if actionFn == None:
            actionFn = lambda state: state.getLegalActions()
        self.actionFn = actionFn
        self.episodesSoFar = 0
        self.accumTrainRewards = 0.0
        self.accumTestRewards = 0.0
        self.numTraining = int(numTraining)
    
    
    def registerInitialState(self, state):
        self.startEpisode()
        if self.episodesSoFar == 0:
            print('Beginning %d episodes of Training' % (self.numTraining))
    
# start training()
    def training(x,y):
        maxReward = 100
        minReward = 0
        Total_Reward = 0 # keep a running total of rewards
        
        
        for i in trainerArr:
            while not done:
                action = env.action_space.sample()
                state, reward, done, info = env.step(action)


                #penalty for walking into wall
                if reward == -100:
                    penalties += 1
                    Total_Reward
                
                # reward not the max means continue
                if reward < MaxReward:


                # getting to Max reward
                if reward == MaxReward




print( 'Trianing done, Episodes' %(Episodes) 'reward' %(Total_Reward))