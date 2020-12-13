"""
file to hold 2D arrays that hold the reward data for the various maps
"""

import math

class Rewards:   
    
    # This function can create a 2d array of dimmensions size x size.
    # The values of the array are calculated as (maxReward - 5*dist)
    # where the max reward is 100 and dist is the disance of the (i,j) from (x,y)
    # where (x,y) is the goal/player position #
    def trainerRewardArr(self, x, y, size):
        """
        function to automate the process of creating a 20x20 array of 
        reward values that converge on the player position 
            (player position being the highest reward 
            with the rewards shrinking the father from the player you get)
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
        
        
        