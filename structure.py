import pygame, sys
from actor import *

level_map = [
[3,3,3,0,0,0,0,0,0,0,0,0,0,0,1,1,3,3,0,0,0,0,0,0,0,0,0,0,0,3,3,3],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,3,3,0,0,0,0,0,0,1,1],
[1,1,0,0,1,0,0,0,0,0,3,3,0,0,0,0,0,0,1,0,0,1,1,1,1,0,0,0,0,0,0,1],
[0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1],
[0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,1,1,1,0],
[0,0,0,0,0,1,1,0,0,3,3,0,0,1,0,0,0,0,0,0,0,3,0,3,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0],
[1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0],
[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,3],
[1,1,1,1,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,1,0,0,0,1,1,1,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
[1,1,0,0,0,0,0,0,0,0,0,3,3,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1],
[1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
[1,0,0,0,3,3,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3],
[0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,3,3,0,3],
[3,3,3,3,3,1,0,0,0,1,1,1,1,0,1,1,1,1,1,1,0,0,0,0,0,0,3,3,0,0,0,3],
]

class Structure(pygame.sprite.Sprite) :
        def __init__(self) :
                super().__init__()

        def scroll (self, shift) :
                for plateform in self.plateforms :
                        plateform.x += shift
                #test print(plateform.x)                      # Probleme au niveau du scroll, aucun defilement..
                        
                        

        def  stage (self, data, screen) :
                self.gamer = Gamer()
                self.plateforms = []
                for r_index, row in enumerate (data) :
                        for c_index, cell in enumerate(row) :
                                if cell == 1:
                                        x = c_index * 60
                                        y = r_index * 40
                                        plateform = pygame.Rect( x, y, 60, 30) #self
                                        pygame.draw.rect(screen, (255, 255, 100), plateform )#
                                        self.plateforms.append(plateform)
                print(self.gamer.rect,'\n')
                
# Collision-------------------------------------------------------------------------------------[]----------------[]---------------[]----------------[]----------------[]---------------[]
                for plateform in self.plateforms :
                        if self.gamer.rect.colliderect(plateform ) :
                                print(' Leo ')
                                if self.gamer.falling is True:
                                        print(' FALLING EVENT ')            #Vertical collision (falling)
                                        self.gamer.rect.bottom = plateform.top
                                        self.gamer.falling = False
                                        print(' Yo ! ')
                                                        # Horizontal collision(sliding)
                                if gamer.direction < 0 :
                                        self.gamer.rect.left = plateform.right
                                elif gamer.direction > 0 :
                                        self.gamer.rect.right = plateform.left
                
