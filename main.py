from pygame_functions import *
import pygame
import os

base_folder = os.path.dirname(__file__)

#Title Screen
screenSize(1000, 700)
setBackgroundImage(base_folder+"/resources/assets/backgrounds/landscape.png")
pygame.display.set_caption("Romeo and Juliet")

titleMusic = makeMusic(base_folder+"/resources/assets/sound/music/title.wav")
playMusic(-1)

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
        if 100+190 > mouse[0] > 100 and 280+50 > mouse[1] > 280:
            startLabel.update(" Start", "black", "orange")
            if click[0] == 1:
                print("Click Received! \n")
                is_intro = False
                selectCharacter = True
        else:
            startLabel.update(" Start", "black", "white")

        #Button 2 (Options)
        if 100+190 > mouse[0] > 100 and 360+50 > mouse[1] > 360:
            optionsLabel.update(" Options", "black", "orange")
            if click[0] == 1:
                print("Click Received! \n")
                is_intro = False
                is_options = True
        else:
            optionsLabel.update(" Options", "black", "white")

        #Button 3 (Quit)
        if 100+190 > mouse[0] > 100 and 440+50 > mouse[1] > 440:
            quitLabel.update(" Quit", "black", "orange")
            if click[0] == 1:
                print("Click Received! \n")
                is_intro = False
                quit()
        else:
            quitLabel.update(" Quit", "black", "white")

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
