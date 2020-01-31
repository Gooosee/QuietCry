import pygame
import Button
import LoadImage
pygame.init()
size = width, height = 1280, 1024
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)


class Menu:
    def __init__(self):
        self.butNewG = Button.Button(992, 738, 124, 19)
        self.butLoadG = Button.Button(992, 760, 124, 19)
        self.butSurv = Button.Button(992, 782, 124, 19)
        self.butSettings = Button.Button(992, 804, 124, 19)
        self.butExit = Button.Button(992, 826, 124, 19)

    def updateClicked(self, pos):
        if self.butExit.clicked(pos, LoadImage.load_image('Exit_a.png', 'data')):
            quit()
        else:
            self.butExit.draw(screen, LoadImage.load_image('Exit_na.png', 'data'))
        if self.butSurv.clicked(pos, LoadImage.load_image('Surv_a.png', 'data')):
            return 'StartSurv'
        else:
            self.butSurv.draw(screen, LoadImage.load_image('Surv_na.png', 'data'))

    def updateNotClicked(self, pos):
        if self.butExit.clicked(pos, LoadImage.load_image('Exit_a.png', 'data')):
            pass
        else:
            self.butExit.draw(screen, LoadImage.load_image('Exit_na.png', 'data'))
        if self.butNewG.clicked(pos, LoadImage.load_image('newG_a.png', 'data')):
            pass
        else:
            self.butNewG.draw(screen, LoadImage.load_image('newG_na.png', 'data'))
        if self.butLoadG.clicked(pos, LoadImage.load_image('loadG_a.png', 'data')):
            pass
        else:
            self.butLoadG.draw(screen, LoadImage.load_image('loadG_na.png', 'data'))
        if self.butSurv.clicked(pos, LoadImage.load_image('Surv_a.png', 'data')):
            pass
        else:
            self.butSurv.draw(screen, LoadImage.load_image('Surv_na.png', 'data'))
        if self.butSettings.clicked(pos, LoadImage.load_image('Settings_a.png', 'data')):
            pass
        else:
            self.butSettings.draw(screen, LoadImage.load_image('Settings_na.png', 'data'))


MenuOpen = True
menu = Menu()
pospos = [0, 0]
iIntro = 1
while MenuOpen:
    if iIntro >= 17:
        if iIntro == 17:
            pygame.time.delay(800)
            iIntro += 1
        fon = LoadImage.load_image('menu.png', 'data')
        screen.blit(fon, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if menu.updateClicked(event.pos) == 'StartSurv':
                        MenuOpen = False
            elif event.type == pygame.MOUSEMOTION:
                menu.updateNotClicked(event.pos)
                pospos = event.pos
        menu.updateNotClicked(pospos)
    else:

        intro = LoadImage.load_image(f'Start{iIntro}.png', 'intro')
        screen.blit(intro, (0, 0))
        if iIntro == 16:
            pygame.mixer.music.load('sounds/music.mp3')
            pygame.mixer.music.play(100)
        if iIntro == 1:
            sound = pygame.mixer.Sound('sounds/scary_intro.wav')  # звук во время заставки
            sound.play()
            pygame.time.delay(200)
        if iIntro == 9:
            pygame.time.delay(200)
        iIntro += 1
    pygame.display.flip()
