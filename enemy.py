"""
File for enemy functions (AI functionality for movement and attacks and things)
"""
import pygame
import game
from pygame.locals import *
from rewardArrs import Rewards
from pyqlearning.qlearning.greedy_q_learning import GreedyQLearning
from pyqlearning.q_learning import QLearning
from pytmx.util_pygame import load_pygame
    
    
class Enemy():
    def __init__(self, x, y):
        self.image = pygame.image.load("character PNGs\\goblin.png")
        self.x = x
        self.y = y
        self.path = [self.x, self.y]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57) # NEW
        self.health = 1000
        self.visible = True
    
    def draw(self, XYpos, screen):
        screen.blit(self.image, XYpos)
        
        if self.visible:
        # Drawing the health bar of the enemy.
            pygame.draw.rect(screen, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))

        # Substract from the health bar width each time enemy is hit
            pygame.draw.rect(screen, (0,255,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            
        # Creating a hitbox around the character.
            self.hitbox = (self.x + 15, self.y + 10, 29, 52)
            
    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('Enemy hit')
    
    
    # used to tell when an adjacent tile is a wall or not
    def getMapProperties(self, x, y):
        # tile size is 16x16 so dividing the coordinates by 16 gives the tile #
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
        create rewardArrs in game.py and use those in testing
        
        world == rewardArr for given environment
        """
        x, y = state
        
        reward = world[x][y]
        
        return reward
    
    
    def getQvals(self):
        return QLearning.get_q_df()
    
    def checkForEnvDrift(self):
        """
        function to detect environmental drift;
        
        Search the entire state space for a change in rewards compared to the
        original environment
        """
        pass
    
    def performPrioritizedSweeping(self):
        """
        given a change in the environment, perform a prioritized sweep of the new
        environment and update the value functions of state, action pairs
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
        
        action = GreedyQLearning.select_action((x, y), legalActions)
        
        # returns a tuple of coordinates that the main game loop uses to update the position
        return (x, y)