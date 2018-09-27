from pygame_functions import *
import pygame
import os

base_folder = os.path.dirname(os.path.abspath(__file__))

#Title Screen
screenSize(1000, 700)
background = (base_folder+ "/resources/assets/backgrounds/landscape.png")
setBackgroundImage(background)
pygame.display.set_caption("Romeo and Juliet")

titleMusic = makeMusic(base_folder+"/resources/assets/sound/music/title.wav")
playMusic(-1)

def button_clicked(the_label, text, xpos, width, ypos, height, mouse, click):
    if xpos + width > mouse[0] > xpos and ypos + height > mouse[1] > ypos:
        the_label.update(text, "black", "orange")
        if click[0] == 1:
            print("Click Received! \n")
            return True
    else:
        the_label.update(text, "black", "white")


def intro():
    is_intro = True
    is_options = False
    selectCharacter = False

    titleLabel = makeLabel("Romeo and Juliet", 80, 100, 100, "white", "gabriola", "clear")
    titleLabel_two = makeLabel("The Game", 60, 100, 180, "white", "gabriola", "clear")
    startLabel = makeLabel(" Start", 50, 100, 280, "black", "gabriola", "white")
    optionsLabel = makeLabel(" Options", 50, 100, 360, "black", "gabriola", "white")
    quitLabel = makeLabel(" Quit", 50, 100, 440, "black", "gabriola", "white")

    while is_intro:
        showLabel(titleLabel), showLabel(titleLabel_two) ,showLabel(startLabel), showLabel(optionsLabel), showLabel(quitLabel)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #Button 1 (Start)
        b1 = button_clicked(startLabel, " Start", 100, 190, 280, 50, mouse, click)
        if b1 == True:
            is_intro = False
            selectCharacter = True

        #Button 2 (Options)
        b2 = button_clicked(optionsLabel, " Options", 100, 190, 360, 50, mouse, click)
        if b2 == True:
            is_intro = False
            is_options = True

        #Button 3 (Quit)
        b3 = button_clicked(quitLabel, " Quit", 100, 190, 440, 50, mouse, click)
        if b3 == True:
            is_intro = False
            quit()

        tick(30)

    while is_options:
        hideLabel(startLabel), hideLabel(optionsLabel), hideLabel(quitLabel)
        titleLabel_two.update("The Game - Options", "white", 0)


        tick(30)

    while selectCharacter:
        hideLabel(startLabel), hideLabel(optionsLabel), hideLabel(quitLabel)


        tick(30)

intro()

endWait()
