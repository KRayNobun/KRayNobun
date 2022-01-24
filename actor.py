import pygame

class Gamer (pygame.sprite.Sprite) :
    
    def __init__(self) :
        super().__init__()
        self.x, self.y = 320, 100
        self.hight = [15, 40]
        self.rect = pygame.Rect(self.x, self.y, self.hight[0], self.hight[1])
        self.screen = 550, 700
        self.jumped = False
        self.direction = 1
        self.falling = True
        
    def move (self, speed) :
        key = pygame.key.get_pressed()
        if key [pygame.K_LEFT] and self.rect.x > speed:
                self.rect.x -= speed
                self.direction = -1
                print(self.rect.x)
        elif key[pygame.K_RIGHT]and self.rect.x < (self.screen[0]-speed):
                self.rect.x += speed
                self.direction = 1

    def afficher(self, surface) :
        pygame.draw.rect ( surface, (255,0,0), self.rect)

    def fall(self, speedy) :
        if self.falling :
            self.rect.y += speedy
    def jump(self) :
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped is False :
            self.jumped = True
        if self.jumped is True :
                self.rect.y -= self.speed
                self.speed -= 2
                if self.speed < -20 :
                        self.jumped = False
                        self.speed = 20
