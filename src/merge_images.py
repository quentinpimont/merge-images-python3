from PIL import Image
from enum import Enum

class Align(Enum):
    HORIZONTAL = 1
    VERTICAL = 2

def merge(array_images, save_location, align = Align.HORIZONTAL, mode = 'RGBA'):
    max_width = 0
    max_height = 0
    total_width = 0
    total_height = 0
    imgs_opened = []
    for image in array_images:
        current_img = Image.open(image)
        total_width += current_img.width
        total_height += current_img.height
        if(current_img.width > max_width):
            max_width = current_img.width
        if(current_img.height > max_height):
            max_height = current_img.height
        imgs_opened.append(current_img)
    if(align == Align.HORIZONTAL):
        new_img = Image.new(mode, (total_width, max_height))
    else:
        new_img = Image.new(mode, (max_width, total_height))
    for key, img_opened in enumerate(imgs_opened):
        paste_witdh = 0
        paste_height = 0
        if(align == Align.HORIZONTAL):
            paste_witdh = key * max_width
        else:
            paste_height = key * max_height
        new_img.paste(img_opened, (paste_witdh, paste_height));
    new_img.save(save_location)

