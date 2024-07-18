import pygame
import config
import assets
from objcect.background import Background
from objcect.bird import Bird
from objcect.floor import Floor
from objcect.column import Column
from objcect.game_over import GameOver
from objcect.game_start import GameStart
from objcect.score import Score

pygame.init()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
game_over = False
game_start = False

assets.load_prites()

column_create_event = pygame.USEREVENT
assets.load_prites()
assets.load_audios()


sprites = pygame.sprite.LayeredUpdates()
def create_sprites():
    Background(0,sprites)
    Background(1,sprites)

    Floor(0, sprites)
    Floor(1, sprites)

    return Bird(sprites), GameStart(sprites), Score(sprites)
  
bird, Game_start_message, score = create_sprites()

pygame.time.set_timer(column_create_event, 1200)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == column_create_event:
            Column(sprites)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_start:
                game_start = True
                Game_start_message.kill()
                pygame.time.set_timer(column_create_event, 1200)
            if event.key == pygame.K_ESCAPE and game_over:
                game_over = False
                game_start = False
                sprites.empty()
                bird, Game_start_message, score = create_sprites()
        bird.handle_event(event)

    screen.fill(0)

    sprites.draw(screen) 

    if game_start and not game_over:
        sprites.update()

    if bird.check_collision(sprites) and not game_over:
        game_over = True
        game_start = False
        GameOver(sprites)
        pygame.time.set_timer(column_create_event, 0)
        assets.play_audio('hit')

    for sprite in sprites:
        if type(sprite) is Column and sprite.is_passed():
            score.value += 1
            assets.play_audio('point')
    pygame.display.flip()
    clock.tick(config.FPS) 

pygame.quit()