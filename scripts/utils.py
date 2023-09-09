import os
import pygame

BASE_IMG_PATH = 'data/images/'

def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img

def load_images(path):
    images  = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)): # loop through all the files in the folder and sort them alphabetically
        images.append(load_image(path + '/' + img_name)) # load the image and append it to the list
    return images