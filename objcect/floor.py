import pygame.sprite
import assets, config
from layer import Layer

class Floor(pygame.sprite.Sprite):
    def __init__(self,indx, *groups):
        self._layer = Layer.FLOOR
        self.image = assets.get_sprite('floor')
        self.rect = self.image.get_rect(bottomleft = (config.SCREEN_WIDTH * indx, config.SCREEN_HEIGHT))
        self.mask = pygame.mask.from_surface(self.image)
        super().__init__(*groups)

    def update(self):
        self.rect.x -= 2

        if self.rect.right <= 0:
            self.rect.x = config.SCREEN_WIDTH