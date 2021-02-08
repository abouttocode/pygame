import pygame
import random
import sys
import os

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ALPHA = (0, 255, 0)
vihr = (0,45,65)
 

BOO_SIZE = random.randrange(25,50)
FPS=24

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720
world = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])




 
class Boo(pygame.sprite.Sprite):
    """
    Class to keep track of a boo's location and vector.
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.clicked = False

        self.images = []
        
        img = pygame.image.load("boo.png").convert()
        img.convert_alpha()
        img.set_colorkey(BLACK)
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        def update(self):
            if clicked:
                self.kill()
            

 
class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0

        self.images = []


        try:
            for i in range(0,23):
                while i < 10:
                    #print(os.path.join('cave_000'+ str(i) + '.png'))
                    img = pygame.image.load('cave_000'+ str(i) + '.png').convert()
                    img.convert_alpha()  # optimise alpha
                    img.set_colorkey(ALPHA)  # set alpha
                    self.images.append(img)
                    self.image = self.images[0]
                    self.rect = self.image.get_rect()
                    i +=1 
                img = pygame.image.load('cave_00'+ str(i) + '.png').convert()
                #print(os.path.join('cave_00'+ str(i) + '.png'))
                img.convert_alpha()  # optimise alpha
                img.set_colorkey(ALPHA)  # set alpha
                self.images.append(img)
                self.images.append(img)
                self.image = self.images[0]
                self.rect = self.image.get_rect()
        except(error):
            print(error)


    def update(self):
        self.x, self.y = pygame.mouse.get_pos()
        self.rect.center = (self.x+34,self.y+50)

'''
Setup
'''

backdrop = pygame.image.load('mappi3.jpg')
clock = pygame.time.Clock()
pygame.init()
backdropbox = world.get_rect()
font = pygame.font.SysFont('times new roman', 30)

main = True

player = Player()  # spawn player
player.rect.x = 0  # go to x
player.rect.y = 0  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)

 
def make_boo():
    """
    Function to make a new, random boo.
    """
    boo = Boo()
    # Starting position of the boo.
    # Take into account the boo size so we don't spawn on the edge.
    boo.x = random.randrange(BOO_SIZE, SCREEN_WIDTH - BOO_SIZE)
    boo.y = random.randrange(BOO_SIZE, SCREEN_HEIGHT - BOO_SIZE)
 
    # Speed and direction of rectangle
    #boo.change_x = random.randrange(-2, 3)
    #boo.change_y = random.randrange(-2, 3)
 
    return boo
 
 

"""
This is our main program.
"""

# Set the height and width of the screen
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Bouncing Boos")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

player = Player()   # spawn player
player.rect.x = 0   # go to x
player.rect.y = 0   # go to y
player_list = pygame.sprite.Group()
player_list.add(player)

boo_list = []

for i in range(5):
    boo = make_boo()
    boo_list.append(boo)
    i -= 1
score = 50

 
    # -------- Main Program Loop -----------
while main:

    scr = font.render('Score: '+ str(score), False, vihr)
    
    bxp = boo.x + BOO_SIZE
    bxm = boo.x - BOO_SIZE/2
    byp = boo.y + BOO_SIZE/2
    bym = boo.y - BOO_SIZE/2

    # --- Event Processing
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            # Space bar! Spawn a new boo.
            if event.key == pygame.K_SPACE:
                boo = make_boo()
                boo_list.append(boo)
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)
            print("pos individually", pos[0], pos[1])
            print("boo + pos individually", bxp, byp)
            print("boo - pos individually", bxm, bym)

            for boo in boo_list:
                if (pos[0] >= bxm and pos[0] <= bxp and 
                pos[1] >= boo.y-BOO_SIZE and pos[1] <= bxp):
                    score+=1
                    screen.blit(scr, (0,0))
                    print("print", boo_list)
                    print(boo)
                    

                    boo.kill()
                    boo_list.remove(boo)
                    print("boo has been killed")
                    print(boo.x, boo.y)
            print(score)

            
        elif event.type == pygame.MOUSEMOTION:
            player.update()

    # --- Logic
    for boo in boo_list:
        # Move the boo's center
        boo.x += boo.change_x
        boo.y += boo.change_y

        # Bounce the boo if needed
        if boo.y > SCREEN_HEIGHT - BOO_SIZE or boo.y < BOO_SIZE:
            boo.change_y *= -1
        if boo.x > SCREEN_WIDTH - BOO_SIZE or boo.x < BOO_SIZE:
            boo.change_x *= -1

    # --- Drawing
    # Set the screen background
    screen.blit(backdrop, backdropbox)
    player_list.draw(screen) # draw player
    
    

    # Draw the boos
    for boo in boo_list:
        pygame.draw.circle(screen, WHITE, [boo.x, boo.y], BOO_SIZE)

    # --- Wrap-up
    # Limit to 60 frames per second
    

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(FPS)
# Close everything down

pygame.quit()
sys.exit()
