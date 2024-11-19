import pygame as pg  # type: ignore
import sys, time
from bird import bird

pg.init()

class Game():
    def __init__(self):
        self.width = 600
        self.height = 768
        self.scalefactor = 1.5
        self.win = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()
        self.move_speed = 250
        self.bird = bird(self.scalefactor)
        self.setupBgandGround()
        self.gameloop()

    def gameloop(self):
        last_time = time.time()
        while True:
            new_time = time.time()
            dt = new_time - last_time
            last_time = new_time
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            self.updateeverything(dt)
            self.draweverything()
            pg.display.update()
            self.clock.tick(60)

    def setupBgandGround(self):
        self.back_img = pg.transform.scale(pg.image.load("back.png").convert(), (int(self.width * self.scalefactor), int(self.height * self.scalefactor)))
        self.ground_img = pg.transform.scale(pg.image.load("ground.png").convert(), (int(self.width * self.scalefactor), int(self.height * 0.2 * self.scalefactor)))
        
        self.ground1_rect = self.ground_img.get_rect()
        self.ground2_rect = self.ground_img.get_rect()
        self.ground1_rect.x = 0
        self.ground2_rect.x = self.ground1_rect.width
        self.ground1_rect.y = self.height - self.ground1_rect.height
        self.ground2_rect.y = self.height - self.ground2_rect.height

    def draweverything(self):
        self.win.blit(self.back_img, (0, -300))
        self.win.blit(self.ground_img, self.ground1_rect)
        self.win.blit(self.ground_img, self.ground2_rect)
        self.win.blit(self.bird.image, self.bird.rect)

    def updateeverything(self, dt):
        self.ground1_rect.x -= self.move_speed * dt
        self.ground2_rect.x -= self.move_speed * dt
        if self.ground1_rect.right < 0:
            self.ground1_rect.x = self.ground2_rect.right
        if self.ground2_rect.right < 0:
            self.ground2_rect.x = self.ground1_rect.right

# Create an instance of the game class
game_instance = Game()
