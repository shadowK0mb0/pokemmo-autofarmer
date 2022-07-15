import numpy as np
from PIL import Image, ImageChops
from collections.abc import Iterable
from typing import Any, AnyStr, NoReturn, Tuple, Union, Optional 

def paste_grid_on_image(grid_square_size:int, image:Image, inplace:bool=False):
    grid = np.zeros((image.size[0], image.size[1], 4))
    grid[:, grid_square_size::grid_square_size, :] = 255
    grid[grid_square_size::grid_square_size, :, :] = 255
    grid_image = Image.fromarray(grid.astype('uint8'))
    if not inplace:
        base_image = image.copy()
        base_image.paste(grid_image, None, grid_image)
        return base_image
    else:
        image.paste(grid_image, None, grid_image)
        return image

def crop_to_game(image:Image) -> Image:
    return image.crop([0,30,1920,1020])

def validate_pokemmo_running(image:Image) -> bool:
    assert(image.size == (1920, 1080))
    logo = Image.open("pokemmo_logo.png")
    possible_logo = image.crop([0,0,logo.size[0],logo.size[1]])
    diff = ImageChops.difference(logo, possible_logo)
    return not diff.getbbox()

def have_sweet_scent(image:Image) -> bool:
    assert(image.size == (1920, 1080))
    no_sweet_scent_img = Image.open("no_sweet_scent.png")
    curr_sweet_scent = image.crop([893,53,938,96])
    diff = ImageChops.difference(no_sweet_scent_img, curr_sweet_scent)
    return diff.getbbox() is not None

