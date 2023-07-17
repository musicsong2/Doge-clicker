#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame
import sys
import time
pygame.init()
pygame.font.init()
#350-400
width=350; 
height=400. 
pygame.display.set_caption("Doge clicker")
bg_color = (255, 255, 255)
screen = pygame.display.set_mode( (width, height ) )
screen.fill(bg_color)
pygame.display.flip()
doge = pygame.image.load("doge-2-white-2.jpg").convert()
x = 40
y = 10
screen.blit(doge ,  ( x,y))
pygame.display.flip()
black = (0, 0, 0)
font = pygame.font.Font('OpenSans-Bold.ttf', 32)
text = font.render('GeeksForGeeks', True, black)
def clear():
    screen.fill((0,0,0))
    screen.fill(bg_color)
    doge = pygame.image.load("doge-2-white-2.jpg").convert()
    x = 40
    y = 10
    screen.blit(doge ,  ( x,y))
    pygame.display.flip()
running = True
score = 0
textfont = pygame.font.SysFont("monospace", 50)
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            doge = pygame.image.load("doge-bruh.webp").convert()
            screen.blit(doge ,  ( 40,10))
            pygame.display.flip()
            time.sleep(0.1)
            if doge.get_rect().collidepoint(x, y):
                clear()
                (score) += 1 
                txtsurf = font.render(str((score)), True, black)
                screen.blit(txtsurf, (0, 0))
                pygame.display.update()
                pygame.display.flip()
                
           
                
                
    
                
           


# In[ ]:




