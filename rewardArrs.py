"""
file to hold 2D arrays that hold the reward data for the various maps
"""

import math

class Rewards:   
    
    # This function can create a 2d array of dimmensions size x size.
    # The values of the array are calculated as (maxReward - 5*dist)
    # where the max reward is 100 and dist is the disance of the (i,j) from (x,y)
    # where (x,y) is the goal/player position #
    def trainer0RewardArr(self, x, y, size):
        """
        function to automate the process of creating a 20x20 array of 
        reward values that converge on the player position 
            (player position being the highest reward 
            with the rewards shrinking the father from the player you get)
            
        The maximum value (i.e. the value at the player pos) would be the maximum 
        distance from any corner of the grid. Say the player has coordinates x,y. 
        The corners are at 0,0 19,0 0,19 and 19,19. Then the maximum value 
        would be the maximum of x+y, 19-x+y, x+19-y and 19-x+19-y. 
        Then, for each point in the grid with coordinates i,j you enter 
        (max value - distance from x,y to i,j), 
        so the neighbors of * have maxvalue -1, their neighbors have maxvalue -2, etc. 
        
        """
        x = x // 16
        y = y // 16
        
        maxReward = 100
        
        trainerArr = []
        
        for i in range(size):
            col = []
            for j in range(size):
                dist = math.sqrt((i-x)**2 + (j-y)**2)
                reward = (maxReward - 5*dist)
                col.append(reward)
            trainerArr.append(col)
            
        return trainerArr
        
        
        