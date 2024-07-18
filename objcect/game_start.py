
import pygame.sprite
import assets, config
from layer import Layer

class GameStart(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = Layer.UI
        self.image = assets.get_sprite('message')
        self.rect = self.image.get_rect(center  = (config.SCREEN_WIDTH/2 , config.SCREEN_HEIGHT/2))

        super().__init__(*groups)