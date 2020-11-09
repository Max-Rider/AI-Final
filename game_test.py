""" 
This file is meant to be used to test various parts of the final game in static, mostly blank world.
The world is created using Tiled and pyTMX.

Features to test here include initial player movement, player attacking, enemy AI movement, and enemy attacking.
"""
import sys
import pygame
from pygame.locals import *
from pytmx.util_pygame import load_pygame

# start main()
def main():
    #initial position for player
    playerXpos = 320 
    playerYpos = 500
    dXpos = 0
    dYpos = 0
    # Game loop
    running = True
    while running:
        screen.fill((255,255,255)) # Screen starts white before doing anything else
        keyPressed = pygame.key.get_pressed() # get key presses for movement
        #event loop -- looks for events like key presses or quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        #player movement
        playerXY = movePlayer(playerXpos, playerYpos, keyPressed)
        playerXpos = playerXY[0]
        playerYpos = playerXY[1]
        
        draw_map()
        #(playerXpos, playerYpos)
        player((playerXpos, playerYpos)) #draw player and update postion
        pygame.display.update() # Makes sure the screen is always being updated
# end main()

# start getLocProperties
# gets the properties of the given location on the map i.e. solid for walls so the player cant move through them
def getLocProperties(tmxdata, xPos, yPos):
    xTile = xPos // 16
    yTile = yPos // 16
    wallProp = tmxdata.get_tile_properties(xTile, yTile, 0)
    stairProp = tmxdata.get_tile_properties(xTile, yTile, 1)
    
    if wallProp is None: # set default properties if none are found
        wallProp = {"solid":0, "stairs":0}
        stairProp = {"solid":0, "stairs":0}
    return (wallProp, stairProp)
# end getLocProperties

# start player()
# loads player into bottom middle of the world
# NOTE player sprite is pretty small, maybe try and scale it up
def player(position):
    playerImg = pygame.image.load("tile PNGs\\blueWizard.png") # Load player sprite
    #print(position)
    screen.blit(playerImg, position) # draws player to screen
# end player()

# start movePlayer()
def movePlayer(xPos, yPos, keyPressed):
    if keyPressed[ord("a")]: # check what key was pressed
        westTile = getLocProperties(tmxdata, xPos-2, yPos+11) #find the tile next to the player and get its properties
        if westTile[0]['solid'] == 0: # if not solid keep moving, stop otherwise
            xPos += -1
    if keyPressed[ord("d")]:
        eastTile = getLocProperties(tmxdata, xPos+22, yPos+11)
        if eastTile[0]['solid'] == 0:
            xPos += 1
    if keyPressed[ord("w")]:
        northTile = getLocProperties(tmxdata, xPos, yPos-2)
        if northTile[0]['solid'] == 0:
            yPos += -1
    if keyPressed[ord("s")]:
        southTile = getLocProperties(tmxdata, xPos+2, yPos+22)
        if southTile[0]['solid'] == 0:
            yPos += 1
    return(xPos, yPos)
# end movePlayer()

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

# Initialize and run game
if __name__ == "__main__":
    width, height = 640, 640
    #init pygame
    pygame.init()
    #create screen (width, height)
    screenSize = (width, height)
    screen = pygame.display.set_mode(screenSize)
    # Window title
    pygame.display.set_caption("Untitled Rogue-Like game")
    tmxdata = load_pygame("rooms\\basic_room.tmx") # Load map from tmx file
    # To set window icon: 
    # icon = pygame.image.load("image.png")
    # pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    main()  
    pygame.quit()