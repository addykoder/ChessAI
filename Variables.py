import pygame

# playing settings
# this variable tells that whom against do you want to play
# rnd ( random ), ai ( in development ) or mp(multiplayer)
Play_Against = 'mp'

#   This class has all the variables used in the full project you can edit these
#   variables as per your need to see changes in your game

board = []  # this board will be created with 0s and pygame surface objects
activatedBoard = []  # this will modified often in between the game to notify possible moves
activatedBlock = 0
# window
display = 0
dimension = 720  # 512 is the optimum size if try to increase the size the pieces will remain of the same size
# as this is a chess board so both height and width will remain same
size = int(dimension / 8)  # This is the size of a block

# Main flow
playing = False  # this variable will be true after the initializePygame method is been called
clock = 0  # This clock variable will be initialized later with pygame.time.clock()

# Colors
bgColor = (240, 240, 240)
darkBlock = (170, 40, 40)
lightBlock = (128, 234, 255)
# this notifier is not a rgb triplet
# this is a pygame surface object which we will blit later
notifierColor = pygame.Surface((size, size), pygame.SRCALPHA)  # per-pixel alpha
notifierColor.fill((0, 255, 0, 170))

# Chance
chance = 'w'
nextChance = 'b'
player = 'w'

# elevated piece moving
piece = 0
Fromx = 0
Fromy = 0

showNotifier = False

# clicked timing
down = 0
up = 0

# recursion limits

rec_1 = 10
