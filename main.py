from pygame_functions import *
import pygame
import os
import time

base_folder = os.path.dirname(os.path.abspath(__file__))

def get_vol_pref():
    with open(base_folder+ "/resources/preferences/volume.txt", "r") as vol_pref:
        data = vol_pref.read()
        vol_pref.close()

        return data

def update_vol_pref(vol):
    with open(base_folder+ "/resources/preferences/volume.txt", "w") as vol_pref:
        vol_pref.write(str(vol))
        vol_pref.close()

#Title Screen
screen = screenSize(1000, 700)
bg_image = (base_folder+ "/resources/assets/backgrounds/landscape.png")
setBackgroundImage(bg_image)
pygame.display.set_caption("Romeo and Juliet")

titleMusic = makeMusic(base_folder+"/resources/assets/sound/music/title.wav")
playMusic(-1)

pygame.mixer.music.set_volume(float(get_vol_pref()))

slider_hit = False

class level():
    num = 0
    def generic_function():
        return num

def button_clicked(the_label, text, width, height, mouse, click, is_slider = False):
    if not is_slider:
        if the_label.rect.topleft[0] + width > mouse[0] > the_label.rect.topleft[0] and the_label.rect.topleft[1] + height > mouse[1] > the_label.rect.topleft[1]:
            the_label.update(text, "black", "orange")
            if the_label.rect.topleft[0] == 100:
                moveLabel(the_label, (the_label.rect.topleft[0] + 20), the_label.rect.topleft[1])

            if click[0] == 1:
                print("Click Received! \n")
                return True
        else:
            the_label.update(text, "black", "white")
            if the_label.rect.topleft[0] == 120:
                moveLabel(the_label, (the_label.rect.topleft[0] - 20), the_label.rect.topleft[1])

    else:
        if the_label.rect.topleft[0] + width > mouse[0] > the_label.rect.topleft[0] and the_label.rect.topleft[1] + height > mouse[1] > the_label.rect.topleft[1]:
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
    is_fade = False
    chosenRole = ""

    titleLabel = makeLabel("Romeo and Juliet", 80, 100, 100, "white", "gabriola", "clear")
    titleLabel_two = makeLabel("The Game", 60, 100, 180, "white", "gabriola", "clear")
    startLabel = makeLabel(" Start", 50, 100, 280, "black", "gabriola", "white")
    optionsLabel = makeLabel(" Options", 50, 100, 360, "black", "gabriola", "white")
    quitLabel = makeLabel(" Quit", 50, 100, 440, "black", "gabriola", "white")
    backLabel = makeLabel(" Back", 50, 100, 520, "black", "gabriola", "white")

    soundSlider = makeLabel("    ", 50, ((float(get_vol_pref()) * 400) + 100), 280, "black", "gabriola", "white")
    soundLabel = makeLabel(" ", 60, 550, 280, "white", "gabriola", "clear")

    selectMontague = makeLabel(" Montagues", 60, 240, 320, "black", "gabriola", "white")
    selectCapulet = makeLabel(" Capulets", 60, 540, 320, "black", "gabriola", "white")

    while is_intro:
        showLabel(titleLabel), showLabel(titleLabel_two) ,showLabel(startLabel), showLabel(optionsLabel), showLabel(quitLabel)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #Button 1 (Start)
        b1 = button_clicked(startLabel, " Start", 190, 50, mouse, click)
        if b1 == True:
            is_intro = False
            selectCharacter = True

        #Button 2 (Options)
        b2 = button_clicked(optionsLabel, " Options", 190, 50, mouse, click)
        if b2 == True:
            is_intro = False
            is_options = True

        #Button 3 (Quit)
        b3 = button_clicked(quitLabel, " Quit", 190, 50, mouse, click)
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

            b4 = button_clicked(backLabel, " Back", 190, 50, mouse, click)
            if b4 == True:
                is_intro = True
                is_options = False
                hideLabel(backLabel), hideLabel(soundLabel), hideLabel(soundSlider)
                titleLabel_two.update("The Game", "white", 0)
                break

            button_clicked(soundSlider, "    ", 36, 51, mouse, click, True)

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

            update_vol_pref(volume_value)

            tick(30)

    while selectCharacter:
        hideLabel(startLabel), hideLabel(optionsLabel), hideLabel(quitLabel)
        titleLabel_two.update("The Game - Role Selection", "white", 0)
        showLabel(selectMontague), showLabel(selectCapulet)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        b5 = button_clicked(selectMontague, " Montagues", 220, 70, mouse, click)
        if b5 == True:
            is_intro = False
            selectCharacter = False
            chosenRole = "Montagues"
            break

        b6 = button_clicked(selectCapulet, " Capulets", 220, 70, mouse, click)
        if b6 == True:
            is_intro = False
            selectCharacter = False
            chosenRole = "Capulets"
            break

        tick(30)

    hideLabel(selectMontague), hideLabel(selectCapulet), hideLabel(titleLabel), hideLabel(titleLabel_two)
    return chosenRole

chosen_role = intro()

#Fade out
fade = pygame.Surface((1000,700))
def fade_out():
    for alpha in range(0, 50):
        fade.set_alpha(alpha)
        fade.fill((0, 0, 0))
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(1)

fade_out()
stopMusic()

#Fancy loading screen here?

def prologue():
    setBackgroundImage(bg_image)
    the_lines = makeSprite(base_folder+ "/resources/assets/images/prologue_lines.png")

    continueLabel_1 = makeLabel(" Continue", 60, 390, 550, "black", "gabriola", "white")
    ypos = 700

    show_prologue = True

    while show_prologue:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        showSprite(the_lines)
        if ypos >= -750:
            moveSprite(the_lines, 73, ypos)
            ypos -= 1.5

        else:
            pygame.time.delay(1)
            showLabel(continueLabel_1)
            b7 = button_clicked(continueLabel_1, " Continue", 220, 70, mouse, click)
            if b7 == True:
                print("Yay")
                #Do button stuff

        tick(30)

prologue()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
    #Perhaps consider updateDisplay() if bugs arise
#endWait()
