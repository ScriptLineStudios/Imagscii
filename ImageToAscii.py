import pygame
from PIL import Image
import numpy as np
import random
pygame.init()

replacements = {
    0: "#",
    10: "@",
    20: "$",
    30: "M",
    40: "W",
    50: "Q",
    60: "A",
    70: "&",
    80: "F",
    90: "D",
    100: "O",
    110: "?",
    120: "*",
    130: "<",
    140: ">",
    150: "^",
    160: "-",
    170: "_",
    180: "+",
    190: ".",
    200: ",",
    210: "'",
    220: "d",
    230: "'",
    240: "~",
    250: "`"
}

def greyscale(surface: pygame.Surface) -> pygame.surfarray:
    arr = pygame.surfarray.pixels3d(surface)
    mean_arr = np.dot(arr[:,:,:], [0.216, 0.587, 0.144])
    mean_arr3d = mean_arr[..., np.newaxis]
    new_arr = np.repeat(mean_arr3d[:, :, :], 3, axis=2)
    return pygame.surfarray.make_surface(new_arr)


def create_ascii_image(image_name, font_size, spacing) -> str:
    font = pygame.font.Font('freesansbold.ttf', font_size)
    image = Image.open(image_name)
    width, height = image.size
    width = width
    height = height
    image = image.resize((width, height))

    display = pygame.Surface((width, height))

    display.fill((0,0,0))

    for y in range(height):
        for x in range(width):
            color = image.getpixel((x, y))
            display.set_at((x, y), color)

    surf = greyscale(display)
    display.fill((255,255,255))

    for y in range(0, height, spacing):
        for x in range(0, width, spacing):
            color = pygame.Surface.get_at(surf, (x, y))
            for key, value in replacements.items():
                if color[0] >= key and color[0] < key+10:
                    text = font.render(value, True, (0,0,0))
                    display.blit(text, (x, y))

    name = f"{random.random()}.jpg"
    pygame.image.save(display, name)
    return name                                                         