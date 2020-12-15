""" 
This file is meant to be used to test various parts of the final game in static, mostly blank world.
The world is created using Tiled and pyTMX.

Features to test here include initial player movement, player attacking, enemy AI movement, and enemy attacking.
"""
import sys
import random
import pygame
import math
from enemy import Enemy
from player import Player
from game import Game
from pygame.locals import *
from pytmx.util_pygame import load_pygame


width, height = 640, 640
#init pygame
pygame.init()
#create screen (width, height)
#Game().runGame() # UNCOMMENT THIS TO RUN WITH GAME CLASS INSTEAD -- CURRENTLY UNECESSARY
screenSize = (width, height)
screen = pygame.display.set_mode(screenSize)
# Window title
pygame.display.set_caption("Untitled Rogue-Like game")
tmxdata = load_pygame("rooms\\basic_room.tmx") # Load map from tmx file
fireBallList = [] # list of fire ball sprites
    
fireBallTimer = 0.1
# To set window icon: 
# icon = pygame.image.load("image.png")
# pygame.display.set_icon(icon)
clock = pygame.time.Clock()
dt = clock.tick(60)/1000 # dt = time since last tick in milliseconds
startTicks = pygame.time.get_ticks()

class fireBall:
    def __init__(self, playerX, playerY, mouseX, mouseY):
        self.x = playerX
        self.y = playerY
        self.speed = 2
        self.angle = math.atan2(mouseY-playerY, mouseX-playerX)
        self.xVel = math.cos(self.angle) * self.speed
        self.yVel = math.sin(self.angle) * self.speed
        self.fireBallTimer = 0.1
        
    def update(self, dt):
        self.x += int(self.xVel)
        self.y += int(self.yVel)
        
        # fbTimer = self.fireBallTimer - dt
        # if fbTimer <= 0:
        #     print("SHHOOOOTT HEERRRR")
        #     #wafbTimer = 0
        pygame.draw.circle(screen, (0,0,0), (self.x, self.y), 10)
        # fbTimer = 0.1



"""
Consider changing attack buttons to arrow keys instead of mouse
"""
def playerAttack(playerX, playerY, mouseX, mouseY, mousePressed):
    if mousePressed:
        fireBallList.append(fireBall(playerX, playerY, mouseX, mouseY))
    for fb in fireBallList:
        #pygame.time.wait(5)
        #print("before update")
        fb.update(dt)
        #print("after update")
        if fb.x < 20 or fb.y < 20 or fb.x > 610 or fb.y > 610: #delete orb if it leaves world bounds -- 
                                                               #need to make this so it deltes when it hits an enemy or a wall
            fireBallList.pop(fireBallList.index(fb))

"""
Using this for now but there is also a drawMap function in the Game class from game.py
"""
# start draw_map()
def draw_map():
    #tmxdata = load_pygame("rooms\\basic_room.tmx") # Load map from tmx file
    for layer in tmxdata:
        for tiles in layer.tiles():
            xPixelPos = tiles[0] * 16 #+ world_offset
            yPixelPos = tiles[1] * 16 #+ world_offset
            mapImg = tiles[2] #get img to draw from tmxdata
            screen.blit(mapImg, (xPixelPos, yPixelPos)) #draw map to screen
# end draw_map()

def redraw_game_window():
    win.blit(bg, (0, 0))
    win.blit(text, (520, 10))
    player.draw(win)
    enemy.draw(win)
    for fireball in fireballs
        fireball.draw(win)
    # Refresh the display and show the character
    pygame.display.update()


player = Player(250, 250)
enemy = Enemy(450, 300)
    
# Game loop
running = True
fireballCooldown = 0
fireballs = []
while running:
    screen.fill((255,255,255)) # Screen starts white before doing anything else
    keyPressed = pygame.key.get_pressed() # get key presses for movement
    mousePressed = pygame.mouse.get_pressed()[0]
    mouseX, mouseY = pygame.mouse.get_pos()
        
    if fireballCooldown > 0:
            fireballCooldown += 1
        if fireballCooldown > 3:
            fireballCooldown = 0    
        
        #event loop -- looks for events like key presses or quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
               
         
        for fireball in fireballs:
            if fireball.y - fireball.radius < enemy.hitbox[1] + enemy.hitbox[3] and fireball.y + fireball.radius > enemy.hitbox[1]:
                if fireball.x + fireball.radius > enemy.hitbox[0] and fireball.x - fireball.radius < enemy.hitbox[0] + enemy.hitbox[2]:
               
                    enemy.hit()
                
                    fireballs.pop(fireballs.index(fireball))
            if fireball.x < 750 and fireball.x > 0:
                fireball.x += fireball.vel
            else:
                fireballs.pop(fireballs.index(fireball))


         
        #player movement
    playerXY = player.move(playerXpos, playerYpos, keyPressed, tmxdata)
    playerXpos = playerXY[0]
    playerYpos = playerXY[1]
        
    draw_map() #draws the map to the screen
        #draw player and update postion
    player.draw((playerXpos, playerYpos), screen)
        
        
        
    playerAttack(playerXpos, playerYpos, mouseX, mouseY, mousePressed)
        
    redraw_game_window()
        
    
        
pygame.quit()

    
    
    
    
    
    
    
    
    
    
    
    
    


