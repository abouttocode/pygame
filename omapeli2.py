import pygame  # pygame-module needs to be imported
import sys     # sys-module will be needed to exit the program
import random  # random-module will be needed for random numbers
from pygame.locals import * # pygame.locals gives us the constants of pygame
pygame.init()  # this function initializes pygame, mandatory in the beginning



class ukko(object):
    def __init__(self, screen_rect):
        self.screen_rect = screen_rect
        self.image = pygame.Surface([150,150]).convert()
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center=screen_rect.center)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
       

# the basic display-surface with suitable width and height
leveys = 1200 # 'leveys' variable contains the width of the display-surface
korkeus = 700 # 'korkeus' variable contains the height of the display-surface
# the next function will create the display-surface and stores it into 'screen'
screen = pygame.display.set_mode((leveys,korkeus))
# the caption of the display-window is set with the following function
pygame.display.set_caption("My game")


# the actual "building blocks" of the game, the Surface-objects
#hahmo = ukko(pygame.image.load("luugi2.png").convert_alpha())     # image-surface
hahmo = ukko(screen.get_rect()) 
pallo = pygame.image.load("boo.png").convert_alpha() # image-surface
# load()-function can load a picture which is on the same folder
# convert()-function converts it into the right pixel-format
# Surface((x,y)) creates empty surface, the default color is black
suorakaide = pygame.Surface((350,100))
# screen, hahmo, pallo and suorakaide are all Surface-objects


# the game also needs some RGB-colors (r,g,b), where 0<r,g,b<255
musta = (0,0,0)   # black color
puna = (255,0,0)  # red color
vihr = (0,255,0)  # green color
sini = (0,0,255)  # blue color
# Surface-objects can be filled with a color using fill()-function
suorakaide.fill(puna) # paints the suorakaide-Surface with color 'puna'


# Surface-objects can be added to the display-surface with blit()-function
screen.blit(pallo, (0,0))
#screen.blit(hahmo, (500,600))
screen.blit(suorakaide, (0,300))
# blit(Surface,(x,y)) adds the Surface into coordinates (x,y)=(left, top)


# the display-surface needs to be updated for the Surfaces to become visible
pygame.display.flip()
# pygame.display.update() would do the same


# Rect-object holds the coordinates of a Surface-object
# Rect-objects are needed to move Surfaces and check if they overlap
# Surface.get_rect() returns the Rect-object of the Surface
palloAlue = pallo.get_rect()
#hahmoAlue = hahmo.get_rect()
suoraAlue = suorakaide.get_rect()
# for example hahmoAlue = Rect(left,top,width,height) = (0,0,70,91)
# by default, get_rect() sets the left-top-corner to (0,0)
# hahmo and suorakaide were not blitted into (0,0)
# we need to cahnge the coordinates with dot-notation (left,right,top,bottom)
#hahmoAlue.left = 500
#hahmoAlue.top = 600
suoraAlue.left = 0
suoraAlue.top = 300


# nopeus contains the [x,y]-speed of the pallo-Surface in pixels (x,y>=1)
nopeus = [1,1]







######################################
######################################
######################################






# Event()-function will create an Event-object of a given type
# pygame.USEREVENT = 32847 is preferable type
# if you need more events, use pygame.USEREVENT+1, pygame.USEREVENT+2, etc.
pisteevent = pygame.event.Event(pygame.USEREVENT)


# the following timer will be used to create collectable balls
# set_timer() will put pisteevent into the event queue every 2 seconds
# pygame uses milliseconds for tracking time, the 2000 is milliseconds
pygame.time.set_timer(pisteevent,2000)


# the following lists are used for generating new collectable balls
palloLista = []
koordLista = []
nopeusLista = []


pisteet=0 # variable that keeps tracking the points
nopeus2 = [1,1] # the speed of the collectable balls
kello = pygame.time.Clock() # Clock-object is used to set the frame rate


# font-module can be used to create text into the game
# pygame.font.get_fonts() will give you all the available fonts
fonttiLoppu = pygame.font.SysFont('arial', 90)
fonttiPisteet = pygame.font.SysFont('cambria', 40)
# render()-function will create Surface-object from the text
loppuTeksti = fonttiLoppu.render('GAME OVER', True, sini)
pisteTeksti = fonttiPisteet.render('Pisteet: '+str(pisteet), False, vihr)




# You can also try to code the following properties:
# starting menu (easy/intermediate/hard-options)
# shooting bullets by the hahmo-surface
# winning the game and high scores table
# timer which forces you to win the game inside the given time
# game sounds when you die or collect a ball
# background music





######################################
######################################
######################################





# endless game-loop which runs until sys.exit() and/or pygame.quit()
while True:


    # check if the user has closed the display-window or pressed esc
    for event in pygame.event.get():  # all the events in the event queue
        if event.type == pygame.QUIT: # if the player closed the window
            pygame.quit() # the display-window closes
            sys.exit()    # the whole python program exits
        if event.type == KEYDOWN:     # if the player pressed down any key
            if event.key == K_ESCAPE: # if the key was esc
                pygame.quit() # the display-window closes
                sys.exit()    # the whole python program exits


        if event.type == pygame.USEREVENT:
            # pisteEvent was set to happen every 2 seconds by set_timer()
            olio=pygame.image.load("ball.png").convert()
            # we create new collectable ball and its Rect and speed
            palloLista.append(olio)
            koordLista.append(olio.get_rect())
            nopeusLista.append([nopeus2[0],nopeus2[1]])


        if event.type == pygame.MOUSEMOTION:
            hahmo.update()

    # pallo-Surface will be moved by nopeus=[1,1] in every iteration
    palloAlue.move_ip(nopeus)
    # move_ip([x,y]) changes the Rect-objects coordinates by x and y
    # move([x,y]) doesn't change the Rect-object, it creates new one:
    # palloAlue = palloAlue.move(nopeus)



    # pallo-Surface bounces from the edges of the display-surface
    if palloAlue.left < 0 or palloAlue.right > leveys:
    # if pallo is vertically outside
        nopeus[0] = -nopeus[0]
        # the x-direction of the speed will be changed with minus
    if palloAlue.top < 0 or palloAlue.bottom > korkeus:
    # if pallo is horizontally outside
        nopeus[1] = -nopeus[1]
        # the y-direction of the speed will be changed with minus



    # pallo-Surface bounces from the suorakaide-Surface
    if suoraAlue.colliderect(palloAlue):
    # colliderect()-function returns True if two Rect-objects overlap
        if suoraAlue.colliderect(palloAlue.move(-nopeus[0],0)):
        # if the pallo came from vertical direction
            nopeus[1] = -nopeus[1]
            # the y-direction of the speed will be changed with minus
        if suoraAlue.colliderect(palloAlue.move(0,nopeus[1])):
        # if the pallo came from horizontal direction
            nopeus[0] = -nopeus[0]
            # the x-direction of the speed will be changed with minus



    # you can move hahmo-Surface with left,right,up,down-keys
    painallukset = pygame.key.get_pressed()
    # get.pressed()-function gives a list of all the keys that are being pressed
    #if painallukset[K_LEFT]:       # if left-key is in this list
        #hahmoAlue.move_ip((-1,0))  # hahmo will be moved one pixel left
    #if painallukset[K_RIGHT]:
        #hahmoAlue.move_ip((1,0))
    #if painallukset[K_DOWN]:
        #hahmoAlue.move_ip((0,1))
    #if painallukset[K_UP]:
        #hahmoAlue.move_ip((0,-1))
    # from pygame-documentation you can find all the names for the keys





######################################
######################################
######################################




    # # hahmo-Surface will appear on the other side of the display-surface
    # if hahmoAlue.left > leveys: # if hahmo is over the right side
    #     hahmoAlue.right=0       # right-coordinate will go to 0
    # if hahmoAlue.right < 0:
    #     hahmoAlue.left = leveys
    # if hahmoAlue.top > korkeus:
    #     hahmoAlue.bottom = 0
    # if hahmoAlue.bottom < 0:
    #     hahmoAlue.top = korkeus


    # # hahmo-Surface will "bounce" from the edges of the display-surface
    # if hahmoAlue.left > leveys:          # if hahmo is over the right side
    #     hahmoAlue.left=hahmoAlue.left-70 # move 70 pixels left
    # if hahmoAlue.right < 0:
    #     hahmoAlue.right=hahmoAlue.right+70
    # if hahmoAlue.top > korkeus:
    #     hahmoAlue.top=hahmoAlue.top-70
    # if hahmoAlue.bottom < 0:
    #     hahmoAlue.bottom=hahmoAlue.bottom+70


    # # if hahmo-Surface overlaps pallo-Surface the game will end
    # if hahmoAlue.colliderect(palloAlue):
    #     screen.blit(loppuTeksti,(600, 350))
    #     pygame.display.update()
    #     # pygame.quit() would close the window, no time see the "game over"
    #     sys.exit()



    # move all the collectable balls
    for i in range(0,len(palloLista)):
        koordLista[i]=koordLista[i].move(nopeusLista[i])
        # make the collectable balls bounce from the edges of the window
        if koordLista[i].left < 0 or koordLista[i].right > leveys:
            nopeusLista[i][0] = -nopeusLista[i][0]
        if koordLista[i].top < 0 or koordLista[i].bottom > korkeus:
            nopeusLista[i][1] = -nopeusLista[i][1]




    # # hahmo-Surface gets randomly 50-100 points from collectable balls
    # j=0 # j is assistant variable, it tracks the number of deleted elements
    # for i in range(0,len(palloLista)):
    #     if hahmoAlue.colliderect(koordLista[i-j]):
    #     # if hahmo overlaps with a collectable ball
    #         palloLista.pop(i-j)
    #         koordLista.pop(i-j)
    #         nopeusLista.pop(i-j)
    #         j=j+1
    #         pisteet=pisteet+random.randint(50,100)
    #         # the ball will be deleted and you get randomly 50-100 points


    # Surface-object which shows the current points
    pisteTeksti = fonttiPisteet.render('Pisteet: '+str(pisteet), False, vihr)






######################################
######################################
######################################





    # clear the display-surface and draw all the Surfaces again
    screen.fill(musta) # without this, moving characters would have a "trace"
    screen.blit(pallo, palloAlue)
    #screen.blit(hahmo, hahmoAlue)
    screen.blit(suorakaide, suoraAlue)

    for i in range(0,len(palloLista)):
        screen.blit(palloLista[i], koordLista[i])
    screen.blit(pisteTeksti, (0,0)) # point-calculator


    # this is always needed to the end to update the display surface
    pygame.display.flip()


    # pygame.time.get_ticks() # this function gives the time in milliseconds from calling pygame.init()
    # pygame.time.wait(10) # this will pause the game for the given amount of milliseconds
    # kello.get_fps() # this will give the current frame rate of the game
    kello.tick(260) # this will set the frame rate
