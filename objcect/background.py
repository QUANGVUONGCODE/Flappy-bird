import pygame.sprite
import assets, config
from layer import Layer

class Background(pygame.sprite.Sprite): 
    def __init__(self,indx, *groups):
        self._layer = Layer.BACKGROUND
        self.image = assets.get_sprite('background')
        self.rect = self.image.get_rect(topleft = (config.SCREEN_WIDTH * indx, 0))
        super().__init__(*groups)
    
    def update(self):
        self.rect.x -= 1
        if self.rect.right <= 0:
            self.rect.x = config.SCREEN_WIDTH