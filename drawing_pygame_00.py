#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 09:56:49 2019

@author: MCA
"""

import pygame as pg
import sys
import math 

from pygame.locals import *
vec = pg.math.Vector2



BLACK = (0,0,0)
WHITE = (255,255,255)

BGCOLOR = WHITE


FPS = 120
WIDTH = 600
HEIGHT = 300

class WorkPlace:
    def __init__(self):
        pg.init()       
        self.screen = pg.display.set_mode((WIDTH,HEIGHT),0,32)
        pg.display.set_caption("animation of a vector")
        self.clock = pg.time.Clock()
        self.running = True
        self.screen.fill(BGCOLOR)
    
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.vector = Vector(self)
        self.all_sprites.add(self.vector) 
    
    
    def draw(self):
        self.all_sprites.update()
        self.all_sprites.draw(self.screen)
        pg.display.flip()
    
    
    def run(self):
        self.clock.tick(FPS)
        self.events()
        self.draw()
        
    
    def events(self):
        for event in pg.event.get():
                    # check for closing window
                if event.type == pg.QUIT:
                 if self.running:
                    self.running = False
                 pg.quit()
                 sys.exit()
                 
                if event.type == pg.KEYDOWN:
                 if event.key == pg.K_UP:
                  pass
                 if event.key == ord('q'):
                    if self.running:
                     self.running = False
                     
class Vector(pg.sprite.Sprite):
    
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        
        self.game = game
        self.image = pg.Surface((1,1))
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        
    def follow (self):
        mouse_pos = pg.mouse.get_pos()
        self.rect.midbottom = mouse_pos
        
    def update(self):
        self.follow()
#        self.vel = vec(0,0)
#        keys = pg.key.get_pressed()
#        if keys[pg.K_LEFT]:
#            self.vel.x = -1 
#        if keys[pg.K_RIGHT]:
#            self.vel.x = 1
#        if keys[pg.K_UP]:
#            self.vel.y = -1 
#        if keys[pg.K_DOWN]:
#            self.vel.y = 1
            

#        self.pos += self.vel
#        self.rect.midbottom = self.pos
        
        
if __name__ == "__main__":
    
    wp = WorkPlace()
    wp.new()
    
    while wp.running:
        
        wp.run()
    
    pg.quit()
    wp.running = False
    sys.exit()
