import pygame as pg  
from pygame import K_RETURN, K_s, K_w, K_UP, K_DOWN
import sys,time
from bird import bird
from pipe import Pipe

pg.init()

class game():
    def __init__(self):
        self.width = 600
        self.height = 768
        self.scalefactor=1.5
        self.is_enter_pressed=False
        self.win = pg.display.set_mode((self.width, self.height))
        self.clock=pg.time.Clock()
        self.move_speed=350
        self.start_monitering=False
        self.score=0
        self.font=pg.font.Font("font.ttf",24)
        self.score_text=self.font.render("Score: 0",True,(255,255,255))
        self.score_rect=self.score_text.get_rect(center=(150,30))
        
        self.restart_text=self.font.render("Restart",True,(255,0,0))
        self.restart_rect=self.restart_text.get_rect(center=(300,650))
        
        self.data_text=self.font.render("HighScore: ",True,(255,0,0))
        self.data_rect=self.data_text.get_rect(center=(150,20))
        self.pipes=[]
        self.pipe_generate_counter=71
        self.is_game_started=True
        self.bird=bird()
        self.setupBgandGround()
        self.gameloop()


    def gameloop(self):
        last_time=time.time()
        while True:
            new_time=time.time()
            dt=new_time-last_time
            last_time=new_time
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type==pg.KEYDOWN and self.is_game_started: 
                    if event.key==K_RETURN: 
                        self.is_enter_pressed=True
                        self.bird.update_on=True
                    if event.key==pg.K_SPACE and self.is_enter_pressed:
                        self.bird.flap(dt)
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.restart_rect.collidepoint(pg.mouse.get_pos()):
                        self.restartgame()
            self.updateeverything(dt)
            self.checkcollions()
            self.checkscore()
            # self.diplay_highscore()
            self.draweverything()
            pg.display.update()
            self.clock.tick(60)
            
    def checkscore(self):
        if len(self.pipes)>0:
            if (self.bird.rect.left>self.pipes[0].rect_down.left and
            self.bird.rect.right<self.pipes[0].rect_down.right and not self.start_monitering):
                self.start_monitering=True
            if self.bird.rect.left > self.pipes[0].rect_down.right and self.start_monitering:
                self.start_monitering=False
                self.score+=1    
        self.score_text=self.font.render(f"Score: {self.score}",True,(255,255,255))
    
    # def diplay_highscore(self):
    #     with open("score.txt") as f:
    #         data=int(f.read())
    #         if(self.score<=data):
    #             pass
    #         else:
    #             with open("score.txt","w") as f:
    #                 f.write(self.score)
    #                 f.close()
    #     self.data_text=self.font.render(f" HIScore: {data}",True,(255,255,255))
            
                
    def setupBgandGround(self):
        self.back_img = pg.transform.scale_by( pg.image.load("back.png").convert(),self.scalefactor)
        self.ground1_img=pg.transform.scale_by( pg.image.load("ground.png").convert(),self.scalefactor)
        self.ground2_img=pg.transform.scale_by( pg.image.load("ground.png").convert(),self.scalefactor)

        self.ground1_rect=self.ground1_img.get_rect()
        self.ground2_rect=self.ground2_img.get_rect()
        self.ground1_rect.x=0
        self.ground2_rect.x=self.ground2_rect.right
        self.ground1_rect.y=568
        self.ground2_rect.y=568

    def restartgame(self):
        self.score=0
        self.score_text=self.font.render("Score: 0",True,(255,255,255))
        self.is_enter_pressed=False
        self.is_game_started=True  
        self.bird.resetposition()
        self.pipes.clear()
        self.pipe_generate_counter=71
        self.bird.update_on=False

    def draweverything(self):
        self.win.blit(self.back_img, (0, -300))
        for pipe in self.pipes:
            pipe.drawpipe(self.win)
        self.win.blit(self.ground1_img, self.ground1_rect)
        self.win.blit(self.ground2_img, self.ground2_rect)
        self.win.blit(self.bird.image, self.bird.rect)
        self.win.blit(self.score_text,self.score_rect)
        if not self.is_game_started:
            self.win.blit(self.restart_text,self.restart_rect)

    def checkcollions(self):
        if len(self.pipes):
            if (self.bird.rect.bottom>568):
                self.bird.update_on=False
                self.is_enter_pressed=False
                self.is_game_started=False
            if(self.bird.rect.colliderect(self.pipes[0].rect_down) or 
                self.bird.rect.colliderect(self.pipes[0].rect_up)):
                self.is_enter_pressed=False
                self.is_game_started=False
                    
        
        
    def updateeverything(self,dt):
        if self.is_enter_pressed:
            #moving the ground
            
            self.ground1_rect.x -=self.move_speed*dt
            self.ground2_rect.x -=self.move_speed*dt
            if self.ground1_rect.right<0:
                self.ground1_rect.x=self.ground2_rect.right
            if self.ground2_rect.right<0:
                self.ground2_rect.x=self.ground1_rect.right
                
                # generating pipes
            if self.pipe_generate_counter>70:   
                self.pipes.append(Pipe(self.move_speed))
                self.pipe_generate_counter=0
                # print("pipe created")
            self.pipe_generate_counter+=1
            
            
            # moving pipes
            for pipe in self.pipes:
                pipe.update(dt)
                
              #removing pipe  
            if len(self.pipes)!=0:
                if self.pipes[0].rect_up.right<0:
                    self.pipes.pop(0)
                    # print("pipe removed")
                #moving the bird
                
        self.bird.update(dt)

# Create an instance of the game class
game = game()


