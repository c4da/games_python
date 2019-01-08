# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 21:37:48 2017

@author: MCA

simple PONG game written with Python 3.6.

"""

import pygame, random
from pygame.locals import *
pygame.init()
random.seed()

pygame.display.set_caption("pong")

deviation = 0 
FPS = 200
fpsClock = pygame.time.Clock()

ball_color = (255, 255, 255)
paddle_color = (255, 255, 255)

screen = pygame.display.set_mode((400, 400))
#ball = pygame.draw.circle(screen, ball_color, (200, 200), 20, 0)

ball = pygame.image.load("ball.png")
sprite_ball = pygame.transform.scale(ball, (20, 20))
rect_ball = sprite_ball.get_rect()

sprite_paddle1 = pygame.image.load("paddle.png")
sprite_paddle2 = pygame.image.load("paddle.png")
rect_paddle1 = sprite_paddle1.get_rect()
rect_paddle2 = sprite_paddle2.get_rect()

rect_ball.left = 187.5
rect_ball.top = 187.5
rect_paddle1.left = 150
rect_paddle2.left = 150
rect_paddle1.top = 0
rect_paddle2.top = 375

h_speed = 0
v_speed = 0

while h_speed == 0:
    h_speed = random.randint(-1, 1)


while v_speed == 0:  
    v_speed = random.randint(-1, 1)
  
    
slower = 30

run = True
while run:
    
    slower -=1
    if slower == 0:
        slower = 8
        
       #horizontal movement for ball  
    if h_speed < 0:
        if (rect_ball.left + h_speed > 0):
            rect_ball.left += h_speed
        else:
            h_speed = -h_speed
    else:
        if (rect_ball.left + h_speed < 375):
                rect_ball.left += h_speed
        else:
                h_speed = -h_speed
                
        #vertical movement for ball
    if v_speed < 0:
        if (rect_ball.top + v_speed > 0):
            rect_ball.top += v_speed
        else:
            rect_ball.left = 200 - 12.5
            rect_ball.top = 200 - 12.5
    else:
        if (rect_ball.top + v_speed < 375):
                rect_ball.top += v_speed
        else:
            rect_ball.left = 200 - 12.5
            rect_ball.top = 200 - 12.5
                
                
        #ball collision with paddle1
    coll = False
    if ((rect_ball.left >= rect_paddle1.left) and \
(rect_ball.left <= rect_paddle1.left + rect_paddle1.width) and \
(rect_ball.top >= rect_paddle1.top) and \
(rect_ball.top <= rect_paddle1.top + rect_paddle1.height)):
        coll = True
    elif ((rect_paddle1.left >= rect_ball.left) and \
(rect_paddle1.left <= rect_ball.left + rect_ball.width) and \
(rect_paddle1.top >= rect_ball.top) and \
(rect_paddle1.top <= rect_ball.top + rect_ball.height)):
        coll = True
    #ball collision with paddle2
    if ((rect_ball.left >= rect_paddle2.left) and \
(rect_ball.left <= rect_paddle2.left + rect_paddle2.width) and \
(rect_ball.top + rect_ball.height >= rect_paddle2.top) and \
(rect_ball.top + rect_ball.height <= rect_paddle2.top + rect_paddle2.height)):
        coll = True
    elif ((rect_paddle2.left >= rect_ball.left) and \
(rect_paddle2.left <= rect_ball.left + rect_ball.width) and \
(rect_paddle2.top >= rect_ball.top) and \
(rect_paddle2.top <= rect_ball.top + rect_ball.height)):
        coll = True

    if coll:
        if ((rect_ball.top < 200) and (v_speed < 0)):
            v_speed = -v_speed
        elif ((rect_ball.top > 200) and (v_speed > 0)):
            v_speed = -v_speed
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        #LEFT is pressed
        if (rect_paddle1.left > 0) :
            rect_paddle1.left -= 5 

    if keys[pygame.K_RIGHT]:
        #LEFT is pressed
        if (rect_paddle1.right < 400) :
            rect_paddle1.left += 5
            
               
    
    if (rect_ball.top == 300) and (v_speed > 0):
        deviation = random.randint(-30, 30)

    if (rect_ball.top == 300) and (v_speed > 0):
        rect_paddle2.left = rect_ball.left - 55 + deviation
#    
#    if (paddle2_middle < rect_ball.left) and (rect_ball.top == 300) and v_speed == 1:
#        rect_paddle2.left = paddle2_middle - 10
#    if (paddle2_middle > rect_ball.left) and (rect_ball.top == 300) and v_speed == 1:
#        rect_paddle2.left = paddle2_middle + 10
# AI - sledovat polohu mice a pridavat nahodnou odchylku s kazdym hitem
#pridavat prekazky - pohyblive a destruktivni  


    screen.fill((0,0,0))

    screen.blit(sprite_paddle1, rect_paddle1)
    screen.blit(sprite_paddle2, rect_paddle2)
    screen.blit(sprite_ball, rect_ball)
    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
            
    fpsClock.tick(FPS)  
        
pygame.quit()        