import pygame
from pygame.draw import *
from random import randint
import numpy as np
import matplotlib as mp
pygame.init()

output = open('scores.txt', 'a')
db=0
BALLS =np.empty((20,9))
A=20000
a=0
name=" "
time=0
FPS = 30
WIDTH=1200
HEIGHT=800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
points=0
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)

Ux=5
Uy=5
COLORS = [ BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def spawn_black_hole():
    global bh_x, bh_y, bh_Ux,bh_Uy,bh_sz, bh_hp, bh_exist,A
    bh_exist=1
    bh_y = randint(0.4*WIDTH,0.6*HEIGHT)
    bh_Uy = randint(-2,2)
    bh_Ux = randint(2,4)
    bh_sz = randint(65,75)
    bh_x = -1*bh_sz
    bh_hp = 5+(bh_sz-65)//2
    circle(screen, (200,200,200), (round(bh_x), round(bh_y)), round(bh_sz) )
    A+=5000
    
def new_balls():
    
    '''0,1 -x,y
       2,3 -Ux,Uy
       4 - r
       5,6,7 - color(R,G,B)
       
    '''
    
    for i in range(20):
        color =COLORS[randint(0, 4)]
        BALLS[i,0] = randint(100, WIDTH)
        BALLS[i,1] = randint(100, HEIGHT)
        BALLS[i,2] = randint(-10, 10)
        BALLS[i,3] = randint(-10, 10)
        BALLS[i,4] = randint(10, 50)

        BALLS[i,8]=randint(0,100)
        if BALLS[i,8]>80:
            color=RED
            BALLS[i,8]=1
        else:
            BALLS[i,8]=0
        BALLS[i,5] = color[0]
        BALLS[i,6] = color[1]
        BALLS[i,7] = color[2]
        circle(screen, (BALLS[i,5],BALLS[i,6],BALLS[i,7]), (round(BALLS[i,0]), round(BALLS[i,1])), round(BALLS[i,4]))

def draw():
    '''0,1 -x,y
       2,3 -Ux,Uy
       4 - r
       5,6,7 - color(R,G,B)
    '''
    global bh_x, bh_y, bh_Ux,bh_Uy,bh_sz, bh_hp, bh_exist,points,db
    
    if bh_exist==1:
        circle(screen, (200,200,200), (round(bh_x), round(bh_y)), round(bh_sz) )
    for i in range(20):
        circle(screen, (BALLS[i,5],BALLS[i,6],BALLS[i,7]), (round(BALLS[i,0]), round(BALLS[i,1])), round(BALLS[i,4]) )

def move_bh():
    '''0,1 -x,y
       2,3 -Ux,Uy
       4 - r
       5,6,7 - color(R,G,B)
    '''
    global bh_x, bh_y, bh_Ux,bh_Uy,bh_sz, bh_hp, bh_exist,points,db
    
    if bh_exist==1:
        bh_x+=bh_Ux
        bh_y+=bh_Uy
        
    if bh_hp <= 0:
        if bh_exist==1:
            bh_exist=0
            points+=(bh_sz-65)//2+5
            print(points)

    if bh_x >= WIDTH+bh_sz:
        bh_exist=0
        
    if bh_y >=HEIGHT+bh_sz:
        bh_exist=0

    if bh_y <= -bh_sz:
        bh_exist=0
    

def move_ball():
    
    '''0,1 -x,y
       2,3 -Ux,Uy
       4 - r
       5,6,7 - color(R,G,B)
    '''
    global bh_x, bh_y, bh_Ux,bh_Uy,bh_sz, bh_hp, bh_exist,points,db
    
    for i in range(20):
        if BALLS[i,0]-BALLS[i,4] <= 1:
            BALLS[i,2]=np.abs(BALLS[i,2])
            
        if BALLS[i,0]+BALLS[i,4] >= WIDTH - 1:
            BALLS[i,2]=-1*np.abs(BALLS[i,2])
        
        if BALLS[i,1]-BALLS[i,4] <= 1:
            BALLS[i,3]=abs(BALLS[i,3])
            
        if BALLS[i,1]+BALLS[i,4] >= HEIGHT - 1:
            BALLS[i,3]=-1*np.abs(BALLS[i,3])

            
        if bh_exist==1:
            a=(bh_sz/65)**2*A/( (BALLS[i,0]-bh_x)**2+(BALLS[i,1]-bh_y) **2)
            BALLS[i,2]+=a/(((bh_y-BALLS[i,1])/(bh_x-BALLS[i,0]))**2+1)*(bh_x-BALLS[i,0])/np.abs(bh_x-BALLS[i,0])
            BALLS[i,3]+=a/(((bh_y-BALLS[i,1])/(bh_x-BALLS[i,0]))**2+1)*np.abs((bh_y-BALLS[i,1])/(bh_x-BALLS[i,0]))*(bh_y-BALLS[i,1])/np.abs(bh_y-BALLS[i,1])
            if (BALLS[i,0]-bh_x)**2+(BALLS[i,1]-bh_y) **2 <= (bh_sz+BALLS[i,4])**2:
                bh_sz=np.sqrt(BALLS[i,4]**2/3+bh_sz**2)
                BALLS[i,4]=0
                BALLS[i,0]=-1000000
                BALLS[i,1]=-1000000
                BALLS[i,2]=0
                BALLS[i,3]=0
                db+=1        
        BALLS[i,0]+=BALLS[i,2]
        BALLS[i,1]+=BALLS[i,3]



    
        
pygame.display.update()
clock = pygame.time.Clock()
finished = False
spawn_black_hole()
new_balls()
while not finished:
    clock.tick(FPS)
    time+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(20):
                if np.sqrt((event.pos[0]-BALLS[i,0])**2+(event.pos[1]-BALLS[i,1])**2)<BALLS[i,4]:
                    if BALLS[i,8]==0 :
                        points+=round(100/BALLS[i,4])
                        print(points)
                    else:
                        points-=round(100/BALLS[i,4])
                        print(points)
            if bh_exist==1:
                if np.sqrt((event.pos[0]-bh_x)**2+(event.pos[1]-bh_y)**2)<bh_sz:
                    bh_hp-=1
    if bh_exist==0:
        if time%(FPS*5) == FPS*3:
            spawn_black_hole()
    if db>= 20:
        print("score:",points)
        name=input()
        print('\n',name, ":",points, file=output)
        output.close()
        pygame.quit()
    
    move_bh()
    move_ball()
    draw()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()