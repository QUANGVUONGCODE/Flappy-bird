import pygame
import assets
import config
from layer import Layer
from objcect.column import Column
from objcect.floor import Floor


class Bird(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = Layer.PLAYER
        
        self.images = [
            assets.get_sprite('redbird-upflap'),
            assets.get_sprite('redbird-midflap'),
            assets.get_sprite('redbird-downflap'),
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft = (-50,50))

        self.mask = pygame.mask.from_surface(self.image)

        self.flag = 0
        
        super().__init__(*groups)

    def update(self):
        self.images.insert(0,self.images.pop()) 
        self.image = self.images[0]

        self.flag += config.GRAVITY
        self.rect.y += self.flag

        if self.rect.x < 50:
            self.rect.x += 3

    def handle_event(self,event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.flag = 0
            self.flag -= 4
            assets.play_audio('wing')

    def check_collision(self,sprites):
        for sprite in sprites:
            if ((type(sprite) is Column or type(sprite) is Floor) and sprite.mask.overlap(self.mask,(self.rect.x - sprite.rect.x, self.rect.y - sprite.rect.y)) or self.rect.bottom < 0) :
                return True
        return False
    
