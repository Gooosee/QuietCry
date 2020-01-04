import pygame
import os


def load_image(name, path, colorkey=None):  # функция для загрузки изображений
    fullname = os.path.join(path, name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image
