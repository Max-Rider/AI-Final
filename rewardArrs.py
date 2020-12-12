"""
file to hold 2D arrays that hold the reward data for the various maps
These are disgusting to make so it might take a while to complete -- currently working on a way to automate this process
"""

class Rewards:
    trainer0Arr = [[-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100],
                   [-100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-100],
                   [-100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-100]
                   [-100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-100],
                   [-100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-100],
                   [-100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-100],
                   [-100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-100],
                   [-100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-100],
                   [-100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-100],
                   [-100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-100],
                   [-100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-100],
                   [-100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-100],
                   [-100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-100],
                   [-100,0,0,0,0,0,0,0,0,0,0,80,85,90,95,90,85,80,75,-100],
                   [-100,35,40,45,50,55,60,65,70,75,80,85,90,95,100,95,90,85,80,-100],
                   [-100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-100],
                   [-100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-100],
                   [-100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-100],
                   [-100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-100],
                   [-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100]]
    
    
    
    def trainer0():
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