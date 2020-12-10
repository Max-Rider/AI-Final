"""
File for enemy functions (AI functionality for movement and attacks and things)
"""
from pyqlearning.qlearning.greedy_q_learning import GreedyQLearning
import rewardarrs

    
    
class Enemy():
    def __init__(self):
        pass
    
    def getLegalActions(self, currState):
        """
        Get a list of the legal actions from the current state
        
        *use a similar method used for stopping the player 
            movement to find find the legal moves
                (if the adjacent tile is solid then it is not legal)
        return a list of North, South, East, West 
                which will correspond to movement vectors 
                (i.e. North = (0,-16) it's -16 because pygame 
                has the origin at the top left and the blocks are each 16 pixels long/wide)
                
        """
        pass
    
    def moveAgent(self):
        """
        use pyqlearning functions to compute Q(s,a)
        funcs available to use:
            *get_epsilon_greedy_rate(self)
            *set_epsilon_greedy_rate(self, value)
            *select_action(self, state_key, next_action_list)
            
        need to define some other funcs though:
            *getLegalActions()
            *getRewardVal
            *initialize => this func would prepare everything like
                            the map data and the reward data and things like that
            *
        """
        pass