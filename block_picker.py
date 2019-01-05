# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 22:21:57 2017

@author: MCA

Simple block picking with mouse, with pygame.
Code could be used as a base for space invaders kind of game.
Python 3.6.
"""

import pygame
import random #using for random block positions

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Block(pygame.sprite.Sprite):
    
 """
 class inherits from pygame.sprite
 """
    
 def __init__(self, color, width, height):
    """ 
    Constructor. Pass in the color of the block,
    and its x and y position. 
    """
 
    # init the parent class (Sprite) constructor
    super().__init__()
    
    # Set the background color and set it to be white
    self.image = pygame.Surface([width, height])
    self.image.fill(color)
    self.image.set_colorkey(WHITE)    
    # Fetch the rectangle object that has the dimensions of the image
    # Update the position of this object by setting the values
    # of rect.x and rect.y
    self.rect = self.image.get_rect() 
    
 def reset_pos(self):
    """ 
    Reset position to the top of the screen, at a random x location.
    Called by update() or the main program loop if there is a collision.
    """
    self.rect.y = random.randrange(-300, -20)
    self.rect.x = random.randrange(0, screen_width)
    
 def update(self):
    """ Called each frame. """
 
    # Move block down one pixel
    self.rect.y += 1
    
    if self.rect.y > screen_height:
       self.reset_pos()
    
pygame.init()

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
# This is a list of 'sprites.' Each block in the program is
# added to this list.
# The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
#block_list je list kazdeho bloku s kterym muze hrac kolidovat 
# This is a list of every sprite.
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

for i in range(50):
    # This represents a block
    # generates 50 blocks
    block = Block(BLACK, 20, 15)
    print(block)
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
    
# Create a RED player block
player = Block(RED, 20, 15)
all_sprites_list.add(player)

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # Clear the screen
    screen.fill(WHITE)
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()
 
    # Fetch the x and y out of the list,
    # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    # See if the player block has collided with anything. - if True block is deleted
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
    # Check the list of collisions. 
    for block in blocks_hit_list:
        score +=1
        print(score)
        block.reset_pos()
        
    block_list.update()
    # Draw all the spites
    all_sprites_list.draw(screen)
# Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
pygame.quit()