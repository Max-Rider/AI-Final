"""
File for enemy functions (AI functionality for movement and attacks and things)
"""

import pygame
from pygame.locals import *
from pytmx.util_pygame import load_pygame

    
    
class Enemy:

    
    
    
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

    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            
            
        # Drawing the health bar of the enemy.
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))

        # Substract from the health bar width each time enemy is hit
            pygame.draw.rect(win, (0,255,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            
        # Creating a hitbox around the character.
            self.hitbox = (self.x + 15, self.y + 10, 29, 52)
        
        def hit(self):
            if self.health > 0:
                self.health -= 1
            else:
                self.visible = False
            print('Enemy hit')

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    # NEW METHOD
    def hit(self):  # This will display when the enemy is hit
        print('hit')
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        