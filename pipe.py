import pygame as pg
from random import randint
class Pipe:
    def __init__(self,movespeed):
        self.img_up=pg.transform.scale_by(pg.image.load("pipeup.png").convert_alpha(),1.5)
        self.img_down=pg.transform.scale_by(pg.image.load("pipedown.png").convert_alpha(),1.5)
        self.rect_up=self.img_up.get_rect()
        self.rect_down=self.img_down.get_rect()
        self.pipe_distance=200
        self.rect_up.y=randint(250,520)
        self.rect_up.x=600
        self.rect_down.y=self.rect_up.y-self.pipe_distance-self.rect_up.height
        self.rect_down.x=600
        self.movespeed=movespeed
    def drawpipe(self,win):
        win.blit(self.img_up,self.rect_up)
        win.blit(self.img_down,self.rect_down)
    
    def update(self,dt):
        self.rect_up.x-=int(self.movespeed*dt)
        self.rect_down.x -= int(self.movespeed*dt)
        