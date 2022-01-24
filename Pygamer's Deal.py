import pygame
from actor import *
from  structure import *
from interaction import *

screen = pygame.display.set_mode((550, 700))
pygame.display.set_caption('   Simple Reflection    ')
structure = Structure()
gamer = Gamer()
interaction = Interaction()
#falling = True
launched = True


while launched :
        for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                        launched = False

        screen.fill('gray')
        gamer.fall(5)
        structure.stage(level_map, screen)
        structure.scroll(-2)
        gamer.move(10)
        gamer.afficher (screen)
        pygame.time.delay(40)
        pygame.display.update()                
        pygame.display.flip()
