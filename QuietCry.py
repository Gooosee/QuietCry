import random
import sqlite3
import sys
import Button
import pygame
from random import choice
import LoadImage
import webbrowser


pygame.init()

# создание окна
blood = True
size = width, height = 1280, 1024
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.display.set_caption('QuietCry')
# загрузка спрайтов
f = True
blood = True
soundPlay = True
time_wave = [1, 20, 30, 40, 50, 60, 70, 80, 90, 105, 120, 135, 150, 165, 190]
dead = False  # Проверка на смерть персонажа
bulletKill = False  # Проверка на нанесение дамага врагу, чтобы не удалить пулю до урона
person_sprites = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
tile_sprites = pygame.sprite.Group()
bullet_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
particle_sprites = pygame.sprite.Group()
aid_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()


personRunM4 = [LoadImage.load_image('anim1_person_run_m4a1s.png', 'data'),
               LoadImage.load_image('anim2_person_run_m4a1s.png', 'data'),
               LoadImage.load_image('anim3_person_run_m4a1s.png', 'data')]

personRunLeftM4 = [pygame.transform.flip(personRunM4[0], True, False),
                   pygame.transform.flip(personRunM4[1], True, False),
                   pygame.transform.flip(personRunM4[2], True, False)]

personJumpM4 = [LoadImage.load_image('anim1_person_jump_m4a1s.png', 'data'),
                LoadImage.load_image('anim2_person_jump_m4a1s.png', 'data'),
                LoadImage.load_image('anim3_person_jump_m4a1s.png', 'data'),
                LoadImage.load_image('anim4_person_jump_m4a1s.png', 'data')]

personJumpLeftM4 = [pygame.transform.flip(personJumpM4[0], True, False),
                    pygame.transform.flip(personJumpM4[1], True, False),
                    pygame.transform.flip(personJumpM4[2], True, False),
                    pygame.transform.flip(personJumpM4[3], True, False)]

personFireM4 = [LoadImage.load_image('anim1_person_fire_m4a1s.png', 'data'),
                LoadImage.load_image('anim2_person_fire_m4a1s.png', 'data'),
                LoadImage.load_image('anim3_person_fire_m4a1s.png', 'data'),
                LoadImage.load_image('anim4_person_fire_m4a1s.png', 'data'),
                LoadImage.load_image('anim2_person_fire_m4a1s.png', 'data'),
                LoadImage.load_image('anim3_person_fire_m4a1s.png', 'data'),
                LoadImage.load_image('anim4_person_fire_m4a1s.png', 'data'),
                LoadImage.load_image('anim2_person_fire_m4a1s.png', 'data'),
                LoadImage.load_image('anim3_person_fire_m4a1s.png', 'data')]

personFireLeftM4 = [pygame.transform.flip(personFireM4[0], True, False),
                    pygame.transform.flip(personFireM4[1], True, False),
                    pygame.transform.flip(personFireM4[2], True, False),
                    pygame.transform.flip(personFireM4[3], True, False),
                    pygame.transform.flip(personFireM4[4], True, False),
                    pygame.transform.flip(personFireM4[5], True, False),
                    pygame.transform.flip(personFireM4[6], True, False),
                    pygame.transform.flip(personFireM4[7], True, False),
                    pygame.transform.flip(personFireM4[8], True, False)]

personStopM4 = [LoadImage.load_image('anim1_person_stop_m4a1s.png', 'data'),
                LoadImage.load_image('anim2_person_stop_m4a1s.png', 'data'),
                LoadImage.load_image('anim3_person_stop_m4a1s.png', 'data'),
                LoadImage.load_image('anim4_person_stop_m4a1s.png', 'data')]

personStopLeftM4 = [pygame.transform.flip(personStopM4[0], True, False),
                    pygame.transform.flip(personStopM4[1], True, False),
                    pygame.transform.flip(personStopM4[2], True, False),
                    pygame.transform.flip(personStopM4[3], True, False)]

personRunSG = [LoadImage.load_image('anim1_run_shotgun.png', 'data'),
               LoadImage.load_image('anim2_run_shotgun.png', 'data'),
               LoadImage.load_image('anim3_run_shotgun.png', 'data')]

personRunLeftSG = [pygame.transform.flip(personRunSG[0], True, False),
                   pygame.transform.flip(personRunSG[1], True, False),
                   pygame.transform.flip(personRunSG[2], True, False)]

personJumpSG = [LoadImage.load_image('anim1_jump_shotgun.png', 'data'),
                LoadImage.load_image('anim2_jump_shotgun.png', 'data'),
                LoadImage.load_image('anim3_jump_shotgun.png', 'data'),
                LoadImage.load_image('anim4_jump_shotgun.png', 'data')]

personJumpLeftSG = [pygame.transform.flip(personJumpSG[0], True, False),
                    pygame.transform.flip(personJumpSG[1], True, False),
                    pygame.transform.flip(personJumpSG[2], True, False),
                    pygame.transform.flip(personJumpSG[3], True, False)]

personFireSG = [LoadImage.load_image('anim1_fire_shotgun.png', 'data'),
                LoadImage.load_image('anim2_fire_shotgun.png', 'data'),
                LoadImage.load_image('anim3_fire_shotgun.png', 'data')]

personFireLeftSG = [pygame.transform.flip(personFireSG[0], True, False),
                    pygame.transform.flip(personFireSG[1], True, False),
                    pygame.transform.flip(personFireSG[2], True, False)]

personStopSG = [LoadImage.load_image('anim1_stop_shotgun.png', 'data'),
                LoadImage.load_image('anim2_stop_shotgun.png', 'data'),
                LoadImage.load_image('anim3_stop_shotgun.png', 'data'),
                LoadImage.load_image('anim4_stop_shotgun.png', 'data')]

personStopLeftSG = [pygame.transform.flip(personStopSG[0], True, False),
                    pygame.transform.flip(personStopSG[1], True, False),
                    pygame.transform.flip(personStopSG[2], True, False),
                    pygame.transform.flip(personStopSG[3], True, False)]

enemyARun = [LoadImage.load_image('anim1_enemyA_run.png', 'data'),
             LoadImage.load_image('anim2_enemyA_run.png', 'data'),
             LoadImage.load_image('anim3_enemyA_run.png', 'data'),
             LoadImage.load_image('anim4_enemyA_run.png', 'data'),
             LoadImage.load_image('anim5_enemyA_run.png', 'data')]

enemyARunLeft = [pygame.transform.flip(enemyARun[0], True, False),
                 pygame.transform.flip(enemyARun[1], True, False),
                 pygame.transform.flip(enemyARun[2], True, False),
                 pygame.transform.flip(enemyARun[3], True, False),
                 pygame.transform.flip(enemyARun[4], True, False)]

enemyAJump = [LoadImage.load_image('anim1_enemyA_jump.png', 'data'),
              LoadImage.load_image('anim2_enemyA_jump.png', 'data'),
              LoadImage.load_image('anim3_enemyA_jump.png', 'data'),
              LoadImage.load_image('anim4_enemyA_jump.png', 'data'),
              LoadImage.load_image('anim5_enemyA_jump.png', 'data')]

enemyAJumpLeft = [pygame.transform.flip(enemyAJump[0], True, False),
                  pygame.transform.flip(enemyAJump[1], True, False),
                  pygame.transform.flip(enemyAJump[2], True, False),
                  pygame.transform.flip(enemyAJump[3], True, False),
                  pygame.transform.flip(enemyAJump[4], True, False)]

enemyAKick = [LoadImage.load_image('anim1_enemyA_kick.png', 'data'),
              LoadImage.load_image('anim2_enemyA_kick.png', 'data'),
              LoadImage.load_image('anim3_enemyA_kick.png', 'data'),
              LoadImage.load_image('anim4_enemyA_kick.png', 'data')]

enemyAKickLeft = [pygame.transform.flip(enemyAKick[0], True, False),
                  pygame.transform.flip(enemyAKick[1], True, False),
                  pygame.transform.flip(enemyAKick[2], True, False),
                  pygame.transform.flip(enemyAKick[3], True, False)]

tile_images = {'plat_d1': LoadImage.load_image('plat_down1.png', 'data'),
               'plat_d2': LoadImage.load_image('plat_down2.png', 'data'),
               'plat_d3': LoadImage.load_image('plat_down3.png', 'data'),
               'plat_u1': LoadImage.load_image('plat_up1.png', 'data'),
               'plat_u2': LoadImage.load_image('plat_up2.png', 'data'),
               'plat_u3': LoadImage.load_image('plat_up3.png', 'data')}

aid_kid = LoadImage.load_image('aid_kid.png', 'data')

coin = LoadImage.load_image('coin1.png', 'data')

bull = LoadImage.load_image('bullet.png', 'data')


def start():
    global buul, running, kill, wave_count, i, textWave, iWave, weapon, money, pers, sg, HP, speed, power, Power, win
    for y in [person_sprites, all_sprites, tile_sprites, bullet_sprites, enemy_sprites, particle_sprites, aid_sprites,
              coin_sprites]:
        for j in y:
            j.kill()
            y.remove(j)
    running = False
    money = 0
    buul = []
    sg = False
    kill = 0  # количество убитых монстров
    wave_count = 0  # Номер волны
    i = 0  # Счетчик для таймера
    textWave = None  # Текст для вывода волны
    iWave = None  # Время в которое начала показываться надпись с волной
    weapon = 'm4a1s'
    pers = Person(305, 856)  # Начальное положение персонажа
    win = 0
    HP = 0
    speed = 0
    power = 0
    Power = 10


class Particle(pygame.sprite.Sprite):
    # сгенерируем частицы разного размера

    def __init__(self, pos, dx, dy):
        super().__init__(particle_sprites)
        self.a = random.randint(5, 15)
        self.image = pygame.Surface([self.a, self.a])
        self.image.fill([50, 0, 0])
        self.rect = pygame.Rect(pos[0], pos[1], self.a, self.a)

        # у каждой частицы своя скорость — это вектор
        self.velocity = [dx, dy]
        # гравитация будет одинаковой (значение константы)
        self.gravity = 5

    def update(self):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации
        self.velocity[1] += self.gravity
        # перемещаем частицу
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        # убиваем, если частица ушла за экран
        if len(pygame.sprite.spritecollide(self, tile_sprites, False)) >= 1:
            self.kill()


def start_screen(frase):  # заставка
    delay = 0  # задержка для мигания надписи
    text1 = "Quiet Cry"
    fon = pygame.transform.scale(LoadImage.load_image('fon_b.png', 'data'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 150)
    string_rendered = font.render(text1, 1, pygame.Color('black'))
    intro_rect = string_rendered.get_rect()
    intro_rect.y = 50
    intro_rect.x = 330
    screen.blit(string_rendered, intro_rect)

    while True:
        delay += 1
        if delay % 5 == 0:
            text2 = f"Нажмите любую кнопку {frase}"
        else:
            text1, text2 = "Quiet Cry", ""
            fon = pygame.transform.scale(LoadImage.load_image('fon_b.png', 'data'), (width, height))
            screen.blit(fon, (0, 0))
            font = pygame.font.Font(None, 150)
            string_rendered = font.render(text1, 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            intro_rect.y = 50
            intro_rect.x = 330
            screen.blit(string_rendered, intro_rect)
        font = pygame.font.Font(None, 70)
        string_rendered = font.render(text2, 1, pygame.Color('green'))
        intro_rect = string_rendered.get_rect()
        intro_rect.y = 950
        intro_rect.x = 100
        screen.blit(string_rendered, intro_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        pygame.time.Clock().tick(5)


class Person(pygame.sprite.Sprite):
    global i, soundPlay

    def __init__(self, x, y):
        super().__init__(person_sprites)
        # Начальные координаты персонажа
        self.fullBul = 25
        self.shop = 25
        self.pos_x = x
        self.fullHP = 200
        self.hp = 200
        self.fireSG = 0
        self.jump_count = 10
        self.re20 = False
        self.pos_y = y
        self.sdvig = False
        self.landing = 855  # координата приземления при запрыгивание на платформу
        self.if_jump = False
        self.direction = False
        self.cur_frame = 0  # Номер кадра
        self.frames = personStopM4  # Анимация стоя
        self.image = personStopM4[self.cur_frame]  # Изображение спрайта
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.pos_x, self.pos_y)
        self.soundTime = -99
        self.tm = -6
        self.tm_jump = -6
        self.shop_size_m4 = 25
        self.shop_size_sg = 8
        self.speed = 10

    def run(self, keys):  # Бег
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction = True  # Персонаж смотрит влево
            if weapon == 'm4a1s':
                self.frames = personRunLeftM4
            else:
                self.frames = personRunLeftSG
            if (Platforms.generate_level(Platforms.load_level('first_level.txt'), self.rect[0] // tile_width,
                                         (self.rect[1] + self.rect[3]) // tile_height) or
                Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                         (self.rect[0] + self.rect[2] - 20) // tile_width,
                                         (self.rect[1] + self.rect[3]) // tile_height)
                and not self.if_jump) and self.rect.x > 1:
                self.rect.x -= self.speed  # Смещение влево
            elif self.if_jump and self.rect.x > 1:
                self.rect.x -= self.speed
            elif self.rect.x > 1:
                for x in range((self.rect[1] + self.rect[3]) // tile_height, height // tile_height):
                    if (Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                                 self.rect[0] // tile_width, x) or
                            Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                                     (self.rect[0] + self.rect[2] - 20) // tile_width, x)):
                        self.rect.y = (x - 4) * tile_height - 2
                        break
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction = False  # Персонаж смотрит вправо
            if weapon == 'm4a1s':
                self.frames = personRunM4
            else:
                self.frames = personRunSG
            if (Platforms.generate_level(Platforms.load_level('first_level.txt'), (self.rect[0] + 20) // tile_width,
                                         (self.rect[1] + self.rect[3]) // tile_height) or
                Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                         (self.rect[0] + self.rect[2]) // tile_width,
                                         (self.rect[1] + self.rect[3]) // tile_height)
                and not self.if_jump) and (self.rect.x + self.rect[2]) < width - 6:
                self.rect.x += self.speed  # Смещение вправо
            elif self.if_jump and (self.rect.x + self.rect[2]) < width - 6:
                self.rect.x += self.speed
            elif (self.rect.x + self.rect[2]) < width - 6:
                for x in range((self.rect[1] + self.rect[3]) // tile_height, height // tile_height):
                    if (Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                                 (self.rect[0] + 20) // tile_width, x) or
                            Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                                     (self.rect[0] + self.rect[2]) // tile_width, x)):
                        self.rect.y = (x - 4) * tile_height - 2
                        break

    def stop(self):  # Отсутствие движения
        if self.direction:
            if weapon == 'm4a1s':
                self.frames = personStopLeftM4
            else:
                self.frames = personStopLeftSG
        else:
            if weapon == 'm4a1s':
                self.frames = personStopM4
            else:
                self.frames = personStopSG

    def jump(self):  # Прыжок
        stop = True
        if self.direction:
            if weapon == 'm4a1s':
                self.frames = personJumpLeftM4[:2]
            else:
                self.frames = personJumpLeftSG[:2]
        else:
            if weapon == 'm4a1s':
                self.frames = personJumpM4[:2]
            else:
                self.frames = personJumpSG[:2]
        if self.jump_count > 0:
            if self.direction:
                if weapon == 'm4a1s':
                    self.frames = personJumpLeftM4[2:3]
                else:
                    self.frames = personJumpLeftSG[2:3]
            else:
                if weapon == 'm4a1s':
                    self.frames = personJumpM4[2:3]
                else:
                    self.frames = personJumpSG[2:3]
            if not (Platforms.generate_level(Platforms.load_level('first_level.txt'), self.rect[0] // tile_width,
                                             (self.rect[1] // tile_height) - 1) or
                    Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                             (self.rect[0] + self.rect[2]) // tile_width,
                                             (self.rect[1] // tile_height) - 1)):
                self.rect.y -= self.jump_count ** 2 // 2
                self.jump_count -= 1
            else:
                if self.jump_count != 10:
                    self.jump_count += 1
                    self.jump_count *= -1
                else:
                    self.rect.y = self.landing - 55
                    stop = False
                    self.if_jump = False
                    self.re20 = True
        elif stop:
            if self.direction:
                if weapon == 'm4a1s':
                    self.frames = personJumpLeftM4[3:4]
                else:
                    self.frames = personJumpLeftSG[3:4]
            else:
                if weapon == 'm4a1s':
                    self.frames = personJumpM4[3:4]
                else:
                    self.frames = personJumpSG[3:4]
            for x in range((self.rect[1] + self.rect[3]) // tile_height, height // tile_height):
                if (Platforms.generate_level(Platforms.load_level('first_level.txt'), self.rect[0] // tile_width,
                                             x) or
                        Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                                 (self.rect[0] + self.rect[2]) // tile_width, x)):
                    self.landing = (x - 9) * tile_height + 6
                    break
            if self.rect.y + self.jump_count ** 2 // 2 <= self.landing:
                self.rect.y += self.jump_count ** 2 // 2
            else:
                self.rect.y = self.landing + 35
                self.if_jump = False
                self.re20 = True
                stop = False
            self.jump_count -= 1
        if self.jump_count == -10 and stop:
            self.if_jump = False
            self.re20 = True
            self.rect.y += 35
            for x in range((self.rect[1] + self.rect[3]) // tile_height, height // tile_height):
                if (Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                             (self.rect[0] + 20) // tile_width, x) or
                        Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                                 (self.rect[0] + self.rect[2]) // tile_width, x)):
                    self.rect.y = (x - 7) * tile_height + 3
                    break

    def fire(self):  # Стрельба
        if self.direction:
            if weapon == 'm4a1s':
                if self.shop_size_m4 > 0:
                    if soundPlay:
                        sound = pygame.mixer.Sound('sounds\pfire.wav')  # звуки стрельбы
                        sound.play()
                    self.frames = personFireLeftM4
            else:
                if self.shop_size_sg > 0:
                    if soundPlay:
                        sound = pygame.mixer.Sound('sounds\shootg.wav')  # звуки стрельбы
                        sound.play()
                    self.frames = personFireLeftSG
        else:
            if weapon == 'm4a1s':
                if self.shop_size_m4 > 0:
                    if soundPlay:
                        sound = pygame.mixer.Sound('sounds\pfire.wav')  # звуки стрельбы
                        sound.play()
                    self.frames = personFireM4
            else:
                if self.shop_size_sg > 0:
                    if soundPlay:
                        sound = pygame.mixer.Sound('sounds\shootg.wav')  # звуки стрельбы
                        sound.play()
                    self.frames = personFireSG
        global buul
        if weapon == 'm4a1s':
            if self.shop_size_m4 > 0:
                if self.cur_frame in [2, 4, 6]:
                    buul.append(Bullet(self.rect.x + 60, self.rect.y + 36, self.direction))  # Создание пули
                    self.shop_size_m4 -= 1
        else:
            if self.shop_size_sg > 0:
                self.fireSG = i
                buul.append(Bullet(self.rect.x + 60, self.rect.y + 36, self.direction, 'up', 200))
                buul.append(Bullet(self.rect.x + 60, self.rect.y + 36, self.direction, '', 250))
                buul.append(Bullet(self.rect.x + 60, self.rect.y + 20, self.direction, '', 250))
                buul.append(Bullet(self.rect.x + 60, self.rect.y + 36, self.direction, 'down', 200))
                self.shop_size_sg -= 1
                if soundPlay:
                    sound = pygame.mixer.Sound('sounds\shotgun_dop.wav')  # звуки стрельбы
                    sound.play()

    def reload(self):
        if weapon == 'm4a1s':
            if soundPlay:
                sound = pygame.mixer.Sound('sounds\preload_m4.wav')
                sound.play()
            self.shop_size_m4 = 25
        else:
            if soundPlay:
                for _ in range(2):
                    sound = pygame.mixer.Sound('sounds\preload_sg.wav')
                    sound.play()
            self.shop_size_sg = 8

    def update(self, time):
        if self.hp <= 0:
            global dead, money
            dead = True
            money = 0
            global blood
            if blood:
                for _ in range(30):  # Создание частиц крови
                        part = Particle([self.rect.x + 50, self.rect.y + 30], random.randint(-8, 8), random.randint(-5, 3))
            self.kill()
        elif self.hp < 50 and time - self.soundTime >= 1:
            if soundPlay:
                soundBr = pygame.mixer.Sound('sounds/heavyBreathing.wav')  # звук тяжелого дыхания
                soundBr.play()
            self.soundTime = time
        running = False
        keys = pygame.key.get_pressed()  # в этом списке лежат все нажатые кнопки
        if self.re20:
            self.rect.y += 55
            self.re20 = False
        if keys[pygame.K_RIGHT] or keys[pygame.K_a] or keys[pygame.K_LEFT] or keys[pygame.K_d]:
            # Нажаты клавиши для бега
            self.run(keys)
            running = True
        if not self.if_jump:
            if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.tm_jump + 3 < i:  # Нажат прыжок
                self.tm_jump = i
                self.if_jump = True
                self.landing = self.rect.y
                self.jump_count = 10
                self.rect.y -= 40
            elif keys[pygame.K_h] and not running and -self.fireSG + i >= 1 and self.tm + 4 <= i:  # Нажатие клавиши "h" для стрельбы
                self.fire()
            elif keys[pygame.K_r] and self.tm + 4 <= i:
                self.tm = i
                self.reload()
            elif not (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_d]):
                self.stop()  # отсутствие движения
        else:
            self.jump()
        if weapon == 'm4a1s':
            self.fullBul = 25
            self.shop = self.shop_size_m4
        else:
            self.shop = self.shop_size_sg
            self.fullBul = 8
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame - 1]


class Bullet(pygame.sprite.Sprite):  # Класс пуль
    def __init__(self, x, y, direction_bul, UpOrDown='', rangeB=1240):
        super().__init__(bullet_sprites)
        self.x, self.y, self.direction_bul, self.UpOrDown = x, y, direction_bul, UpOrDown
        self.rangeB = rangeB
        self.image = bull  # Изображение пули
        self.rect = self.image.get_rect()
        if direction_bul:  # Проверка направления и смещение координаты появления пули
            self.x -= 25
        self.rect = self.rect.move(self.x, self.y)

    def update(self, *args):
        global f
        if self.UpOrDown == 'up':
            self.rect.y += 5
        elif self.UpOrDown == 'down':
            self.rect.y -= 5
        if not self.direction_bul:
            if self.rect.x - self.x >= self.rangeB:
                self.kill()
            if self.rect.x <= 1280:
                self.rect.x += 60
            else:
                self.kill()  # Уничтожение пуль вышедших за границы экрана
        else:
            if self.x - self.rect.x >= self.rangeB:
                self.kill()
            if self.rect.x >= 0:
                self.rect.x -= 60
            else:
                self.kill()  # Уничтожение пуль вышедших за границы экрана
        if len(pygame.sprite.spritecollide(self, tile_sprites, False)) >= 1:
            self.kill()


class EnemyA(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(enemy_sprites)
        # Начальные координаты персонажа
        self.hp = 40
        self.pos_x = x
        self.pos_y = y
        self.running = False
        self.if_jump = False
        self.jump_count = 10
        self.frames = enemyARun  # Анимация стоя
        self.cur_frame = 0  # Номер кадра
        self.image = enemyARun[self.cur_frame]  # Изображение спрайта
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.pos_x, self.pos_y + 15)
        if self.rect.x < (width // 2):
            self.direction = False
        else:
            self.direction = True

    def run(self):  # Бег
        if pers.rect.x < self.rect.x:
            self.frames = enemyARunLeft
            if (Platforms.generate_level(Platforms.load_level('first_level.txt'), self.rect[0] // tile_width,
                                         (self.rect[1] + self.rect[3]) // tile_height) or
                    Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                             (self.rect[0] + self.rect[2] - 20) // tile_width,
                                             (self.rect[1] + self.rect[3]) // tile_height)
                    and not self.if_jump):
                self.rect.x -= 6
            elif self.if_jump:
                self.rect.x -= 6
            else:
                for x in range((self.rect[1] + self.rect[3]) // tile_height, height // tile_height):
                    if (Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                                 self.rect[0] // tile_width, x) or
                            Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                                     (self.rect[0] + self.rect[2] - 20) // tile_width, x)):
                        self.rect.y = (x - 3) * tile_height
                        break  # Смещение влево
            self.direction = True  # Персонаж смотрит влево
        elif pers.rect.x > self.rect.x:
            self.frames = enemyARun
            if (Platforms.generate_level(Platforms.load_level('first_level.txt'), (self.rect[0] + 20) // tile_width,
                                         (self.rect[1] + self.rect[3]) // tile_height) or
                    Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                             (self.rect[0] + self.rect[2]) // tile_width,
                                             (self.rect[1] + self.rect[3]) // tile_height)
                    and not self.if_jump):
                self.rect.x += 6  # Смещение вправо
            elif self.if_jump:
                self.rect.x += 6
            else:
                for x in range((self.rect[1] + self.rect[3]) // tile_height, height // tile_height):
                    if (Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                                 (self.rect[0] + 20) // tile_width, x) or
                            Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                                     (self.rect[0] + self.rect[2]) // tile_width, x)):
                        self.rect.y = (x - 3) * tile_height - 6
                        break
            self.direction = False  # Монстр смотрит вправо

    def upper_run(self):
        if self.direction:
            self.frames = enemyARunLeft
            if (Platforms.generate_level(Platforms.load_level('first_level.txt'), self.rect[0] // tile_width,
                                         (self.rect[1] + self.rect[3]) // tile_height) or
                    Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                             (self.rect[0] + self.rect[2]) // tile_width,
                                             (self.rect[1] + self.rect[3]) // tile_height)):
                self.rect.x -= 6
            else:
                for x in range((self.rect[1] + self.rect[3]) // tile_height, height // tile_height):
                    if (Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                                 self.rect[0] // tile_width, x) or
                            Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                                     (self.rect[0] + self.rect[2]) // tile_width, x)):
                        self.rect.y = (x - 3) * tile_height - 6
                        break  # Смещение влево
            self.direction = True
        else:
            self.frames = enemyARun
            if (Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                         (self.rect[0]) // tile_width,
                                         (self.rect[1] + self.rect[3]) // tile_height) or
                    Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                             (self.rect[0] + self.rect[2]) // tile_width,
                                             (self.rect[1] + self.rect[3]) // tile_height)):
                self.rect.x += 6
            else:
                for x in range((self.rect[1] + self.rect[3]) // tile_height, height // tile_height):
                    if (Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                                 (self.rect[0]) // tile_width, x) or
                            Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                                     (self.rect[0] + self.rect[2]) // tile_width, x)):
                        self.rect.y = (x - 3) * tile_height - 6
                        break
            self.direction = False

    def lower_run(self):
        if self.direction:
            self.frames = enemyARunLeft
            if (Platforms.generate_level(Platforms.load_level('first_level.txt'), self.rect[0] // tile_width,
                                         (self.rect[1] + self.rect[3]) // tile_height) or
                    Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                             (self.rect[0] + self.rect[2] - 20) // tile_width,
                                             (self.rect[1] + self.rect[3]) // tile_height)
                    and not self.if_jump):
                self.rect.x -= 6
            elif self.if_jump:
                self.rect.x -= 6
            else:
                for x in range((self.rect[1] + self.rect[3]) // tile_height, height // tile_height):
                    if (Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                                 self.rect[0] // tile_width, x) or
                            Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                                     (self.rect[0] + self.rect[2] - 20) // tile_width, x)):
                        self.rect.y = (x - 3) * tile_height - 6
                        break  # Смещение влево
            self.direction = True  # Персонаж смотрит влево
        else:
            self.frames = enemyARun
            if (Platforms.generate_level(Platforms.load_level('first_level.txt'), (self.rect[0] + 20) // tile_width,
                                         (self.rect[1] + self.rect[3]) // tile_height) or
                    Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                             (self.rect[0] + self.rect[2]) // tile_width,
                                             (self.rect[1] + self.rect[3]) // tile_height)
                    and not self.if_jump):
                self.rect.x += 6  # Смещение вправо
            elif self.if_jump:
                self.rect.x += 6
            else:
                for x in range((self.rect[1] + self.rect[3]) // tile_height, height // tile_height):
                    if (Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                                 (self.rect[0] + 20) // tile_width, x) or
                            Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                                     (self.rect[0] + self.rect[2]) // tile_width, x)):
                        self.rect.y = (x - 3) * tile_height - 6
                        break
            self.direction = False  # Монстр смотрит вправо

    def kick(self):
        if self.direction:
            self.frames = enemyAKickLeft
        else:
            self.frames = enemyAKick
        pers.hp -= 10

    def jump(self):  # Прыжок
        stop = True
        if self.direction:
            self.frames = enemyAJumpLeft[:1]
        else:
            self.frames = enemyAJump[:1]
        if self.jump_count > 0:
            if self.direction:
                self.frames = enemyAJumpLeft[2:3]
            else:
                self.frames = enemyAJump[2:3]
            if not (Platforms.generate_level(Platforms.load_level('first_level.txt'), self.rect[0] // tile_width,
                                             (self.rect[1] // tile_height) - 1) or
                    Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                             (self.rect[0] + self.rect[2]) // tile_width,
                                             (self.rect[1] // tile_height) - 1)):
                self.rect.y -= self.jump_count ** 2 // 2
                self.jump_count -= 1
            else:
                self.jump_count += 1
                self.jump_count *= -1
        elif stop:
            if self.direction:
                self.frames = enemyAJumpLeft[2:3]
            else:
                self.frames = enemyAJump[2:3]
            for x in range((self.rect[1] + self.rect[3]) // tile_height, height // tile_height):
                if (Platforms.generate_level(Platforms.load_level('first_level.txt'), self.rect[0] // tile_width,
                                             x) or
                        Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                                 (self.rect[0] + self.rect[2]) // tile_width, x)):
                    self.landing = (x - 9) * tile_height - 15
                    break
            if self.rect.y + self.jump_count ** 2 // 2 <= self.landing:
                self.rect.y += self.jump_count ** 2 // 2
            else:
                self.rect.y = self.landing + 105
                stop = False
                self.if_jump = False
                self.re20 = True
            self.jump_count -= 1
        if self.jump_count == -10 and stop:
            if self.direction:
                self.frames = enemyAJumpLeft[4:]
            else:
                self.frames = enemyAJump[4:]
            self.if_jump = False
            self.re20 = True
            self.rect.y += 100

    def update(self):
        global f, kill
        if self.hp <= 0:
            global money
            money += 10
            if blood:
                for _ in range(20):  # Создание частиц
                    part = Particle([self.rect.x + 50, self.rect.y + 20], random.randint(-8, 8), random.randint(-5, 3))
            aid_chance = random.choice([1, 0, 0, 0, 0, 0, 0, 0, 0])  # шанс выпадения аптечки
            coin_chance = random.choice([1, 0, 0, 0, 0, 0, 0, 0])  # шанс выпадения монеты
            if aid_chance:
                Aid(self.rect.x, self.rect.y + 37, self.if_jump)
            elif coin_chance:
                Coin(self.rect.x, self.rect.y + 37, self.if_jump)
            self.kill()
            kill += 1
        if self.hp < 40:
            pygame.draw.line(screen, (255, 0, 0), (self.rect.x, self.rect.y),
                             (self.rect.x + 2 * self.hp, self.rect.y), 7)
        if self.rect.x <= 0:
            self.direction = False
        elif self.rect.x >= 1180:
            self.direction = True
        if self.rect.y < pers.rect.y:
            self.upper_run()
        elif (self.rect.y - 45) > pers.rect.y:
            self.lower_run()
        elif abs(self.rect.x - pers.rect.x) > 70:  # Персонаж вне зоны досягаемости
            self.run()
            self.running = True  # Враг бежит
        if not self.if_jump:
            if abs(self.rect.x - pers.rect.x) <= 70 and abs(
                    - pers.rect.y + self.rect.y) <= 50 and not self.running:  #
                self.kick()
            elif - pers.rect.y + self.rect.y > 150:  # Нажат прыжок
                self.if_jump = True
                self.jump_count = 10
                self.landing = self.rect.y
        else:
            self.jump()
        global buul
        if len(pygame.sprite.spritecollide(self, bullet_sprites, False)) >= 1:
            for j in buul:
                if self.rect.x <= j.rect.x <= self.rect.x + 81 and self.rect.y <= j.rect.y <= self.rect.y + 69:
                    j.kill()
                    buul.remove(j)
                    self.hp -= Power
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame - 1]
        self.running = False  # Враг стоит


def wave():  # Создание волн
    global wave_count
    global textWave
    global iWave
    xxl = xxr = yyl = yyr = 20  # Сдвиг каждого следующего мостра
    wave_count += 1
    font = pygame.font.Font(None, 100)
    textWave = font.render(f"WAVE {str(wave_count)}", True, [100, 0, 0])  # текст
    iWave = i
    for y in range(wave_count):
        if y % 4 == 0:
            en = EnemyA(-50 - xxl, 840)
            xxl += 40
        elif y % 4 == 1:
            en = EnemyA(1280 + xxr, 840)
            xxr += 40
        elif y % 4 == 2:
            en = EnemyA(0, -10 - yyl)
            yyl += 40
        elif y % 4 == 3:
            en = EnemyA(1280, -10 - yyr)
            yyr += 40


class Aid(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, if_jump):
        super().__init__(aid_sprites)
        global i
        self.image = aid_kid
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(pos_x, pos_y)
        self.time = i
        self.jump_count = 0
        self.landing = 915
        self.if_jump = if_jump

    def fall(self):
        for x in range((self.rect[1] + self.rect[3]) // tile_height, height // tile_height):
            if (Platforms.generate_level(Platforms.load_level('first_level.txt'), self.rect[0] // tile_width,
                                         x) or
                    Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                             (self.rect[0] + self.rect[2]) // tile_width, x)):
                self.landing = (x - 2) * tile_height + 10
                break
        if self.rect.y + self.jump_count ** 2 // 2 <= self.landing:
            self.rect.y += self.jump_count ** 2 // 2
        else:
            self.rect.y = self.landing
            self.if_jump = False
        self.jump_count += 1

    def update(self):
        if self.if_jump:
            self.fall()
        if self.time + 14 < i:
            self.kill()
        if len(pygame.sprite.spritecollide(self, person_sprites, False)) >= 1 and pers.hp < pers.fullHP:
            sound = pygame.mixer.Sound('sounds/pick_up_aid.wav')
            sound.play()
            pers.hp = pers.hp + 50
            if pers.hp > pers.fullHP:
                pers.hp = pers.fullHP
            self.kill()


class Coin(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, if_jump):
        super().__init__(aid_sprites)
        global i
        self.image = coin
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(pos_x, pos_y)
        self.time = i
        self.jump_count = 0
        self.landing = 915
        self.if_jump = if_jump

    def fall(self):
        for x in range((self.rect[1] + self.rect[3]) // tile_height, height // tile_height):
            if (Platforms.generate_level(Platforms.load_level('first_level.txt'), self.rect[0] // tile_width,
                                         x) or
                    Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                             (self.rect[0] + self.rect[2]) // tile_width, x)):
                self.landing = (x - 2) * tile_height + 10
                break
        if self.rect.y + self.jump_count ** 2 // 2 <= self.landing:
            self.rect.y += self.jump_count ** 2 // 2
        else:
            self.rect.y = self.landing
            self.if_jump = False
        self.jump_count += 1

    def update(self):
        global money
        if self.if_jump:
            self.fall()
        if self.time + 14 < i:
            self.kill()
        if len(pygame.sprite.spritecollide(self, person_sprites, False)) >= 1:
            money += 30
            if soundPlay:
                sound = pygame.mixer.Sound('sounds/coin.wav')
                sound.play()
            self.kill()


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tile_sprites, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class Platforms(pygame.sprite.Sprite):
    def load_level(filename):
        filename = "data/" + filename
        # читаем уровень, убирая символы перевода строки
        with open(filename, 'r') as mapFile:
            level_map = [line.strip() for line in mapFile]

        # и подсчитываем максимальную длину
        max_width = max(map(len, level_map))

        # дополняем каждую строку пустыми клетками ('.')
        return list(map(lambda x: x.ljust(max_width, '.'), level_map))

    def generate_level(level, x=None, y=None):
        if x == None and y == None:  # отрисовка уровня
            for y in range(len(level)):
                for x in range(len(level[y])):
                    if level[y][x] == '#':
                        Tile(choice(['plat_u1', 'plat_u2', 'plat_u3']), x, y)
                    elif level[y][x] == '@':
                        Tile(choice(['plat_d1', 'plat_d2', 'plat_d3']), x, y)
            # вернем размер поля в клетках
            return x, y
        else:  # проверка наличия тайла
            if x > 19:
                x = 19
            if y > 51:
                y = 51
            if level[y][x] == '#' or level[y][x] == '@':
                return True
            else:
                return False


con = sqlite3.connect('table.db')
cur = con.cursor()
res1 = int(str(cur.execute("SELECT result FROM leaderboard WHERE id = 1").fetchall()[0])[1:-2])
res2 = int(str(cur.execute("SELECT result FROM leaderboard WHERE id = 2").fetchall()[0])[1:-2])
res3 = int(str(cur.execute("SELECT result FROM leaderboard WHERE id = 3").fetchall()[0])[1:-2])
res4 = int(str(cur.execute("SELECT result FROM leaderboard WHERE id = 4").fetchall()[0])[1:-2])
res5 = int(str(cur.execute("SELECT result FROM leaderboard WHERE id = 5").fetchall()[0])[1:-2])


def leaderboard(kill):
    global res1, res2, res3, res4, res5, win
    if kill >= res3:
        if kill >= res1:
            res5 = res4
            res4 = res3
            res3 = res2
            res2 = res1
            res1 = kill
            win = 1
        elif kill >= res2:
            res5 = res4
            res4 = res3
            res3 = res2
            res2 = kill
            win = 2
        else:
            res5 = res4
            res4 = res3
            res3 = kill
            win = 3
    else:
        if kill >= res4:
            res5 = res4
            res4 = kill
            win = 4
        elif kill >= res5:
            res5 = kill
            win = 5
    cur.execute("UPDATE leaderboard SET result = ? WHERE id = 1",
                (str(res1),))
    cur.execute("UPDATE leaderboard SET result = ? WHERE id = 2",
                (str(res2),))
    cur.execute("UPDATE leaderboard SET result = ? WHERE id = 3",
                (str(res3),))
    cur.execute("UPDATE leaderboard SET result = ? WHERE id = 4",
                (str(res4),))
    cur.execute("UPDATE leaderboard SET result = ? WHERE id = 5",
                (str(res5),))
    con.commit()
    return res1, res2, res3, res4, res5, win


tile_width = 64
tile_height = 20  # размер клетки


def clickButton():
    if soundPlay:
        soundBut1 = pygame.mixer.Sound('sounds/button1.wav')  # звук кнопки 1
        soundBut1.play()


def gameInterface():
    back = LoadImage.load_image('back_interf.png', 'data')
    interf = LoadImage.load_image('interface.png', 'data')
    hpI = LoadImage.load_image('hp.png', 'data')
    bulI = LoadImage.load_image('bullets.png', 'data')
    screen.blit(back, [0, 0, 1280, 1024])
    if pers.hp > 0:
        screen.blit(pygame.transform.scale(hpI, (round(108 / pers.fullHP * pers.hp), 12)), [140, 965, 108 // pers.fullHP * pers.hp, 12])
    if pers.shop > 0:
        screen.blit(pygame.transform.scale(bulI, (round(108 / pers.fullBul * pers.shop), 12)),
                    [140, 1005, 108 // pers.fullBul * pers.shop, 12])

    screen.blit(interf, [0, 0, 1280, 1024])
    if weapon == 'm4a1s':
        screen.blit(LoadImage.load_image('m4inter.png', 'data'), [15, 965, 108, 40])
    else:
        screen.blit(LoadImage.load_image('sginter.png', 'data'), [15, 965, 108, 40])


def shop():
    global HP, speed, power, blood, running
    HPup = False
    sq = LoadImage.load_image('square.png', 'data')
    pospos = (0, 0)
    dontdaung = True
    but_exit = Button.Button(40, 900, 180, 70)
    but_back = Button.Button(400, 900, 180, 70)
    but_on1 = Button.Button(270, 200, 120, 62)
    but_on2 = Button.Button(270, 350, 120, 62)
    but_on3 = Button.Button(270, 500, 120, 62)
    but_off1 = Button.Button(470, 200, 120, 62)
    but_off2 = Button.Button(470, 350, 120, 62)
    but_off3 = Button.Button(470, 500, 120, 62)
    but_buy_SG = Button.Button(922, 354, 100, 40)
    but_red_plus = Button.Button(1200, 630, 27, 27)
    but_red_minus = Button.Button(900, 630, 27, 27)
    but_blue_plus = Button.Button(1200, 740, 27, 27)
    but_blue_minus = Button.Button(900, 740, 27, 27)
    but_green_plus = Button.Button(1200, 850, 27, 27)
    but_green_minus = Button.Button(900, 850, 27, 27)
    shopping = True
    shopim = LoadImage.load_image('shop.png', 'data')
    screen.blit(shopim, (0, 0, 1280, 1024))
    global sg, money, soundPlay
    while shopping:
        pygame.time.delay(300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    shopping = False
                    if dontdaung:
                        pers.hp = pers.fullHP
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if but_exit.clicked(event.pos, LoadImage.load_image('butEXIT_a.png', 'data')):
                        clickButton()
                        shopping = False
                        running = False
                        global person_sprites, all_sprites, tile_sprites, bullet_sprites, enemy_sprites, particle_sprites, aid_sprites, coin_sprites

                        for y in [person_sprites, all_sprites, tile_sprites, bullet_sprites, enemy_sprites, particle_sprites, aid_sprites, coin_sprites]:
                            for j in y:
                                j.kill()
                                j.remove()
                        global dead
                        dead = False

                    else:
                        but_exit.clicked(event.pos, LoadImage.load_image('butEXIT_na.png', 'data'))
                    if but_back.clicked(event.pos, LoadImage.load_image('butBACK_a.png', 'data')):
                        shopping = False
                        clickButton()
                        if dontdaung:
                            pers.hp = pers.fullHP
                    else:
                        but_back.clicked(event.pos, LoadImage.load_image('butBACK_na.png', 'data'))
                    if but_on1.clicked(event.pos, LoadImage.load_image('but_on_a.png', 'data')):
                        clickButton()
                        soundPlay = True
                    else:
                        but_on1.clicked(event.pos, LoadImage.load_image('but_on_na.png', 'data'))
                    if but_on2.clicked(event.pos, LoadImage.load_image('but_on_a.png', 'data')):
                        clickButton()
                        pygame.mixer.music.load('sounds\music.mp3')
                        pygame.mixer.music.play(100000)
                    else:
                        but_on2.clicked(event.pos, LoadImage.load_image('but_on_na.png', 'data'))
                    if but_on3.clicked(event.pos, LoadImage.load_image('but_on_a.png', 'data')):
                        clickButton()
                        blood = True
                    else:
                        but_on3.clicked(event.pos, LoadImage.load_image('but_on_na.png', 'data'))
                    if but_off1.clicked(event.pos, LoadImage.load_image('but_off_a.png', 'data')):
                        clickButton()
                        soundPlay = False
                    else:
                        but_off1.clicked(event.pos, LoadImage.load_image('but_off_na.png', 'data'))
                    if but_off2.clicked(event.pos, LoadImage.load_image('but_off_a.png', 'data')):
                        clickButton()
                        pygame.mixer.music.stop()
                    else:
                        but_off2.clicked(event.pos, LoadImage.load_image('but_off_na.png', 'data'))
                    if but_off3.clicked(event.pos, LoadImage.load_image('but_off_a.png', 'data')):
                        clickButton()
                        blood = False
                    else:
                        but_off3.clicked(event.pos, LoadImage.load_image('but_off_na.png', 'data'))
                    if but_green_plus.clicked(event.pos, LoadImage.load_image('butPlusGreenA.png', 'data')):
                        if power < 4 and money >= 50 * (power + 1):
                            screen.blit(shopim, (0, 0, 1280, 1024))
                            money -= 50 * (power + 1)
                            power += 1
                        clickButton()
                    else:
                        but_green_plus.draw(screen, LoadImage.load_image('butPlusGreenNA.png', 'data'))
                    if but_green_minus.clicked(event.pos, LoadImage.load_image('butMinusGreenA.png', 'data')):
                        if power >= 1:
                            money += 25 * power
                            power -= 1
                        clickButton()
                    else:
                        but_green_minus.draw(screen, LoadImage.load_image('butMinusGreenNA.png', 'data'))
                    if but_blue_minus.clicked(event.pos, LoadImage.load_image('butMinusBlueA.png', 'data')):
                        if speed >= 1:
                            money += 25 * speed
                            speed -= 1
                        clickButton()
                    else:
                        but_blue_minus.draw(screen, LoadImage.load_image('butMinusBlueNA.png', 'data'))
                    if but_buy_SG.clicked(event.pos, LoadImage.load_image('buySGa.png', 'data')):
                        if money >= 150 and not sg:
                            money -= 150
                            sg = True
                            soundBut1 = pygame.mixer.Sound('sounds/buy_sg.wav')  # звук кнопки 1
                            soundBut1.play()
                    else:
                        but_buy_SG.draw(screen, LoadImage.load_image('buySGna.png', 'data'))
                    if but_red_plus.clicked(event.pos, LoadImage.load_image('butPlusRedA.png', 'data')):
                        if HP < 4 and money >= 50 * (HP + 1):
                            money -= 50 * (HP + 1)
                            screen.blit(shopim, (0, 0, 1280, 1024))
                            HP += 1
                            HPup = True
                            dontdaung = True
                        clickButton()
                    else:
                        but_red_plus.draw(screen, LoadImage.load_image('butPlusRedNA.png', 'data'))
                    if but_blue_plus.clicked(event.pos, LoadImage.load_image('butPlusBlueA.png', 'data')):
                        if speed < 4 and money >= 50 * (speed + 1):
                            screen.blit(shopim, (0, 0, 1280, 1024))
                            money -= 50 * speed
                            speed += 1
                        clickButton()
                    else:
                        but_blue_plus.draw(screen, LoadImage.load_image('butPlusBlueNA.png', 'data'))
                    if but_red_minus.clicked(event.pos, LoadImage.load_image('butMinusRedA.png', 'data')):
                        if HP >= 1:
                            money += 25 * HP
                            HP -= 1
                            HPup = True
                            dontdaung = False
                        clickButton()
                    else:
                        but_red_minus.draw(screen, LoadImage.load_image('butMinusRedNA.png', 'data'))
            elif event.type == pygame.MOUSEMOTION:
                if but_back.clicked(event.pos, LoadImage.load_image('butBACK_a.png', 'data')):
                    pass
                else:
                    but_back.clicked(event.pos, LoadImage.load_image('butBACK_na.png', 'data'))
                if but_exit.clicked(event.pos, LoadImage.load_image('butEXIT_a.png', 'data')):
                    pass
                else:
                    but_exit.clicked(event.pos, LoadImage.load_image('butEXIT_na.png', 'data'))
                if but_blue_minus.clicked(event.pos, LoadImage.load_image('butMinusBlueA.png', 'data')):
                    pass
                else:
                    but_blue_minus.draw(screen, LoadImage.load_image('butMinusBlueNA.png', 'data'))
                if but_green_plus.clicked(event.pos, LoadImage.load_image('butPlusGreenA.png', 'data')):
                    pass
                else:
                    but_green_plus.draw(screen, LoadImage.load_image('butPlusGreenNA.png', 'data'))
                if but_green_minus.clicked(event.pos, LoadImage.load_image('butMinusGreenA.png', 'data')):
                    pass
                else:
                    but_green_minus.draw(screen, LoadImage.load_image('butMinusGreenNA.png', 'data'))
                if but_blue_plus.clicked(event.pos, LoadImage.load_image('butPlusBlueA.png', 'data')):
                    pass
                else:
                    but_blue_plus.draw(screen, LoadImage.load_image('butPlusBlueNA.png', 'data'))
                if but_buy_SG.clicked(event.pos, LoadImage.load_image('buySGa.png', 'data')):
                    pass
                else:
                    but_buy_SG.draw(screen, LoadImage.load_image('buySGna.png', 'data'))
                if but_red_plus.clicked(event.pos, LoadImage.load_image('butPlusRedA.png', 'data')):
                    pass
                else:
                    but_red_plus.draw(screen, LoadImage.load_image('butPlusRedNA.png', 'data'))
                if but_red_minus.clicked(event.pos, LoadImage.load_image('butMinusRedA.png', 'data')):
                    pass
                else:
                    but_red_minus.draw(screen, LoadImage.load_image('butMinusRedNA.png', 'data'))
                if but_on1.clicked(event.pos, LoadImage.load_image('but_on_a.png', 'data')):
                    pass
                else:
                    but_on1.clicked(event.pos, LoadImage.load_image('but_on_na.png', 'data'))
                if but_on2.clicked(event.pos, LoadImage.load_image('but_on_a.png', 'data')):
                    pass
                else:
                    but_on2.clicked(event.pos, LoadImage.load_image('but_on_na.png', 'data'))
                if but_on3.clicked(event.pos, LoadImage.load_image('but_on_a.png', 'data')):
                    pass
                else:
                    but_on3.clicked(event.pos, LoadImage.load_image('but_on_na.png', 'data'))
                if but_off1.clicked(event.pos, LoadImage.load_image('but_off_a.png', 'data')):
                    pass
                else:
                    but_off1.clicked(event.pos, LoadImage.load_image('but_off_na.png', 'data'))
                if but_off2.clicked(event.pos, LoadImage.load_image('but_off_a.png', 'data')):
                    pass
                else:
                    but_off2.clicked(event.pos, LoadImage.load_image('but_off_na.png', 'data'))
                if but_off3.clicked(event.pos, LoadImage.load_image('but_off_a.png', 'data')):
                    pass
                else:
                    but_off3.clicked(event.pos, LoadImage.load_image('but_off_na.png', 'data'))
                pospos = event.pos
            if but_back.clicked(pospos, LoadImage.load_image('butBACK_a.png', 'data')):
                pass
            else:
                but_back.draw(screen, LoadImage.load_image('butBACK_na.png', 'data'))
            if but_exit.clicked(pospos, LoadImage.load_image('butEXIT_a.png', 'data')):
                pass
            else:
                but_exit.draw(screen, LoadImage.load_image('butEXIT_na.png', 'data'))
            if but_on1.clicked(pospos, LoadImage.load_image('but_on_a.png', 'data')):
                pass
            else:
                but_on1.draw(screen, LoadImage.load_image('but_on_na.png', 'data'))
            if but_on2.clicked(pospos, LoadImage.load_image('but_on_a.png', 'data')):
                pass
            else:
                but_on2.draw(screen, LoadImage.load_image('but_on_na.png', 'data'))
            if but_on3.clicked(pospos, LoadImage.load_image('but_on_a.png', 'data')):
                pass
            else:
                but_on3.draw(screen, LoadImage.load_image('but_on_na.png', 'data'))
            if but_off1.clicked(pospos, LoadImage.load_image('but_off_a.png', 'data')):
                pass
            else:
                but_off1.draw(screen, LoadImage.load_image('but_off_na.png', 'data'))
            if but_off2.clicked(pospos, LoadImage.load_image('but_off_a.png', 'data')):
                pass
            else:
                but_off2.draw(screen, LoadImage.load_image('but_off_na.png', 'data'))
            if but_off3.clicked(pospos, LoadImage.load_image('but_off_a.png', 'data')):
                pass
            else:
                but_off3.draw(screen, LoadImage.load_image('but_off_na.png', 'data'))
            if but_blue_minus.clicked(pospos, LoadImage.load_image('butMinusBlueA.png', 'data')):
                pass
            else:
                but_blue_minus.draw(screen, LoadImage.load_image('butMinusBlueNA.png', 'data'))
            if but_green_plus.clicked(pospos, LoadImage.load_image('butPlusGreenA.png', 'data')):
                pass
            else:
                but_green_plus.draw(screen, LoadImage.load_image('butPlusGreenNA.png', 'data'))
            if but_green_minus.clicked(pospos, LoadImage.load_image('butMinusGreenA.png', 'data')):
                pass
            else:
                but_green_minus.draw(screen, LoadImage.load_image('butMinusGreenNA.png', 'data'))
            if but_red_minus.clicked(pospos, LoadImage.load_image('butMinusRedA.png', 'data')):
                pass
            else:
                but_red_minus.draw(screen, LoadImage.load_image('butMinusRedNA.png', 'data'))
            if but_blue_plus.clicked(pospos, LoadImage.load_image('butPlusBlueA.png', 'data')):
                pass
            else:
                but_blue_plus.draw(screen, LoadImage.load_image('butPlusBlueNA.png', 'data'))
            if but_buy_SG.clicked(pospos, LoadImage.load_image('buySGa.png', 'data')):
                pass
            else:
                but_buy_SG.draw(screen, LoadImage.load_image('buySGna.png', 'data'))
            if but_red_plus.clicked(pospos, LoadImage.load_image('butPlusRedA.png', 'data')):
                pass
            else:
                but_red_plus.draw(screen, LoadImage.load_image('butPlusRedNA.png', 'data'))
        for h in range(4 - HP):
            screen.blit(sq, [1286 - 40 - 75 * (h + 1), 575, 75, 40])
        for sp in range(4 - speed):
            screen.blit(sq, [1286 - 40 - 75 * (sp + 1), 675, 75, 40])
        for pow in range(4 - power):
            screen.blit(sq, [1286 - 40 - 75 * (pow + 1), 785, 75, 40])
        if HPup:
            pers.fullHP = 200 + HP * 25

            HPup = False
        pers.speed = 10 + speed * 2
        global Power
        Power = 10 + power * 5
        pygame.display.flip()


def main():  # главная функция
    global time_wave, i, kill, res1, res2, res3, res4, res5, running
    level_x, level_y = Platforms.generate_level(Platforms.load_level('first_level.txt'))
    clock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT, 1000)  # Таймер с переодичностью в секунду
    ii = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT:
                i += 1
                if i in time_wave:
                    wave()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    shop()
                elif event.key == pygame.K_SPACE:
                    global dead
                    global wave_count
                    if dead:
                        dead = False
                        for y in enemy_sprites:
                            enemy_sprites.remove(y)  # удаление ненужных элементов
                        for y in aid_sprites:
                            aid_sprites.remove(y)
                        for y in coin_sprites:
                            coin_sprites.remove(y)
                        kill = 0
                        i = ii = 0
                        start()
                elif event.key == pygame.K_u:
                    if dead:
                        try:
                            webbrowser.open(f'http://webquietcry.herokuapp.com/addRecord/{web}', new=2)
                        except:
                            webbrowser.open(f'http://webquietcry.herokuapp.com/addRecord/0', new=2)
                elif event.key == pygame.K_q:
                    global weapon
                    if weapon == 'm4a1s' and sg:
                        weapon = 'ShotGun'
                    else:
                        weapon = 'm4a1s'
                elif event.key == pygame.K_p:  # пауза
                    start_screen('чтобы продолжить')
                elif event.key == pygame.K_TAB:
                    res1, res2, res3, res4, res5 = 0, 0, 0, 0, 0
        fon = LoadImage.load_image('fon_b.png', 'data')
        global iWave
        if not dead:
            screen.blit(fon, (0, 0, 1280, 1024))
            font = pygame.font.Font(None, 50)
            if iWave is not None:
                if i - iWave <= 2:
                    screen.blit(textWave, [520, 200])
            font = pygame.font.Font(None, 50)
            text2 = font.render(f"Баланс: {money}", True, [100, 100, 100])
            screen.blit(text2, [50, 80])
            person_sprites.draw(screen)
            bullet_sprites.draw(screen)
            aid_sprites.draw(screen)
            tile_sprites.draw(screen)
            coin_sprites.draw(screen)
            particle_sprites.draw(screen)
            enemy_sprites.draw(screen)  # Отображение всех спрайтов
            person_sprites.update(i)
            coin_sprites.update()
            aid_sprites.update()
            bullet_sprites.update()
            enemy_sprites.update()
            particle_sprites.update()
            gameInterface()
        else:
            screen.blit(fon, (0, 0, 1280, 1024))
            font = pygame.font.Font(None, 110)
            text1 = font.render("Умер насмерть(", True, [100, 0, 0])
            font = pygame.font.Font(None, 65)
            text2 = font.render("Чтобы выйти в меню нажмите \"пробел\"", True, [100, 100, 100])
            text3 = font.render("Таблица рекордов:", True, [0, 0, 150])
            text4 = font.render("Чтобы загрузить результат на веб-сайт нажмите \"U\"", True, [80, 80, 80])
            # Вывести сделанную картинку на экран в точке (300, 300)
            screen.blit(text1, [360, 200])
            screen.blit(text2, [200, 290])
            screen.blit(text3, [360, 430])
            screen.blit(text4, [80, 360])
            a, b, c, d, e, label = leaderboard(kill)
            if kill > -1:
                web = kill
            if label:
                font = pygame.font.Font(None, 100)
                if label == 1:
                    lb = font.render("Вы заняли 1-ое место", True, [255, 255, 0])
                elif label == 2:
                    lb = font.render("Вы заняли 2-ое место", True, [113, 125, 130])
                elif label == 3:
                    lb = font.render("Вы заняли 3-ье место", True, [205, 127, 50])
                elif label == 4:
                    lb = font.render("Вы заняли 4-ое место", True, [0, 0, 0])
                else:
                    lb = font.render("Вы заняли 5-ое место", True, [0, 0, 0])
                screen.blit(lb, [265, 50])
            font = pygame.font.Font(None, 50)
            l1 = font.render('1. ' + str(a), True, [0, 0, 0])
            screen.blit(l1, [490, 500])
            l2 = font.render('2. ' + str(b), True, [0, 0, 0])
            screen.blit(l2, [490, 550])
            l3 = font.render('3. ' + str(c), True, [0, 0, 0])
            screen.blit(l3, [490, 600])
            l4 = font.render('4. ' + str(d), True, [0, 0, 0])
            screen.blit(l4, [490, 650])
            l5 = font.render('5. ' + str(e), True, [0, 0, 0])
            screen.blit(l5, [490, 700])
            wave_count = 0
            kill = -1

        # Обновление спрайтов
        clock.tick(60)
        pygame.display.flip()


def settings():
    global blood
    but_exit = Button.Button(40, 900, 180, 70)
    but_on1 = Button.Button(270, 200, 120, 62)
    but_on2 = Button.Button(270, 350, 120, 62)
    but_on3 = Button.Button(270, 500, 120, 62)
    but_off1 = Button.Button(470, 200, 120, 62)
    but_off2 = Button.Button(470, 350, 120, 62)
    but_off3 = Button.Button(470, 500, 120, 62)
    settingsO = True
    settingsim = LoadImage.load_image('settings.png', 'data')
    screen.blit(settingsim, (0, 0, 1280, 1024))
    pospos = (0, 0)
    global soundPlay
    while settingsO:
        pygame.time.delay(300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    settingsO = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if but_exit.clicked(event.pos, LoadImage.load_image('butEXIT_a.png', 'data')):
                        clickButton()
                        settingsO = False
                    else:
                        but_exit.clicked(event.pos, LoadImage.load_image('butEXIT_na.png', 'data'))
                    if but_on1.clicked(event.pos, LoadImage.load_image('but_on_a.png', 'data')):
                        clickButton()
                        soundPlay = True
                    else:
                        but_on1.clicked(event.pos, LoadImage.load_image('but_on_na.png', 'data'))
                    if but_on2.clicked(event.pos, LoadImage.load_image('but_on_a.png', 'data')):
                        clickButton()
                        pygame.mixer.music.load('sounds\music.mp3')
                        pygame.mixer.music.play(100000)
                    else:
                        but_on2.clicked(event.pos, LoadImage.load_image('but_on_na.png', 'data'))
                    if but_on3.clicked(event.pos, LoadImage.load_image('but_on_a.png', 'data')):
                        clickButton()
                        blood = True
                    else:
                        but_on3.clicked(event.pos, LoadImage.load_image('but_on_na.png', 'data'))
                    if but_off1.clicked(event.pos, LoadImage.load_image('but_off_a.png', 'data')):
                        clickButton()
                        soundPlay = False
                    else:
                        but_off1.clicked(event.pos, LoadImage.load_image('but_off_na.png', 'data'))
                    if but_off2.clicked(event.pos, LoadImage.load_image('but_off_a.png', 'data')):
                        clickButton()
                        pygame.mixer.music.stop()
                    else:
                        but_off2.clicked(event.pos, LoadImage.load_image('but_off_na.png', 'data'))
                    if but_off3.clicked(event.pos, LoadImage.load_image('but_off_a.png', 'data')):
                        clickButton()
                        blood = False
                    else:
                        but_off3.clicked(event.pos, LoadImage.load_image('but_off_na.png', 'data'))
            elif event.type == pygame.MOUSEMOTION:
                if but_exit.clicked(event.pos, LoadImage.load_image('butEXIT_a.png', 'data')):
                    pass
                else:
                    but_exit.clicked(event.pos, LoadImage.load_image('butEXIT_na.png', 'data'))
                if but_on1.clicked(event.pos, LoadImage.load_image('but_on_a.png', 'data')):
                    pass
                else:
                    but_on1.clicked(event.pos, LoadImage.load_image('but_on_na.png', 'data'))
                if but_on2.clicked(event.pos, LoadImage.load_image('but_on_a.png', 'data')):
                    pass
                else:
                    but_on2.clicked(event.pos, LoadImage.load_image('but_on_na.png', 'data'))
                if but_on3.clicked(event.pos, LoadImage.load_image('but_on_a.png', 'data')):
                    pass
                else:
                    but_on3.clicked(event.pos, LoadImage.load_image('but_on_na.png', 'data'))
                if but_off1.clicked(event.pos, LoadImage.load_image('but_off_a.png', 'data')):
                    pass
                else:
                    but_off1.clicked(event.pos, LoadImage.load_image('but_off_na.png', 'data'))
                if but_off2.clicked(event.pos, LoadImage.load_image('but_off_a.png', 'data')):
                    pass
                else:
                    but_off2.clicked(event.pos, LoadImage.load_image('but_off_na.png', 'data'))
                if but_off3.clicked(event.pos, LoadImage.load_image('but_off_a.png', 'data')):
                    pass
                else:
                    but_off3.clicked(event.pos, LoadImage.load_image('but_off_na.png', 'data'))
                pospos = event.pos
            if but_exit.clicked(pospos, LoadImage.load_image('butEXIT_a.png', 'data')):
                pass
            else:
                but_exit.draw(screen, LoadImage.load_image('butEXIT_na.png', 'data'))
            if but_on1.clicked(pospos, LoadImage.load_image('but_on_a.png', 'data')):
                pass
            else:
                but_on1.draw(screen, LoadImage.load_image('but_on_na.png', 'data'))
            if but_on2.clicked(pospos, LoadImage.load_image('but_on_a.png', 'data')):
                pass
            else:
                but_on2.draw(screen, LoadImage.load_image('but_on_na.png', 'data'))
            if but_on3.clicked(pospos, LoadImage.load_image('but_on_a.png', 'data')):
                pass
            else:
                but_on3.draw(screen, LoadImage.load_image('but_on_na.png', 'data'))
            if but_off1.clicked(pospos, LoadImage.load_image('but_off_a.png', 'data')):
                pass
            else:
                but_off1.draw(screen, LoadImage.load_image('but_off_na.png', 'data'))
            if but_off2.clicked(pospos, LoadImage.load_image('but_off_a.png', 'data')):
                pass
            else:
                but_off2.draw(screen, LoadImage.load_image('but_off_na.png', 'data'))
            if but_off3.clicked(pospos, LoadImage.load_image('but_off_a.png', 'data')):
                pass
            else:
                but_off3.draw(screen, LoadImage.load_image('but_off_na.png', 'data'))
        pygame.display.flip()


class Menu:
    def __init__(self):
        self.butNewG = Button.Button(992, 738, 124, 19)
        self.butLoadG = Button.Button(992, 760, 124, 19)
        self.butSurv = Button.Button(992, 782, 124, 19)
        self.butSettings = Button.Button(992, 804, 124, 19)
        self.butExit = Button.Button(992, 826, 124, 19)

    def updateClicked(self, pos):
        clickButton()
        if self.butExit.clicked(pos, LoadImage.load_image('Exit_a.png', 'data')):
            quit()
        else:
            self.butExit.draw(screen, LoadImage.load_image('Exit_na.png', 'data'))
        if self.butSurv.clicked(pos, LoadImage.load_image('Surv_a.png', 'data')):
            return 'StartSurv'
        else:
            self.butSurv.draw(screen, LoadImage.load_image('Surv_na.png', 'data'))
        if self.butSettings.clicked(pos, LoadImage.load_image('Settings_a.png', 'data')):
            return 'Settings'
        else:
            self.butSettings.draw(screen, LoadImage.load_image('Settings_na.png', 'data'))

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
                MenuOpen = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if menu.updateClicked(event.pos) == 'StartSurv':
                        start()
                        main()
                    if menu.updateClicked(event.pos) == 'Settings':
                        settings()
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
# Загрузка музыки
pygame.mixer.music.load('sounds/music.mp3')
pygame.mixer.music.play(100000)
pygame.mixer.music.set_volume(0.5)


con.close()
pygame.display.quit()
pygame.quit()
sys.exit(0)
