# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 22:46:07 2018

@author: MCA

Simple stars animation with Py36 and Pygame
"""

import pygame
import sys
from random import randrange, choice

BLACK = 0, 0, 0 #barva je reprezentovana jako RGB tuple
WHITE = 255, 255, 255

MAX_STARS = 250
STAR_SPEED = 2


class Stars:
 def __init__(self, MAX_STARS, STAR_SPEED):

  pygame.init()
  
  self.screen = pygame.display.set_mode((640, 480))
  pygame.display.set_caption("this is a test")
  self.clock = pygame.time.Clock() #objekt clock ovlada FPS aplikace
  self.MAX_STARS = MAX_STARS
  self.STAR_SPEED = STAR_SPEED
  
  self.init_stars()
     
#stars coords generation
 def init_stars(self):
    self.stars = []
    for i in range(self.MAX_STARS):
     # A star is represented as a list with this format: [X,Y]
     star = [randrange(0, self.screen.get_width() - 1), 
             randrange(0,self.screen.get_height() - 1),
             choice([1,2,3])]
     self.stars.append(star) #a star has a coordinate

 def move_and_draw_stars(self):
  """ Move and draw the stars in the given screen """

  for star in self.stars:
      #ycoord += zcoord
    star[1] += star[2]
    # If the star hit the bottom border then we reposition
    # it in the top of the screen with a random X coordinate.
    if star[1] >= self.screen.get_height():
      star[1] = 0
      star[0] = randrange(0,639)
      star[2] = choice([1, 2, 3])
      
       
    # Adjust the star color acording to the speed.
    # The slower the star, the darker should be its color.
    if star[2] == 1:
      color = (100,100,100)
    elif star[2] == 2:
      color = (190,190,190)
    elif star[2] == 3:
      color = (255,255,255)
 
    # Draw the star as a rectangle.
    # The star size is proportional to its speed.
    self.screen.fill(color,(star[0],star[1],star[2],star[2]))

    
 def run(self):
  box_x = 300
  box_dir = 3
  
  while True:
    self.clock.tick(50) #uzavreni FPS na 50 FPS
    
    for event in pygame.event.get():
        #smycka ceka zda uzivatel ukoncil aplikaci krizkem tzv.QUIT EVENT
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #clear the screen
    self.screen.fill(BLACK)

    box_x += box_dir
    if box_x >= 620:
        box_x = 620
        box_dir = -3
    elif box_x <= 0:
        box_x = 0
        box_dir = 3
    
    #update screen
    pygame.draw.rect(self.screen, WHITE, (box_x, 200, 20, 20))
    self.move_and_draw_stars()
    pygame.display.flip()
    

if __name__ == "__main__":
    Stars(250, 2).run()
