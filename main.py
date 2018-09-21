from pygame_functions import *
import pygame
import os

print(pygame.font.get_fonts())

base_folder = os.path.dirname(__file__)

#Title Screen
screenSize(1000, 700)
setBackgroundImage(base_folder+"/resources/assets/backgrounds/space.png")
pygame.display.set_caption("Romeo and Juliet")

titleMusic = makeMusic(base_folder+"/resources/assets/sound/music/title.wav")
playMusic(-1)

titleLabel = makeLabel("Romeo and Juliet", 80, 285, 100, "white", "gabriola")

drawRect(350, 250, 300, 80, "gray")
drawRect(350, 250, 300, 80, "black", 5)

drawRect(350, 400, 300, 80, "gray")
drawRect(350, 400, 300, 80, "black", 5)

drawRect(350, 550, 300, 80, "gray")
drawRect(350, 550, 300, 80, "black", 5)

start = False
intro = True

while intro:
    showLabel(titleLabel)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    #Button 1 (Start)
    if 350+300 > mouse[0] > 350 and 250+80 > mouse[1] > 250:
        drawRect(350, 250, 300, 80, "cyan")
        drawRect(350, 250, 300, 80, "black", 5)
        if click[0] == 1:
            print("Click 1 Received! \n")
            start = True
            intro = False
    else:
        drawRect(350, 250, 300, 80, "gray")
        drawRect(350, 250, 300, 80, "black", 5)

    #Button 2 (Options)
    if 350+300 > mouse[0] > 350 and 400+80 > mouse[1] > 400:
        drawRect(350, 400, 300, 80, "cyan")
        drawRect(350, 400, 300, 80, "black", 5)
        if click[0] == 1:
            print("Click 2 Received! \n")
            start = True
            intro = False
    else:
        drawRect(350, 400, 300, 80, "gray")
        drawRect(350, 400, 300, 80, "black", 5)

    #Button 3 (Quit)
    if 350+300 > mouse[0] > 350 and 550+80 > mouse[1] > 550:
        drawRect(350, 550, 300, 80, "cyan")
        drawRect(350, 550, 300, 80, "black", 5)
        if click[0] == 1:
            print("Click 3 Received! \n")
            quit()
    else:
        drawRect(350, 550, 300, 80, "gray")
        drawRect(350, 550, 300, 80, "black", 5)


    if start:
        setBackgroundImage(base_folder+"/resources/assets/backgrounds/stars.png")

    else:
        pass

    tick(30)

hideLabel(titleLabel)
endWait()
