import pygame as pg
import sys
import time
import random
import pygame_menu
from pygame.locals import *


pg.init()
pg.mixer.pre_init(44100, -16, 2, 2048)

#set screen and load sprites taht are used
screen = pg.display.set_mode((1920 ,1080))
pg.display.set_caption("Luugi's adventure 2 Electric boogaluugi")
tausta = pg.image.load("mappi3.jpg").convert_alpha()
fontti = pg.font.SysFont('times new roman', 30)
boo = pg.image.load("boo.png").convert_alpha()

#menu
def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    pass

menu = pygame_menu.Menu(300, 400, 'Welcome',
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add_text_input('Name :', default='Sebastian Vettell')
menu.add_selector('Difficulty :', [('Ezpez', 1), ('Impossibru', 2)], onchange=set_difficulty)
menu.add_button('Play', start_the_game)
menu.add_button('Quit', pygame_menu.events.EXIT)



class Char(pg.sprite.Sprite):
    def __init__(self):
        #self.screen_rect = screen_rect
        self.image = pg.image.load("luugi2.png").convert_alpha()
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.center = pg.mouse.get_pos()

    def collision(self, sprite):
        return self.rect.colliderect(sprite)

vihr = (172,210,47)
aika = (time.time())
scr = 0
fps = 60
luug = Char()
clock = pg.time.Clock()
done = False
screen.blit(boo, (0,0))
boorect = boo.get_rect()
nopeus = [1,1]
boolist = []
cordlist = []
speedlist = []
nopeus2 = [5,5]

boorect.move_ip(nopeus)


def main():

    
    

    menu.mainloop(screen)
    while not done:
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.MOUSEMOTION:
                luug.update()



        boorect.move_ip(nopeus)

        if boorect.left < 0 or boorect.right > 1920:
            nopeus[0] = -nopeus[0]
        if boorect.top < 0 or boorect.bottom > 1080:
            nopeus[1] = -nopeus[1]

        screen.blit(tausta, (0,0))

        screen.blit(boo, boorect)



        #for i in range(0,len(boolist)):
        if luug.collision(boorect):
            scr = scr + 1

        #     sys.exit()

        score = fontti.render('Score: '+ str(scr), False, vihr)
        timer = fontti.render('Time survived: '+str(int(time.time() - aika)), False, vihr)

        painallukset = pg.key.get_pressed()
        if painallukset[K_UP]:
            boolist.append(boo)
            cordlist.append(boo.get_rect())
            speedlist.append([nopeus2[0],nopeus2[1]])

        for i in range(0,len(boolist)):
            cordlist[i]=cordlist[i].move(speedlist[i])
            if cordlist[i].left < 0 or cordlist[i].right > 1920:
                speedlist[i][0] = -speedlist[i][0]
            if cordlist[i].top < 0 or cordlist[i].bottom > 1080:
                speedlist[i][1] = -speedlist[i][1]    

        for i in range(0,len(boolist)):
            screen.blit(boolist[i], (random.randint(1, 1920),random.randint(1, 1080)))
            
        screen.blit(timer, (1690,0))
        screen.blit(score, (0,0))
        luug.draw(screen)           
        pg.display.update()