"""
File for enemy functions (AI functionality for movement and attacks and things)
"""
import pygame
import game
from pygame.locals import *
#from rewardArrs import Rewards
from pyqlearning.qlearning.greedy_q_learning import GreedyQLearning
from pytmx.util_pygame import load_pygame
    
    
class Enemy():
    def __init__(self):
        pass
    
    def getMapProperties(self, x, y):
        xTile = x // 16
        yTile = y // 16
        
        
        wallProp = game.Game().tmxdata.get_tile_properties(xTile, yTile, 0)
        #print("got wall props")
        if wallProp is None:
            wallProp = {"solid":0, "stairs":0}
        return wallProp
    
    def getLegalActions(self, x, y):
        """
        Get a list of the legal actions from the current state
        
        *use a similar method used for stopping the player 
            movement to find find the legal moves (look at getMapProperties and move)
                (i.e. if the adjacent tile is solid then it is not legal)
                    (this also means we don't have to worry 
                    about the reward value of a wall location)
                    
        returns a list of North, South, East, or West 
                which will correspond to movement vectors 
                (i.e. North = (0,-16) it's -16 because pygame 
                has the origin at the top left and the blocks are each 16 pixels long/wide)
        """
        
        legalActions = []
        
        westTile = self.getMapProperties(x-5, y)
        eastTile = self.getMapProperties(x+64, y)
        northTile = self.getMapProperties(x, y)
        southTile = self.getMapProperties(x, y+64)
        
        if westTile[0]['solid'] == 1:
            legalActions = ["North", "South", "East"]
        elif eastTile[0]['solid'] == 1:
            legalActions = ["North", "South", "West"]
        elif northTile[0]['solid'] == 1:
            legalActions = ["South", "East", "West"]
        elif southTile[0]['solid'] == 1:
            legalActions = ["North", "East", "West"]
        else:
            legalActions = ["North", "South", "East", "West"]
            
        return legalActions
    
    def getRewardVal(self, state, world):
        """
        given a state, get the reward value for that state
        """
        pass
    
    def moveAgent(self, x, y, tmxdata):
        """
        Similar to 'update' function in qlearningAgents.py from hw
        use pyqlearning functions to compute Q(s,a)
        funcs available to use:
            *get_epsilon_greedy_rate(self)
            *set_epsilon_greedy_rate(self, value)
            *select_action(self, state_key, next_action_list)
            
            use Q(s,a) to move the agent
            
        need to define some other funcs first though:
            *getLegalActions() => return legal actions from curState
            *getRewardVal() => get the reward value of a given state
            *initialize() => this func would prepare everything like
                            the map data and the reward data and things like that
            *
        """
        
        legalActions = self.getLegalActions(x, y)
        
        GreedyQLearning.select_action((x, y), legalActions)
        
        # returns a tuple of coordinates that the main game loop uses to update the position
        return (x, y)
        
        pass