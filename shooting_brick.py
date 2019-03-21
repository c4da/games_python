# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 13:00:19 2019

@author: MCA
"""

import sys, os
import pygame as pg

# PyGame Constants
from pygame.locals import *
#from pygame.color import THECOLORS
from math import radians, cos, sin
# PyGame gui
#from pgu import gui

# Import the vector class from a local module (in this same directory)
#from vec2d_jdm import Vec2D

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 140, 140)
BGCOLOR = LIGHTBLUE
vec = pg.math.Vector2 

def handleEvents(events, _angle, _release):
    for event in events:
        if event.type == QUIT:
            pg.quit()
            sys.exit(0)
        
        elif event.type == KEYDOWN and _release == False:
            if event.key == K_UP:
              _angle += 5
            if event.key == K_DOWN:
              _angle -= 5
    
            if event.key == K_SPACE:
                print("shoot")
                _release = True   
                
            if event.key == pg.K_q or event.key == K_ESCAPE:
                pg.quit()
                sys.exit(0)
                
    return _angle, _release

class Ball(pg.sprite.Sprite):
    
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30,30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = 100, 380
        
        self.pos = vec(100, 380)
        self.vel = vec(0,0)
        self.acc = vec(0, 0.8)
        self.f = 0.8

        
    def initVel(self,v0, angle):
#        print angle
        angle = radians(abs(angle))
        self.vel.x = v0*cos(angle)
        self.vel.y = -v0*sin(angle)
#        print v0, self.vel
        
    def update(self, angle, FPSadjust):

        self.pos += self.vel + 0.5*self.acc*FPSadjust
        self.rect.center = self.pos

        collision = pg.sprite.spritecollideany(self, floorGRP)
        if collision:
            self.vel[0] = self.vel[0]*self.f
            self.vel[1] = self.vel[1]*(-1)*self.f

            if self.pos.y > 380:
                self.pos.y = 380
                if self.vel[0] < 0.5:
                    self.pos[1] = 380
                    self.acc[1]= 0
                    self.vel = vec(0,0)
                                
        else:
            self.vel += self.acc

        
class trace(pg.sprite.Sprite):
    def __init__(self, actPos):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((10,10))
        self.image.fill(GRAY)
        self.rect = self.image.get_rect()
        self.rect.center = (actPos[0], actPos[1])

    
class Floor(pg.sprite.Sprite):
    def __init__(self, posX, posY):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((1400,1))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = posX, posY       
        
        

class Line(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((140, 32))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pg.draw.polygon(self.image, pg.Color('dodgerblue'), ((100, 0), (132, 16), (100, 32)))
        pg.draw.line(self.image, pg.Color('dodgerblue'), (0, 16), (100, 16), 5)
        self.org_image = self.image.copy()
        self.rect = self.image.get_rect(center=(170, 380))
        self.pos = pg.math.Vector2(self.rect.center)
        
    def rotate(self, img, pos, angle):
        w, h = img.get_size()
        img2 = pg.Surface((w*4, h*4), pg.SRCALPHA)
        img2.blit(img, (w-pos[0], h-pos[1]))
        return pg.transform.rotozoom(img2, angle, 1)
    
    def update(self, angle, FPSadjust):
        
        self.image = self.rotate(self.org_image, (-140, -16), angle)
        self.rect = self.image.get_rect()
        self.rect.center = (100,380)
        
             
pg.init()

baseFPS = 60.
FPS = 60.

FPSadjust = float(FPS/baseFPS)

clock = pg.time.Clock() 


windowSizeL = 1400
windowSizeH = 480
window = pg.display.set_mode((windowSizeL, windowSizeH))

pg.display.set_caption("moving ball")
 
screen = pg.display.get_surface()
screen.fill((255,255,255))

point = Ball()
line = Line()
floor = Floor(700, 380+15)


allSprites = pg.sprite.Group()
allSprites.add(point)
allSprites.add(line)
allSprites.add(floor)

floorGRP = pg.sprite.Group()
floorGRP.add(floor)
arrow = pg.sprite.Group()
arrow.add(line)

traceGRP = pg.sprite.Group()

move = 0
angle = 0
release = False
basePosition = [100, windowSizeH-100]
dt = 0.
dt_ms = 0.

while True:
    screen.fill((255,255,255))
    events = pg.event.get()
    angle, release = handleEvents(events, angle, release)

    
    if release == False:

        angle_ = radians(angle)
        ballPosX = basePosition[0]
        ballPosY = basePosition[1]
        allSprites.draw(screen)
        arrow.update(angle,FPSadjust)
        init = True
        
    if release == True:
        if init == True:
            v0 = 20
            point.initVel(v0, angle)
            init = False
        
        allSprites.update(angle, FPSadjust)
        allSprites.draw(screen)
        tracePoint = trace(point.pos)
        traceGRP.add(tracePoint) 
        traceGRP.draw(screen)        
        
    dt = clock.tick(FPS)
    dt_ms = (clock.get_time())
#    print dt_ms
    pg.display.flip()


