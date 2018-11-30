from pygame_functions import *
import pygame
import os
import time
import random

base_folder = os.path.dirname(os.path.abspath(__file__))

def get_vol_pref():
    try:
        with open(base_folder+ "/resources/preferences/volume.txt", "r") as vol_pref:
            data = vol_pref.read()
            vol_pref.close()

            return data
    except:
        data = 0.5
        return data

def update_vol_pref(vol):
    with open(base_folder+ "/resources/preferences/volume.txt", "w") as vol_pref:
        vol_pref.write(str(vol))
        vol_pref.close()

def get_difficulty_pref():
    try:
        with open(base_folder+ "/resources/preferences/difficulty.txt", "r") as difficulty_pref:
            data = difficulty_pref.read()
            difficulty_pref.close()

            return data
    except:
        data = 0.1
        return data

def update_difficulty_pref(difficulty):
    with open(base_folder+ "/resources/preferences/difficulty.txt", "w") as difficulty_pref:
        difficulty_pref.write(str(difficulty))
        difficulty_pref.close()

#Title Screen
screen = screenSize(1000, 700)
bg_title = (base_folder + "/resources/assets/backgrounds/landscape.png")
bg_options = (base_folder + "/resources/assets/backgrounds/options.png")
bg_l1 = (base_folder + "/resources/assets/backgrounds/street.jpg")
bg_end = (base_folder + "/resources/assets/backgrounds/end.png")

setBackgroundImage(bg_title)
pygame.display.set_caption("Romeo and Juliet")

titleMusic = makeMusic(base_folder+"/resources/assets/sound/music/title.wav")
playMusic(-1)

pygame.mixer.music.set_volume(float(get_vol_pref()))

slider_hit = False
slider_hit_diff = False

class level():
    num = 0
    title = ""
    def scene_title(self):
        scene_titleLabel = makeLabel(self.title, 80, 100, 100, "white", "gabriola", "clear")

        return scene_titleLabel

def button_clicked(the_label, text, width, height, mouse, click, is_slider = False, is_difficulty = False):
    if not is_slider:
        if the_label.rect.topleft[0] + width > mouse[0] > the_label.rect.topleft[0] and the_label.rect.topleft[1] + height > mouse[1] > the_label.rect.topleft[1]:
            the_label.update(text, "black", "orange")
            if the_label.rect.topleft[0] == 100:
                moveLabel(the_label, (the_label.rect.topleft[0] + 20), the_label.rect.topleft[1])

            if click[0] == 1:
                return True
        else:
            the_label.update(text, "black", "white")
            if the_label.rect.topleft[0] == 120:
                moveLabel(the_label, (the_label.rect.topleft[0] - 20), the_label.rect.topleft[1])

    else:
        if not is_difficulty:
            if the_label.rect.topleft[0] + width > mouse[0] > the_label.rect.topleft[0] and the_label.rect.topleft[1] + height > mouse[1] > the_label.rect.topleft[1]:
                if click[0] == 1:
                    global slider_hit
                    slider_hit = True
                else:
                    slider_hit = False
            else:
                the_label.update(text, "black", "white")
        else:
            if the_label.rect.topleft[0] + width > mouse[0] > the_label.rect.topleft[0] and the_label.rect.topleft[1] + height > mouse[1] > the_label.rect.topleft[1]:
                if click[0] == 1:
                    global slider_hit_diff
                    slider_hit_diff = True
                else:
                    slider_hit_diff = False
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

    difficultySlider = makeLabel("    ", 50, ((float(get_difficulty_pref()) * 400) + 100), 400, "black", "gabriola", "white")
    difficultyLabel = makeLabel(" ", 60, 550, 400, "white", "gabriola", "clear")

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
            setBackgroundImage(bg_options)

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
            showLabel(difficultySlider), showLabel(difficultyLabel)

            b4 = button_clicked(backLabel, " Back", 190, 50, mouse, click)
            if b4 == True:
                is_intro = True
                is_options = False
                setBackgroundImage(bg_title)
                hideLabel(backLabel), hideLabel(soundLabel), hideLabel(soundSlider), hideLabel(difficultySlider), hideLabel(difficultyLabel)
                titleLabel_two.update("The Game", "white", 0)
                break

            button_clicked(soundSlider, "    ", 36, 51, mouse, click, True)
            button_clicked(difficultySlider, "    ", 36, 51, mouse, click, True, True)

            minimum = 100
            maximum = 500
            new_xpos = mouse[0] - 18
            if new_xpos < minimum:
                new_xpos = 100
            elif new_xpos > maximum:
                new_xpos = 500

            if slider_hit:
                moveLabel(soundSlider, new_xpos, 280)

            elif slider_hit_diff:
                moveLabel(difficultySlider, new_xpos, 400)

            volume_value = (soundSlider.rect.topleft[0] - 100) / 400
            pygame.mixer.music.set_volume(volume_value)
            soundLabel.update((str(int(volume_value * 100)) + "% - Volume"), "white", 0)

            update_vol_pref(volume_value)

            difficulty_value = (difficultySlider.rect.topleft[0] - 100) / 400
            difficultyLabel.update((str(int(difficulty_value * 100)) + "% - AI Difficulty"), "white", 0)
            update_difficulty_pref(difficulty_value)

            tick(30)

    #while selectCharacter:
    #    hideLabel(startLabel), hideLabel(optionsLabel), hideLabel(quitLabel)
    #    titleLabel_two.update("The Game - Role Selection", "white", 0)
    #    showLabel(selectMontague), showLabel(selectCapulet)

    #    mouse = pygame.mouse.get_pos()
    #    click = pygame.mouse.get_pressed()

    #    b5 = button_clicked(selectMontague, " Montagues", 220, 70, mouse, click)
    #    if b5 == True:
    #        is_intro = False
    #        selectCharacter = False
    #        chosenRole = "Montagues"
    #        break

    #    b6 = button_clicked(selectCapulet, " Capulets", 220, 70, mouse, click)
    #    if b6 == True:
    #        is_intro = False
    #        selectCharacter = False
    #        chosenRole = "Capulets"
    #        break

    #     tick(30)

    hideLabel(startLabel), hideLabel(optionsLabel), hideLabel(quitLabel), hideLabel(selectMontague), hideLabel(selectCapulet), hideLabel(titleLabel), hideLabel(titleLabel_two)
    #return chosenRole

fade = pygame.Surface((1000,700))
def fade_out(img):
    volume_value = get_vol_pref()
    while float(volume_value) > 0:
        volume_value = float(volume_value) - 0.25
        pygame.mixer.music.set_volume(float(volume_value))

    for alpha in range(0, 50):
        fade.set_alpha(alpha)
        #fade.fill((0, 0, 0))
        screen.blit(fade, (0,0))
        pygame.display.update()

    fade.set_alpha(None)
    screen.blit(fade, (0,0))
    pygame.display.update()

    setBackgroundImage(img)

def prologue():
    prologueMusic = makeMusic(base_folder+"/resources/assets/sound/music/prologue.mp3")
    playMusic(-1)
    pygame.mixer.music.set_volume(float(get_vol_pref()))

    #setBackgroundImage(bg_title)
    the_lines = makeSprite(base_folder+ "/resources/assets/images/prologue_lines.png")

    continueLabel_1 = makeLabel(" Continue", 60, 390, 550, "black", "gabriola", "white")
    ypos = 700

    show_prologue = True

    while show_prologue:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        showSprite(the_lines)
        if ypos >= -650:
            moveSprite(the_lines, 73, ypos)
            ypos -= 1.5

        else:
            pygame.time.delay(1)
            showLabel(continueLabel_1)
            b7 = button_clicked(continueLabel_1, " Continue", 220, 70, mouse, click)
            if b7 == True:

                show_prologue = False

        tick(30)

    hideLabel(continueLabel_1), hideSprite(the_lines), killSprite(the_lines)

def l1_transition():
    public_fight = level()
    public_fight.title = "Verona - A public place"
    l1_title = public_fight.scene_title()
    is_l1 = True

    while is_l1:
        showLabel(l1_title)
        time.sleep(3)

        is_l1 = False

        tick(30)

    hideLabel(l1_title)

#Create Sprites
sampson = makeSprite(base_folder + "/resources/assets/sprites/sampson.png", 2)
gregory = makeSprite(base_folder + "/resources/assets/sprites/gregory.png")
abram = makeSprite(base_folder + "/resources/assets/sprites/abram.png", 2)
benvolio = makeSprite(base_folder + "/resources/assets/sprites/benvolio.png", 5)
prince = makeSprite(base_folder + "/resources/assets/sprites/prince.png")
tybalt = makeSprite(base_folder + "/resources/assets/sprites/tybalt.png", 5)

health_left = makeSprite(base_folder + "/resources/assets/images/health_bar_left.png")
health_right = makeSprite(base_folder + "/resources/assets/images/health_bar_right.png")

def scene_1_fight():
    s1_f_1 = makeGenText("*Enter Benvolio*")
    s1_f_2 = makeGenText("Benvolio: Part, Fools!")
    s1_f_3 = makeGenText("Benvolio: Put up your swords, you know not what you do.")
    s1_f_4 = makeGenText("*Enter Tybalt*")
    s1_f_5 = makeGenText("Tybalt: Turn thee, Benvolio, look upon thy death.")
    s1_f_6 = makeGenText("Benvolio: I do but keep the peace. Put up thy sword,")
    s1_f_7 = makeGenText("Benvolio: Or manage it to part these men with me.")

    sampsonY = 300
    sampsonX = 100
    gregoryY = 300
    gregoryX = 300
    abramY = 300
    abramX = 750

    #They Fight
    prologueMusic = makeMusic(base_folder+"/resources/assets/sound/music/battle.wav")
    playMusic(-1)
    pygame.mixer.music.set_volume(float(get_vol_pref()))

    showSprite(health_left), showSprite(health_right), hideSprite(gregory)
    moveSprite(health_left, 20, 20),  moveSprite(health_right, 647, 20)

    sampsonHealth = 100
    abramHealth = 100

    #setBackgroundImage(bg_title)
    time.sleep(2)

    while True:

        drawRect(92, 134, ((sampsonHealth / 5) * 13), 21, "green") #5hp = 13 px
        drawRect(907, 134, -((abramHealth / 5) * 13) + 2, 21, "green")
        if keyPressed("right"):
            sampsonX += 7
            sampsonFacingLeft = False
            changeSpriteImage(sampson, 1)

        elif keyPressed("left"):
            sampsonX -= 7
            sampsonFacingLeft = True
            changeSpriteImage(sampson, 0)

        elif keyPressed("space"):

            swordSound = makeSound(base_folder + "/resources/assets/sound/sword/" + random.choice(os.listdir(base_folder + "/resources/assets/sound/sword/")))
            swordSound.set_volume(0.3)
            playSound(swordSound)

            if sampsonFacingLeft:
                changeSpriteImage(sampson, 0)
                if sampsonX <= abramX + 180 and sampsonX > abramX: #the 180 is abram's width + a bit extra
                    abramHealth -= 4
                    abramX -= 50

            else: #If facing right
                changeSpriteImage(sampson, 1)
                if sampsonX >= abramX - 180 and sampsonX < abramX:
                    abramHealth -= 4
                    abramX += 50

        difficulty = get_difficulty_pref()
        abramXchange = random.randrange(int(0 - (float(difficulty) * 500)), int((float(difficulty) * 500)))
        abramX += abramXchange

        if sampsonX > 1010:
            sampsonX = -140
        elif sampsonX < -140: #- Width of character -10
            sampsonX = 1010

        if abramX > 1010:
            abramX = -140
        elif abramX < -140:
            abramX = 1010

        moveSprite(sampson, sampsonX, sampsonY)
        moveSprite(abram, abramX, abramY)

        if abramX + abramXchange > abramX:
            changeSpriteImage(benvolio, 1)
        else:
            changeSpriteImage(benvolio, 0)

        abramAttack = random.randrange(1, 15)
        if abramAttack <= ((float(difficulty) - 0.05) * 15):
            if sampsonX <= abramX + 50 and sampsonX > abramX:
                swordSound = makeSound(base_folder + "/resources/assets/sound/sword/" + random.choice(os.listdir(base_folder + "/resources/assets/sound/sword/")))
                swordSound.set_volume(0.3)
                playSound(swordSound)
                sampsonHealth -= 10
                sampsonX -= 70

            elif sampsonX >= abramX - 50 and sampsonX < abramX:
                swordSound = makeSound(base_folder + "/resources/assets/sound/sword/" + random.choice(os.listdir(base_folder + "/resources/assets/sound/sword/")))
                swordSound.set_volume(0.3)
                playSound(swordSound)
                sampsonHealth -= 10
                sampsonX += 70

        if abramHealth <= 20 or sampsonHealth <= 20:
            stopMusic()
            smackSound = makeSound(base_folder + "/resources/assets/sound/smack.wav")

            playSound(smackSound)
            showSprite(benvolio), moveSprite(benvolio, 500, 250), moveSprite(sampson, 270, 250), moveSprite(abram, 800, 250)
            hideSprite(health_left), hideSprite(health_right)


            s1_f_labels = [s1_f_1, s1_f_2, s1_f_3, s1_f_4, s1_f_5, s1_f_6, s1_f_7]

            count = 0
            for label in s1_f_labels:
                if s1_f_labels[count] == s1_f_4:
                    showLabel(s1_f_4)
                    showSprite(tybalt), moveSprite(tybalt, 10, 250), changeSpriteImage(tybalt, 2)
                else:
                    showLabel(s1_f_labels[count])
                try:
                    hideLabel(s1_f_labels[count - 1])
                except:
                    pass

                count += 1
                time.sleep(1)

                while not keyPressed("enter"):
                    pass

            break

    hideLabel(s1_f_7)
    scene_1_fight_2()
    prince_speech()

def scene_1_fight_2():
    s1_f_2_1 = makeGenText("Tybalt: Peace? I hate the word. As I hate hell, all Montagues,")
    s1_f_2_1_2 = makeLabel("and thee.", 40, 50, 100, "black", "gabriola", "clear")
    s1_f_2_2 = makeGenText("Tybalt: Have at thee, coward!")

    s1_f_2_labels = [s1_f_2_1, s1_f_2_2]

    count = 0
    for label in s1_f_2_labels:
        if s1_f_2_labels[count] == s1_f_2_1:
            showLabel(s1_f_2_1), showLabel(s1_f_2_1_2)
        else:
            hideLabel(s1_f_2_1_2)
            showLabel(s1_f_2_labels[count])
        try:
            hideLabel(s1_f_2_labels[count - 1])
        except:
            pass
        count += 1
        time.sleep(1)

        while not keyPressed("enter"):
            pass

    hideLabel(s1_f_2_2), hideSprite(sampson), hideSprite(abram), hideSprite(gregory)

    #They Fight
    tybaltX = 50
    tybaltY = 250
    benvolioX = 600
    benvolioY = 250

    prologueMusic = makeMusic(base_folder+"/resources/assets/sound/music/battle.wav")
    playMusic(-1)
    pygame.mixer.music.set_volume(float(get_vol_pref()))

    showSprite(health_left), showSprite(health_right)
    moveSprite(health_left, 20, 20),  moveSprite(health_right, 647, 20)

    benvolioHealth = 100
    tybaltHealth = 100

    time.sleep(2)

    while True:
        drawRect(92, 134, ((tybaltHealth / 5) * 13), 21, "green") #5hp = 13 px
        drawRect(907, 134, -((benvolioHealth / 5) * 13) + 2, 21, "green")
        if keyPressed("right"):
            tybaltX += 7
            tybaltFacingLeft = False
            changeSpriteImage(tybalt, 3)

        elif keyPressed("left"):
            tybaltX -= 7
            tybaltFacingLeft = True
            changeSpriteImage(tybalt, 1)

        elif keyPressed("space"):
            swordSound = makeSound(base_folder + "/resources/assets/sound/sword/" + random.choice(os.listdir(base_folder + "/resources/assets/sound/sword/")))
            swordSound.set_volume(0.3)
            playSound(swordSound)

            if tybaltFacingLeft:
                changeSpriteImage(tybalt, 0)
                if tybaltX <= benvolioX + 180 and tybaltX > benvolioX: #the 180 is abram's width + a bit extra
                    benvolioHealth -= 4
                    benvolioX -= 50

            else: #If facing right
                changeSpriteImage(tybalt, 4)
                if tybaltX >= benvolioX - 180 and tybaltX < benvolioX:
                    benvolioHealth -= 4
                    benvolioX += 50

        difficulty = get_difficulty_pref()
        benvolioXchange = random.randrange(int(0 - (float(difficulty) * 500)), int((float(difficulty) * 500)))
        benvolioX += benvolioXchange

        if benvolioX + benvolioXchange > benvolioX:
            changeSpriteImage(benvolio, 3)
        else:
            changeSpriteImage(benvolio, 1)

        if tybaltX > 1010:
            tybaltX = -140
        elif tybaltX < -140: #- Width of character -10
            tybaltX = 1010

        if benvolioX > 1010:
            benvolioX = -140
        elif benvolioX < -140:
            benvolioX = 1010

        moveSprite(tybalt, tybaltX, tybaltY)
        moveSprite(benvolio, benvolioX, benvolioY)

        benvolioAttack = random.randrange(1, 15)
        if benvolioAttack <= ((float(difficulty) - 0.05) * 15):
            if tybaltX < benvolioX:
                changeSpriteImage(benvolio, 0)
            else:
                changeSpriteImage(benvolio, 4)
            if tybaltX <= benvolioX + 50 and tybaltX > benvolioX:
                swordSound = makeSound(base_folder + "/resources/assets/sound/sword/" + random.choice(os.listdir(base_folder + "/resources/assets/sound/sword/")))
                swordSound.set_volume(0.3)
                playSound(swordSound)
                tybaltHealth -= 10
                tybaltX -= 70

            elif tybaltX >= benvolioX - 50 and tybaltX < benvolioX:
                swordSound = makeSound(base_folder + "/resources/assets/sound/sword/" + random.choice(os.listdir(base_folder + "/resources/assets/sound/sword/")))
                swordSound.set_volume(0.3)
                playSound(swordSound)
                tybaltHealth -= 10
                tybaltX += 70

        if benvolioHealth <= 20 or tybaltHealth <= 20:
            stopMusic()
            smackSound = makeSound(base_folder + "/resources/assets/sound/smack.wav")

            playSound(smackSound)
            showSprite(prince), moveSprite(prince, 500, 250), moveSprite(tybalt, 200, 250), moveSprite(benvolio, 800, 250)
            hideSprite(health_left), hideSprite(health_right)

            break

def prince_speech():
    ps_1 = makeGenText("*Enter Prince*")
    ps_2 = makeGenText("Prince: Rebellious subjects, enemies to peace. You men, you beasts!")
    ps_3 = makeGenText("Prince: Throw your mistempered weapons to the ground, ")
    ps_4 = makeGenText("Prince: And hear the sentence of your movèd prince.")
    ps_5 = makeGenText("Prince: If you ever disturb our streets again,")
    ps_6 = makeGenText("Prince: Your lives shall pay the forfeit of the peace.")
    ps_7 = makeGenText("Prince: For this time all the rest depart away:")
    ps_8 = makeGenText("Prince: You, Capulet, shall go along with me,")
    ps_9 = makeGenText("Prince: And, Montague, come you this afternoon.")
    ps_10 = makeGenText("Prince: Once more, on pain of death, all men depart.")

    ps_c1_a = makeLabel(" Ignore Prince", 60, 230, 200, "black", "gabriola", "white")
    ps_c1_b = makeLabel(" Obey & Depart", 60, 550, 200, "black", "gabriola", "white")

    ps_labels = [ps_1, ps_2, ps_3, ps_4, ps_5, ps_6, ps_7, ps_8, ps_9, ps_10]

    count = 0
    for label in ps_labels:
        showLabel(ps_labels[count])
        try:
            hideLabel(ps_labels[count - 1])
        except:
            pass

        count += 1
        time.sleep(1)

        while not keyPressed("enter"):
            pass

    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        showLabel(ps_c1_a), showLabel(ps_c1_b)

        b12 = button_clicked(ps_c1_a, " Ignore Prince", 220, 70, mouse, click)
        b13 = button_clicked(ps_c1_b, " Obey & Depart", 220, 70, mouse, click)

        if b12 or b13: #If either clicked
            hideLabel(ps_c1_a), hideLabel(ps_c1_b), hideLabel(ps_10)
            break

        tick(30)

    if b12:
        ps_12 = makeGenText("Prince: Thee dare defy me?")
        ps_13 = makeGenText("Prince: Very well. Prepare to face thy death.")

        showLabel(ps_12)
        while not keyPressed("enter"):
            pass

        hideLabel(ps_12)
        showLabel(ps_13)

        time.sleep(1)

        while not keyPressed("enter"):
            pass

        hideLabel(ps_13)

        lightningSound = makeSound(base_folder + "/resources/assets/sound/lightning.wav")
        lightningSound.set_volume(0.6)
        playSound(lightningSound)

        lightning = makeSprite(base_folder + "/resources/assets/images/lightning.png")
        ash = makeSprite(base_folder + "/resources/assets/images/ash.png")
        showSprite(lightning)

        for x in range(25):
            moveSprite(lightning, int(random.randrange(50, 950)), -30) #test this
            time.sleep(0.1)

        hideAll()

        showSprite(ash)
        moveSprite(ash, 500, 640)

        setBackgroundImage(bg_end)
        ps_end_1 = makeGenText("*End Scene 1*")
        ps_end_1_2 = makeLabel("Status: Dead", 40, 50, 100, "black", "gabriola", "clear")
        ps_end_1_3 = makeLabel("Loyalty: Moderate", 40, 50, 150, "black", "gabriola", "clear")

        showLabel(ps_end_1), showLabel(ps_end_1_2), showLabel(ps_end_1_3)

    elif b13:
        hideAll()
        setBackgroundImage(bg_end)

        ps_end_2 = makeGenText("*End Scene 1*")
        ps_end_2_2 = makeLabel("Status: Alive", 40, 50, 100, "black", "gabriola", "clear")
        ps_end_2_3 = makeLabel("Loyalty: Moderate", 40, 50, 150, "black", "gabriola", "clear")

        showLabel(ps_end_2), showLabel(ps_end_2_2), showLabel(ps_end_2_3)

def scene_1():
    s1_1 = makeGenText("*Bantering*")
    s1_2 = makeGenText("Sampson: I will push Montague's men from the wall, and thrust his")
    s1_2_2 = makeLabel("maids to the wall.", 40, 50, 100, "black", "gabriola", "clear")
    s1_3 = makeGenText("Gregory: The quarrel is between our masters, and us their men.")
    s1_a1 = makeGenText("Gregory: Draw thy tool, here comes of the house of Montagues.")
    s1_4 = makeGenText("*Enter Abram*")
    s1_5 = makeGenText("Sampson: My naked weapon is out. Quarrel, I will back thee.")
    s1_a2 = makeGenText("Gregory: I will frown as I pass by.")
    s1_a3 = makeGenText("Sampson: I will bite my thumb at them.")
    s1_6 = makeGenText("Abram: Do you bite your thumb at us, sir?")
    s1_a4 = makeGenText("Sampson: [Aside] Is the law of our side if I say ay?")
    s1_a5 = makeGenText("Gregory: [Aside] No.")

    s1_c1_a = makeLabel(" Bite thumb", 60, 230, 200, "black", "gabriola", "white")
    s1_c1_b = makeLabel(" Don't bite", 60, 550, 200, "black", "gabriola", "white")

    changeSpriteImage(sampson, 1)

    sampsonY = 300
    sampsonX = 50
    gregoryY = 300
    gregoryX = 300
    abramY = 300
    abramX = 750

    s1_labels = [s1_1, s1_2, s1_3, s1_a1 ,s1_4, s1_5, s1_a2, s1_a3 ,s1_6, s1_a4, s1_a5]

    showSprite(sampson), showSprite(gregory)
    moveSprite(sampson, sampsonX, sampsonY), moveSprite(gregory, gregoryX, gregoryY)

    count = 0
    for label in s1_labels:
        if s1_labels[count] == s1_2:
            showLabel(s1_labels[count])
            showLabel(s1_2_2)
        elif s1_labels[count] == s1_3:
            hideLabel(s1_2_2)
            showLabel(s1_labels[count])
        elif s1_labels[count] == s1_4:
            hideLabel(s1_3)
            showLabel(s1_4)
            showSprite(abram), moveSprite(abram, abramX, abramY)
        else:
            showLabel(s1_labels[count])
        try:
            hideLabel(s1_labels[count - 1])
        except:
            pass

        count += 1
        time.sleep(1)

        while not keyPressed("enter"):
            pass

    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        showLabel(s1_c1_a), showLabel(s1_c1_b)

        b8 = button_clicked(s1_c1_a, " Bite thumb", 220, 70, mouse, click)
        b9 = button_clicked(s1_c1_b, " Don't bite", 220, 70, mouse, click)

        if b8 or b9: #If either clicked
            hideLabel(s1_c1_a), hideLabel(s1_c1_b), hideLabel(s1_a5)
            break

        tick(30)

    if b8:
        s1_a6 = makeGenText("Sampson: Indeed I do, sir.")
        s1_a7 = makeGenText("Abram: Thee wilt suffer! Draw, if you be men.")

        showLabel(s1_a6)
        while not keyPressed("enter"):
            pass

        hideLabel(s1_a6)
        showLabel(s1_a7)

        time.sleep(3)
        hideLabel(s1_a7)

        scene_1_fight()


    elif b9:
        s1_7 = makeGenText("Sampson: No, sir, I do not bite my thumb at you, sir, but I do bite")
        s1_7_2 = makeLabel("my thumb, sir.", 40, 50, 100, "black", "gabriola", "clear")
        s1_8 = makeGenText("*Enter Benvolio*")
        s1_9 = makeGenText("Benvolio: Part, Fools!")
        s1_10 = makeGenText("*Enter Tybalt*")
        s1_11 = makeGenText("Tybalt: Turn thee, Benvolio, look upon thy death.")
        s1_12 = makeGenText("Benvolio: I do but keep the peace. Put up thy sword,")
        s1_13 = makeGenText("Benvolio: Or manage it to part these men with me.")

        s1_c2_a = makeLabel(" Keep Peace", 60, 230, 200, "black", "gabriola", "white")
        s1_c2_b = makeLabel(" Fight     ", 60, 550, 200, "black", "gabriola", "white")

        tybaltX = 190
        tybaltY = 250
        benvolioX = 500
        benvolioY = 250

        s1_labels_2 = [s1_7, s1_8, s1_9, s1_10, s1_11, s1_12, s1_13]

        count = 0
        for label in s1_labels_2:
            if s1_labels_2[count] == s1_7:
                showLabel(s1_7), showLabel(s1_7_2)
            if s1_labels_2[count] == s1_8:
                hideLabel(s1_7_2)
                showLabel(s1_labels_2[count])
                showSprite(benvolio), moveSprite(benvolio, benvolioX, benvolioY), hideSprite(gregory)
            elif s1_labels_2[count] == s1_10:
                showLabel(s1_labels_2[count])
                showSprite(tybalt), moveSprite(tybalt, tybaltX, tybaltY), changeSpriteImage(tybalt, 2)
            else:
                showLabel(s1_labels_2[count])
            try:
                hideLabel(s1_labels_2[count - 1])
            except:
                pass

            count += 1
            time.sleep(1)

            while not keyPressed("enter"):
                pass

        while True:
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            showLabel(s1_c2_a), showLabel(s1_c2_b)

            b10 = button_clicked(s1_c2_a, " Keep Peace", 220, 70, mouse, click)
            b11 = button_clicked(s1_c2_b, " Fight     ", 220, 70, mouse, click)

            if b10 or b11: #If either clicked
                hideLabel(s1_c2_a), hideLabel(s1_c2_b), hideLabel(s1_13)
                break

            tick(30)

        if b11:
            scene_1_fight_2()
            prince_speech()

        elif b10:
            s1_14 = makeGenText("Sampson: O calm, dishonourable, vile submission!")
            s1_15 = makeGenText("Sampson: Villain! You side with our enemy!")
            s1_16 = makeGenText("Tybalt: For too long has this ancient grudge")
            s1_17 = makeGenText("Tybalt: Poisoned the quiet of our streets.")
            s1_18 = makeGenText("Sampson: Coward! *Stabs Tybalt*")

            s1_labels_3 = [s1_14, s1_15, s1_16, s1_17, s1_18]

            count = 0
            for label in s1_labels_3:
                if s1_labels_3[count] == s1_18:
                    hideLabel(s1_17)
                    showLabel(s1_18)
                    moveSprite(sampson, tybaltX, tybaltY)
                    swordSound = makeSound(base_folder + "/resources/assets/sound/sword/" + random.choice(os.listdir(base_folder + "/resources/assets/sound/sword/")))
                    swordSound.set_volume(0.5)
                    playSound(swordSound)

                    time.sleep(1)
                    moveSprite(sampson, sampsonX, sampsonY)
                    moveSprite(tybalt, tybaltX, (tybaltY + 180))
                else:
                    showLabel(s1_labels_3[count])
                try:
                    hideLabel(s1_labels_3[count - 1])
                except:
                    pass

                count += 1
                time.sleep(1)

                while not keyPressed("enter"):
                    pass

            hideLabel(s1_18)
            hideAll()
            fade_out(bg_end)

            s1_e_1 = makeGenText("*End Scene 1*")
            s1_e_2 = makeLabel("Status: Dead", 40, 50, 100, "black", "gabriola", "clear")
            s1_e_3 = makeLabel("Loyalty: Little", 40, 50, 150, "black", "gabriola", "clear")

            showLabel(s1_e_1), showLabel(s1_e_2), showLabel(s1_e_3)

chosen_role = intro()

fade_out(bg_title)
stopMusic()
time.sleep(1)

prologue()
fade_out(bg_l1)
stopMusic()

l1_transition()
fade_out(bg_l1)

scene_1()

while True:
    updateDisplay()

#endWait()
