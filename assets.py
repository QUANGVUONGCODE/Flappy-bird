import os
import pygame

sprites = {}
audio = {}
def load_prites():
    path = os.path.join('assets', 'sprites')
    for file in os.listdir(path):
        sprites[file.split('.')[0]] = pygame.image.load(os.path.join(path, file))

def get_sprite(name):
    return sprites[name]

def load_audios():
    path = os.path.join('assets', 'audios')
    for file in os.listdir(path):
        audio[file.split('.')[0]] = pygame.mixer.Sound(os.path.join(path, file))

def play_audio(name):
    audio[name].play()