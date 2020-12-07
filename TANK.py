import pygame
from pygame.draw import *
from random import randint
import numpy as np
import matplotlib as mp
pygame.init()
loose=0
WIDTH=1000
HEIGHT=600
BULLETS=[]

ENEMIES=[]

TIME=0
TIME_last_shoot=0
class Enemy:
    def __init__(self):
        self.type="usual"
        self.x=0
        self.y=0
        self.Vx=0
        self.Vy=5
        self.radius=10
        self.exist=1
        self.hp=10
        self.destroyer_Vy=7.5
    def move(self):
        if self.exist ==1:
                if self.type == "usual":
                    self.x+=self.Vx
                    self.y+=self.Vy
                    circle(screen, (BLUE), (round(self.x), round(self.y)), round(self.radius)) 
                if self.type == "destroyer":
                    self.y+=self.destroyer_Vy
                    rect(screen, (YELLOW), (self.x,self.y, self.radius, self.radius), )
    def check(self):
        if self.y<HEIGHT:
            del self

    

class Hero:
    def __init__(self):
        self.weapon="medium"
        self.V=8
        self.size=120
        self.x=0
        self.y=HEIGHT-self.size//2
        self.dx=0
        self.dy=0
        self.gun_width=20
        self.gunsize=100
        
    def move_right(self):
        self.x+=self.V
        
    def move_left(self):
        self.x-=self.V
        
    def draw(self):
        rect(screen, (183, 196, 200), (self.x,self.y, self.size, self.size//2), )
        line(screen, RED,(self.x+self.size//2,self.y),(self.x+self.size//2+self.dx,self.y+self.dy),round(self.gun_width))
        
    def SHOOT(self):
        a = Bullet()
        if hero.weapon == "small":
            a.type="small"
            a.Vx = self.dx / self.gunsize *a.speed*1.3
            a.Vy = -((a.speed*1.3) ** 2 - a.Vx ** 2) ** 0.5
            a.x = self.x+self.size//2+self.dx 
            a.y = self.y+self.dy
            BULLETS.append(a)
            a.radius=10
        if hero.weapon == "medium":
            a.type="medium"
            a.Vx = self.dx / self.gunsize *a.speed
            a.Vy = -(a.speed ** 2 - a.Vx ** 2) ** 0.5
            a.x = self.x+self.size//2+self.dx 
            a.y = self.y+self.dy
            BULLETS.append(a)
            a.radius=20
        if hero.weapon == "big":
            a.type="big"
            a.Vx = self.dx / self.gunsize *a.speed*0.5
            a.Vy = -((a.speed*0.5) ** 2 - a.Vx ** 2) ** 0.5
            a.x = self.x+self.size//2+self.dx 
            a.y = self.y+self.dy
            a.radius=40
            BULLETS.append(a)
        
        
class Bullet:
    
    def __init__(self):
        self.type="medium"
        self.x=0
        self.y=0
        self.speed = 30
        self.Vy=0
        self.Vx=0
        self.radius=10
        self.g=0.3
        self.exist=1
        
    def check(self):
        if self.x > WIDTH:
            del self


    
    def move(self):
        if self.exist == 1:
            self.x+=self.Vx
            self.y+=self.Vy
            circle(screen, (RED), (round(self.x), round(self.y)), self.radius)
            if self.type=="big" or self.type == "medium":
                self.Vy+=self.g
            
        
def spawner():
    random = randint(1,1000)
    if random >= 990:
        e=Enemy()
        e.hp=randint(1,10)+10
        e.radius=e.hp*2.5
        e.x=randint(1,round(WIDTH-2*e.radius))+e.radius
        e.y=-e.radius
        ENEMIES.append(e)
    if random <= 4:
        e=Enemy()
        e.type="destroyer"
        e.hp=100
        e.radius=50
        e.x=hero.x
        e.y=-e.radius
        ENEMIES.append(e)
        

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WIDTH=1000
HEIGHT=700
FPS = 30
loose=0
screen = pygame.display.set_mode(( WIDTH, HEIGHT))

random=0
del BULLETS[:]
del ENEMIES [:]

ball = Enemy()
hero = Hero()
#ball.move()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    TIME+=1
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            dx = event.pos[0]-(hero.x+hero.size//2)
            dy = event.pos[1]-hero.y
            if dy<0 :
                hero.dx = dx/np.abs(dx)*(hero.gunsize**2/(1+(dy/(dx+0.001))**2))**0.5
                hero.dy = (-1)*(hero.gunsize**2 - hero.dx**2)**0.5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if hero.weapon == "big":
                    if TIME - TIME_last_shoot>=60:
                        hero.SHOOT()
                        TIME_last_shoot=TIME
                else:
                    hero.SHOOT()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
                hero.weapon="medium"
                hero.gun_width=20
            if event.key == pygame.K_3:
                hero.weapon="big"
                hero.gun_width=40
            if event.key == pygame.K_1:
                hero.weapon="small"
                hero.gun_width=10
        
        
        if event.type == pygame.QUIT:
            finished = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        hero.move_left()
    if keys[pygame.K_SPACE]:
        if hero.weapon == "small":
            if TIME%3==0:
                hero.SHOOT()
                
    elif keys[pygame.K_RIGHT]:
        hero.move_right()
        
    ball.move()
    hero.draw()
    for b in BULLETS:
        b.move()
        if b.x > WIDTH:
            b.exist = 0
        if b.x < 0:
            b.exist = 0
        if b.y < 0:
            b.exist = 0
        if b.y > HEIGHT:
            b.exist = 0
        
            
        
    for e in ENEMIES:
        e.move()
        if e.exist == 1:
            if e.type == "destroyer":
                if e.y >= HEIGHT - hero.size//1.5:
                    if np.abs(e.x-(hero.x+hero.size//2))<=hero.size//2:
                        pygame.quit()
            if e.y > HEIGHT:
                if e.type =="usual":
                    e.exist=0
                    loose+=1
                 

                           

                        
    spawner()
    for b in BULLETS:
        for e in ENEMIES:
            if b.exist ==1:
                if e.exist == 1:
                    if (b.x-e.x)**2+(b.y-e.y)**2 <= (e.radius + b.radius)**2:
                        if b.type == "big":
                            e.exist = 0
                        else:
                            if b.exist==1:
                                if b.type == "small":
                                    e.hp-=4
                                if b.type == "medium":
                                    e.hp-=11
                                b.exist=0
                        if e.hp<=0:
                            e.exist=0
                
                
            

    spawner()
    pygame.display.update()
    screen.fill(BLACK)
    if loose >=5:
        pygame.quit()

pygame.quit()        
        
    
    
    