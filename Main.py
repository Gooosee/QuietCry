import pygame
from random import choice
import LoadImage

pygame.init()
# создание окна
size = width, height = 840, 840
screen = pygame.display.set_mode(size)
f = False

personRun = [LoadImage.load_image('anim1_person_run_m4a1s.png', 'data'),
             LoadImage.load_image('anim2_person_run_m4a1s.png', 'data'),
             LoadImage.load_image('anim3_person_run_m4a1s.png', 'data')]

personRunLeft = [pygame.transform.flip(personRun[0], True, False),
                 pygame.transform.flip(personRun[1], True, False),
                 pygame.transform.flip(personRun[2], True, False)]

personJump = [LoadImage.load_image('anim1_person_jump_m4a1s.png', 'data'),
              LoadImage.load_image('anim2_person_jump_m4a1s.png', 'data'),
              LoadImage.load_image('anim3_person_jump_m4a1s.png', 'data'),
              LoadImage.load_image('anim4_person_jump_m4a1s.png', 'data'),
              LoadImage.load_image('anim5_person_jump_m4a1s.png', 'data'),
              LoadImage.load_image('anim6_person_jump_m4a1s.png', 'data')]

personJumpLeft = [pygame.transform.flip(personJump[0], True, False),
                  pygame.transform.flip(personJump[1], True, False),
                  pygame.transform.flip(personJump[2], True, False),
                  pygame.transform.flip(personJump[3], True, False),
                  pygame.transform.flip(personJump[4], True, False),
                  pygame.transform.flip(personJump[5], True, False)]

personFire = [LoadImage.load_image('anim1_person_fire_m4a1s.png', 'data'),
              LoadImage.load_image('anim2_person_fire_m4a1s.png', 'data'),
              LoadImage.load_image('anim3_person_fire_m4a1s.png', 'data'),
              LoadImage.load_image('anim4_person_fire_m4a1s.png', 'data'),
              LoadImage.load_image('anim2_person_fire_m4a1s.png', 'data'),
              LoadImage.load_image('anim3_person_fire_m4a1s.png', 'data'),
              LoadImage.load_image('anim4_person_fire_m4a1s.png', 'data'),
              LoadImage.load_image('anim2_person_fire_m4a1s.png', 'data'),
              LoadImage.load_image('anim3_person_fire_m4a1s.png', 'data')]

personFireLeft = [pygame.transform.flip(personFire[0], True, False),
                  pygame.transform.flip(personFire[1], True, False),
                  pygame.transform.flip(personFire[2], True, False),
                  pygame.transform.flip(personFire[3], True, False),
                  pygame.transform.flip(personFire[4], True, False),
                  pygame.transform.flip(personFire[5], True, False),
                  pygame.transform.flip(personFire[6], True, False),
                  pygame.transform.flip(personFire[7], True, False),
                  pygame.transform.flip(personFire[8], True, False)]

personStop = [LoadImage.load_image('anim1_person_stop_m4a1s.png', 'data'),
              LoadImage.load_image('anim2_person_stop_m4a1s.png', 'data'),
              LoadImage.load_image('anim3_person_stop_m4a1s.png', 'data'),
              LoadImage.load_image('anim4_person_stop_m4a1s.png', 'data')]

personStopLeft = [pygame.transform.flip(personStop[0], True, False),
                  pygame.transform.flip(personStop[1], True, False),
                  pygame.transform.flip(personStop[2], True, False),
                  pygame.transform.flip(personStop[3], True, False)]

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

bull = LoadImage.load_image('bullet.png', 'data')
person_sprites = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
tile_sprites = pygame.sprite.Group()
bullet_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()


def start_screen():
    delay = 0
    text1 = "Quiet Cry"
    fon = pygame.transform.scale(LoadImage.load_image('fon1.png', 'data'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 100)
    string_rendered = font.render(text1, 1, pygame.Color('black'))
    intro_rect = string_rendered.get_rect()
    intro_rect.y = 50
    intro_rect.x = 250
    screen.blit(string_rendered, intro_rect)

    while True:
        delay += 1
        if delay % 5 == 0:
            text2 = "Нажмите любую кнопку"
        else:
            text1, text2 = "Quiet Cry", ""
            fon = pygame.transform.scale(LoadImage.load_image('fon1.png', 'data'), (width, height))
            screen.blit(fon, (0, 0))
            font = pygame.font.Font(None, 100)
            string_rendered = font.render(text1, 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            intro_rect.y = 50
            intro_rect.x = 250
            screen.blit(string_rendered, intro_rect)
        font = pygame.font.Font(None, 50)
        string_rendered = font.render(text2, 1, pygame.Color('green'))
        intro_rect = string_rendered.get_rect()
        intro_rect.y = 750
        intro_rect.x = 200
        screen.blit(string_rendered, intro_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        pygame.time.Clock().tick(5)


start_screen()


class Person(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(person_sprites)
        # Начальные координаты персонажа
        self.pos_x = x
        self.hp = 150
        self.jump_count = 10
        self.re20 = False
        self.pos_y = y
        self.sdvig = False
        self.landing = 505  # координата приземления при запрыгивание на платформу
        self.if_jump = False
        self.direction = False
        self.cur_frame = 0  # Номер кадра
        self.frames = personStop  # Анимация стоя
        self.image = personStop[self.cur_frame]  # Изображение спрайта
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.pos_x, self.pos_y)

    def run(self, keys):  # Бег
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction = True  # Персонаж смотрит влево
            self.frames = personRunLeft

            if (Platforms.generate_level(Platforms.load_level('first_level.txt'), self.rect[0] // 105,
                                         (self.rect[1] + self.rect[3]) // 21) or
                    Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                             (self.rect[0] + self.rect[2]) // 105, (self.rect[1] + self.rect[3]) // 21)
                    and not (self.if_jump)):
                self.rect.x -= 10  # Смещение влево
            elif self.if_jump:
                self.rect.x -= 10
            else:
                for i in range((self.rect[1] + self.rect[3]) // 21, 40):
                    if (Platforms.generate_level(Platforms.load_level('first_level.txt'), self.rect[0] // 105, i) or
                            Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                                     (self.rect[0] + self.rect[2]) // 105, i)):
                        self.rect.y = (i - 4) * 21
                        break
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction = False  # Персонаж смотрит вправо
            self.frames = personRun
            if (Platforms.generate_level(Platforms.load_level('first_level.txt'), self.rect[0] // 105,
                                         (self.rect[1] + self.rect[3]) // 21) or
                    Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                             (self.rect[0] + self.rect[2]) // 105, (self.rect[1] + self.rect[3]) // 21)
                    and not (self.if_jump)):
                self.rect.x += 10  # Смещение вправо
            elif self.if_jump:
                self.rect.x += 10
            else:
                for i in range((self.rect[1] + self.rect[3]) // 21, 40):
                    if (Platforms.generate_level(Platforms.load_level('first_level.txt'), self.rect[0] // 105, i) or
                            Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                                     (self.rect[0] + self.rect[2]) // 105, i)):
                        self.rect.y = (i - 4) * 21
                        break

    def stop(self):  # Отсутствие движения
        if self.direction:
            self.frames = personStopLeft
        else:
            self.frames = personStop

    def jump(self):  # Прыжок
        if self.direction:
            self.frames = personJumpLeft[:1]
        else:
            self.frames = personJump[:1]
        if self.jump_count > 0:
            if self.direction:
                self.frames = personJumpLeft[2:3]
            else:
                self.frames = personJump[2:3]
            if not (Platforms.generate_level(Platforms.load_level('first_level.txt'), self.rect[0] // 105,
                                             (self.rect[1] // 21)) or
                    Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                             (self.rect[0] + self.rect[2]) // 105, (self.rect[1] // 21))):
                self.rect.y -= self.jump_count ** 2 // 2
                self.jump_count -= 1
            else:
                self.jump_count += 1
                self.jump_count *= -1
        else:
            if self.direction:
                self.frames = personJumpLeft[3:4]
            else:
                self.frames = personJump[3:4]
            for i in range((self.rect[1] + self.rect[3]) // 21, 40):
                if (Platforms.generate_level(Platforms.load_level('first_level.txt'), self.rect[0] // 105, i) or
                        Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                                 (self.rect[0] + self.rect[2]) // 105, i)):
                    self.landing = (i - 8) * 21 - 6
                    break
            if self.rect.y + self.jump_count ** 2 // 2 <= self.landing:
                self.rect.y += self.jump_count ** 2 // 2
            else:
                self.rect.y = self.landing
            self.jump_count -= 1
        if self.jump_count == -10:
            if self.direction:
                self.frames = personJumpLeft[5:]
            else:
                self.frames = personJump[5:]
            self.if_jump = False
            self.re20 = True
            self.rect.y += 35

    def fire(self):  # Стрельба
        if self.direction:
            self.frames = personFireLeft
        else:
            self.frames = personFire
        if self.cur_frame in [2, 4, 6]:  # Стрельба очерядями, в момент соответствующих кадров
            bul = Bullet(self.rect.x + 110, self.rect.y + 36, self.direction)  # Создание пули

    def update(self):
        if self.hp <= 0:
            global dead
            dead = True
            self.kill()
        running = False
        keys = pygame.key.get_pressed()  # в этом списке лежат все нажатые кнопки
        if self.re20:
            self.rect.y += 55
            self.re20 = False
        if keys[pygame.K_RIGHT] or keys[pygame.K_a] or keys[pygame.K_LEFT] or keys[pygame.K_d]:  # Нажаты клавиши для
            # бега
            self.run(keys)
            if self.direction:
                self.sdvig = True
            elif self.sdvig:
                self.sdvig = False
                self.rect.x = self.rect.x - 40  # Выравнивание анимации
            running = True
        if not self.if_jump:
            if keys[pygame.K_UP] or keys[pygame.K_w]:  # Нажат прыжок
                self.if_jump = True
                self.landing = 505
                self.jump_count = 10
                self.rect.y -= 40
            elif keys[pygame.K_h] and not running:  # Нажатие клавиши "h" для стрельбы
                self.fire()

            elif not (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_d]):
                self.stop()  # отсутствие движения
        else:
            self.jump()

        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame - 1]


class Bullet(pygame.sprite.Sprite):  # Класс пуль
    def __init__(self, x, y, direction_bul):
        super().__init__(bullet_sprites)
        self.x, self.y, self.direction_bul = x, y, direction_bul
        self.image = bull  # Изображение пули
        self.rect = self.image.get_rect()
        if direction_bul:  # Проверка направления и смещение координаты появления пули
            self.x -= 115
        self.rect = self.rect.move(self.x, self.y)

    def update(self, *args):
        global f
        if not self.direction_bul:
            if self.rect.x <= 800:
                self.rect.x += 60
            else:
                self.kill()  # Уничтожение пуль вышедших за границы экрана
        else:
            if self.rect.x >= 0:
                self.rect.x -= 60
            else:
                self.kill()  # Уничтожение пуль вышедших за границы экрана
        if f:
            self.kill()
        f = False


class EnemyA(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(enemy_sprites)
        # Начальные координаты персонажа
        self.hp = 40
        self.pos_x = x
        self.pos_y = y
        self.running = False
        self.direction = False
        self.if_jump = False
        self.frames = enemyARun  # Анимация стоя
        self.cur_frame = 0  # Номер кадра
        self.image = enemyARun[self.cur_frame]  # Изображение спрайта
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.pos_x, self.pos_y + 15)

    def run(self):  # Бег
        if pers.rect.x < self.rect.x:
            self.frames = enemyARunLeft
            #self.rect.x = self.pos_x  # Выравнивание анимации
            if (Platforms.generate_level(Platforms.load_level('first_level.txt'), self.rect[0] // 105,
                                         (self.rect[1] + self.rect[3]) // 21) or
                    Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                             (self.rect[0] + self.rect[2]) // 105, (self.rect[1] + self.rect[3]) // 21)
                    and not (self.if_jump)):
                pass
            else:
                for i in range((self.rect[1] + self.rect[3]) // 21, 40):
                    if (Platforms.generate_level(Platforms.load_level('first_level.txt'), self.rect[0] // 105, i) or
                            Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                                     (self.rect[0] + self.rect[2]) // 105, i)):
                        self.rect.y = (i - 3) * 21
                        break  # Смещение влево
            self.rect.x -= 6
            self.direction = True  # Персонаж смотрит влево
        elif pers.rect.x > self.rect.x:
            self.frames = enemyARun
            if (Platforms.generate_level(Platforms.load_level('first_level.txt'), self.rect[0] // 105,
                                         (self.rect[1] + self.rect[3]) // 21) or
                    Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                             (self.rect[0] + self.rect[2]) // 105, (self.rect[1] + self.rect[3]) // 21)
                    and not (self.if_jump)):
                self.rect.x += 6  # Смещение вправо
            elif self.if_jump:
                self.rect.x += 6
            else:
                for i in range((self.rect[1] + self.rect[3]) // 21, 40):
                    if (Platforms.generate_level(Platforms.load_level('first_level.txt'), self.rect[0] // 105, i) or
                            Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                                     (self.rect[0] + self.rect[2]) // 105, i)):
                        self.rect.y = (i - 3) * 21
                        break
            self.direction = False  # Персонаж смотрит вправо

    def kick(self):
        if self.direction:
            self.frames = enemyAKickLeft
        else:
            self.frames = enemyAKick
        pers.hp -= 10

    def jump(self):  # Прыжок
        if self.direction:
            self.frames = enemyAJumpLeft[:1]
        else:
            self.frames = enemyAJump[:1]
        if self.jump_count > 0:
            if self.direction:
                self.frames = enemyAJumpLeft[2:3]
            else:
                self.frames = enemyAJump[2:3]
            if not (Platforms.generate_level(Platforms.load_level('first_level.txt'), self.rect[0] // 105,
                                             (self.rect[1] // 21)) or
                    Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                             (self.rect[0] + self.rect[2]) // 105, (self.rect[1] // 21))):
                self.rect.y -= self.jump_count ** 2 // 2
                self.jump_count -= 1
            else:
                self.jump_count += 1
                self.jump_count *= -1
        else:
            if self.direction:
                self.frames = enemyAJumpLeft[2:3]
            else:
                self.frames = enemyAJump[2:3]
            for i in range((self.rect[1] + self.rect[3]) // 21, 40):
                if (Platforms.generate_level(Platforms.load_level('first_level.txt'), self.rect[0] // 105, i) or
                        Platforms.generate_level(Platforms.load_level('first_level.txt'),
                                                 (self.rect[0] + self.rect[2]) // 105, i)):
                    self.landing = (i - 8) * 21 - 6
                    break
            if self.rect.y + self.jump_count ** 2 // 2 <= self.landing:
                self.rect.y += self.jump_count ** 2 // 2
            else:
                self.rect.y = self.landing
            self.jump_count -= 1
        if self.jump_count == -10:
            if self.direction:
                self.frames = enemyAJumpLeft[4:]
            else:
                self.frames = enemyAJump[4:]
            self.if_jump = False
            self.re20 = True
            self.rect.y += 105

    def update(self):
        global f
        if self.hp <= 0:
            self.kill()
        if abs(self.rect.x - pers.rect.x) > 70:  # Персонаж вне зоны досягаемости
            self.run()
            self.running = True  # Враг бежит
        if not self.if_jump:
            if abs(self.rect.x - pers.rect.x) <= 70 and abs(
                    - pers.rect.y + self.rect.y) <= 50 and not(self.running):  #
                self.kick()
            elif - pers.rect.y + self.rect.y > 150:  # Нажат прыжок
                self.if_jump = True
                self.jump_count = 10
        else:
            self.jump()
        if len(pygame.sprite.spritecollide(self, bullet_sprites, False)) >= 1:
            self.hp -= 10
            f = True
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame - 1]
        self.running = False  # Враг стоит


wave_count = 0  # Номер волны


def wave(i):
    global wave_count
    xxl = xxr = yyl = yyr = 20
    wave_count += 1
    for i in range(wave_count):
        if i % 4 == 0:
            en = EnemyA(-50 - xxl, 505)
            xxl += 40
        elif i % 4 == 1:
            en = EnemyA(850 + xxr, 505)
            xxr += 40
        elif i % 4 == 2:
            en = EnemyA(0, -10 - yyl)
            yyl += 40
        elif i % 4 == 3:
            en = EnemyA(840, -10 - yyr)
            yyr += 40


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
            if x > 7:
                x = 7
            if y > 39:
                y = 39
            if level[y][x] == '#' or level[y][x] == '@':
                return True
            else:
                return False


time_wave = [1, 20, 30, 40, 50, 60, 70, 80, 90, 100]
tile_width = 105
tile_height = 21  # размер клетки
dead = False
pers = Person(305, 670)  # Начальное положение персонажа
ii = 0


def main():  # главная функция
    global ii
    level_x, level_y = Platforms.generate_level(Platforms.load_level('first_level.txt'))
    clock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    i = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT:
                i += 1
                if i in time_wave:
                    wave(i)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    global dead
                    global wave_count
                    global pers
                    if dead:
                        dead = False
                        print(1)
                        for y in enemy_sprites:
                            enemy_sprites.remove(y)
                        pers = Person(305, 670)  # Начальное положение персонажа
                        ii = 0
                        wave_count = 0

        fon = LoadImage.load_image('fon1.png', 'data')
        if not dead:
            screen.blit(fon, [0, -80, 840, 840])
            person_sprites.draw(screen)
            bullet_sprites.draw(screen)
            tile_sprites.draw(screen)
            enemy_sprites.draw(screen)  # Отображение всех спрайтов
            person_sprites.update()
            bullet_sprites.update()
            enemy_sprites.update()  #
        else:
            print(1)

            if ii == 0:
                ii = i
            elif i - ii < 3:
                screen.blit(fon, [0, -80, 840, 840])
                person_sprites.draw(screen)
                bullet_sprites.draw(screen)
                tile_sprites.draw(screen)
                enemy_sprites.draw(screen)   # Отображение всех спрайтов
                person_sprites.update()
                bullet_sprites.update()
                enemy_sprites.update()  #
            else:
                screen.blit(fon, [0, 0, 840, 840])
                font = pygame.font.Font(None, 80)
                text1 = font.render("Умер насмерть(", True, [100, 0, 0])
                font = pygame.font.Font(None, 40)
                text2 = font.render("Чтобы начать заново нажмите \"пробел\"", True, [100, 100, 100])
                # Вывести сделанную картинку на экран в точке (300, 300)
                screen.blit(text1, [250, 350])
                screen.blit(text2, [220, 420])
        # Обновление спрайтов
        clock.tick(60)
        pygame.time.delay(50)
        pygame.display.flip()


# запуск главной функции
main()
quit()
