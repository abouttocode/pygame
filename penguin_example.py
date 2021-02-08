#!/usr/bin/env python3
# by Seth Kenlon

# GPLv3
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from typing import Tuple

import pygame
import sys
import os

'''
Variables
'''

worldx = 960
worldy = 720
fps = 60  # frame rate
ani = 22 # animation cycles
world = pygame.display.set_mode([worldx, worldy])

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)

'''
Objects
'''


class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0 # move along X
        self.movey = 0 # move along Y
        #self.moveh = 0 # move along h
        self.frame = 0 # count frames
        self.images = []
        for i in range(1, 23):
            img = pygame.image.load(r'C:\Users\Alarik\OneDrive - Turun ammattikorkeakoulu\Documents\TurkuAMK\tuotekehitys\electric boogaluugi\images\cave_'+str(i)+".png").convert_alpha()
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
        glock = pygame.image.load(r'C:\Users\Alarik\OneDrive - Turun ammattikorkeakoulu\Documents\TurkuAMK\tuotekehitys\electric boogaluugi\images\glock.png).convert_alpha()

    def control(self,x,y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y
        #self.moveh += h

    def update(self):
        """
        Update sprite position
        """
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        #self.rect.h = self.rect.h + self.moveh
        # moving left
        if self.movex < 0:
            self.frame += 6
            if self.movex < 0:
                self.frame += 1
            if self.frame > 21*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]

        # moving right
        if self.movex > 0:
            self.frame += 6
            if self.frame > 21*ani:
                self.frame = 0
            if self.frame > 21*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]

        
'''
Setup
'''

backdrop = pygame.image.load(r'C:\Users\Alarik\OneDrive - Turun ammattikorkeakoulu\Documents\TurkuAMK\tuotekehitys\electric boogaluugi\images\mappi.png')
clock = pygame.time.Clock()
pygame.init()
backdropbox = world.get_rect()
main = True

player = Player()  # spawn player
player.rect.x = 0  # go to x
player.rect.y = 0
player.rect.w = 0 # worldy-pygame.image.load(r"C:\Users\Alarik\OneDrive - Turun ammattikorkeakoulu\Documents\TurkuAMK\tuotekehitys\electric boogaluugi\images\cave_0.png").get_rect().size[1]*2 # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10  # how many pixels to move

'''
Main Loop
'''

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT or event.key == ord('a'):
        #         print('left')
        #     if event.key == pygame.K_RIGHT or event.key == ord('d'):
        #         print('right')
        #     if event.key == pygame.K_UP or event.key == ord('w'):
        #         print('jump')

        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT or event.key == ord('a'):
        #         print('left stop')
        #     if event.key == pygame.K_RIGHT or event.key == ord('d'):
        #         print('right stop')
        #     if event.key == ord('q'):
        #         pygame.quit()
        #         sys.exit()
        #         main = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0,-steps)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0,steps)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0,steps)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0,-steps)
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False\
    
    player.update()
    world.blit(backdrop, backdropbox)
    player_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)

    

    