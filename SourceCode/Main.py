import pygame
import random
import time
from datetime import datetime
import pygame_menu 
from os import system
w_init = 1/2
h_init = 8/9
pygame.init()
infoObject = pygame.display.Info()
size = [int(infoObject.current_w*w_init),int(infoObject.current_h*h_init)]
screen = pygame.display.set_mode(size,pygame.RESIZABLE)
def show_mode():
    menu.clear()
    menu.add.button('Oasis',start_the_game_1)
    menu.add.button('Ice',start_the_game_2)
    menu.add.button('School')
    menu.add.button('Back', back)
    menu.add.button('Quit', pygame_menu.events.EXIT)

def back():
    menu.clear()
    menu.add.button('Select mode', show_mode)
    menu.add.button('Help',show_help)
    menu.add.button('Quit', pygame_menu.events.EXIT)

def help():
    menu.clear()

def show_help():
    menu.add.image(image_path='SourceCode/Image/howtoplay.png', angle=0, scale=(0.5, 0.5))

menu_image = pygame_menu.baseimage.BaseImage(image_path='SourceCode/Image/StartImage.png',drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
mytheme = pygame_menu.themes.THEME_ORANGE.copy()
mytheme.background_color = menu_image 
menu = pygame_menu.Menu('MUHIRRYO GOOD', size[0], size[1], theme=mytheme)
menu.add.button('Select mode', show_mode)
menu.add.button('Help', show_help)
menu.add.button('Quit',pygame_menu.events.EXIT)
background = pygame.image.load("SourceCode/Image/StartImage.png")
def start_the_game_1():
    import Oasis
def start_the_game_2():
    import Ice
def start_the_game_3():
    # import School
    pass
menu.mainloop(screen) 
pygame.quit()
