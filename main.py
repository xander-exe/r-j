from pygame_functions import *
import pygame
import os

base_folder = os.path.dirname(os.path.abspath(__file__))

#Title Screen
screenSize(1000, 700)
bg_image = (base_folder+ "/resources/assets/backgrounds/landscape.png")
setBackgroundImage(bg_image)
pygame.display.set_caption("Romeo and Juliet")

titleMusic = makeMusic(base_folder+"/resources/assets/sound/music/title.wav")
playMusic(-1)
pygame.mixer.music.set_volume(0.5)

slider_hit = False

def button_clicked(the_label, text, xpos, width, ypos, height, mouse, click, is_slider = False):
    if not is_slider:
        if xpos + width > mouse[0] > xpos and ypos + height > mouse[1] > ypos:
            the_label.update(text, "black", "orange")
            if click[0] == 1:
                print("Click Received! \n")
                return True
        else:
            the_label.update(text, "black", "white")
    else:
        if the_label.rect.topleft[0] + width > mouse[0] > the_label.rect.topleft[0] and ypos + height > mouse[1] > ypos:
            if click[0] == 1:
                global slider_hit
                slider_hit = True
            else:
                slider_hit = False
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
    backLabel = makeLabel(" Back", 50, 100, 520, "black", "gabriola", "white")

    soundSlider = makeLabel("    ", 50, 300, 280, "black", "gabriola", "white")
    soundLabel = makeLabel(" ", 60, 550, 280, "white", "gabriola", "clear")

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

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            showLabel(soundSlider), showLabel(soundLabel), showLabel(backLabel)

            b4 = button_clicked(backLabel, " Back", 100, 190, 500, 50, mouse, click)
            if b4 == True:
                is_intro = True
                is_options = False
                hideLabel(backLabel), hideLabel(soundLabel), hideLabel(soundSlider)
                titleLabel_two.update("The Game", "white", 0)
                break

            button_clicked(soundSlider, "    ", 0, 36, 280, 51, mouse, click, True)

            minimum = 100
            maximum = 500
            new_xpos = mouse[0] - 18
            if new_xpos < minimum:
                new_xpos = 100
            elif new_xpos > maximum:
                new_xpos = 500

            if slider_hit:
                moveLabel(soundSlider, new_xpos, 280)

            volume_value = (soundSlider.rect.topleft[0] - 100) / 400
            pygame.mixer.music.set_volume(volume_value)
            soundLabel.update((str(int(volume_value * 100)) + "% - Volume"), "white", 0)

            tick(30)

    while selectCharacter:
        hideLabel(startLabel), hideLabel(optionsLabel), hideLabel(quitLabel)

        tick(30)

intro()

endWait()
