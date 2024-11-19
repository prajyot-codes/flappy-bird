import pygame as pg

class bird(pg.sprite.Sprite):
    def __init__(self):
        super(bird,self).__init__()
        self.img_list=[pg.transform.scale_by( pg.image.load("birdup.png").convert_alpha(),1.5),pg.transform.scale_by( pg.image.load("birddown.png").convert_alpha(),1.5)]
        self.image_index=0
        self.image=self.img_list[self.image_index]
        self.rect=self.image.get_rect(center=(100,100))
        self.y_velocity=0
        self.gravity=10
        self.flap_speed=350
        self.anim_counter=0
        self.update_on=False

 
    def update(self, dt):
        if self.update_on:
            self.playanimation()
            self.applygravity(dt)
            if self.rect.y<=0 and self.flap_speed==350:
                self.rect.y=0 
                self.flap_speed=0
                self.y_velocity=0
            elif self.rect.y>0 and self.flap_speed==0:
                self.flap_speed=350
        
    def applygravity(self,dt):
        self.y_velocity += self.gravity * dt
        self.rect.y += self.y_velocity
        
    def flap(self,dt):
        self.y_velocity -= self.flap_speed*dt
    
    def playanimation(self):
        if self.anim_counter==5:
            self.image=self.img_list[self.image_index]
            if self.image_index==0 : self.image_index=1
            else:
                self.image_index=0
            self.anim_counter=0
        self.anim_counter+=1
    
    
    def resetposition(self):
        self.rect.center=(100,100)
        self.y_velocity=0
        self.anim_counter=0