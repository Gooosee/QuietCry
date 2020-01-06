import pygame
import LoadImage

pygame.init()
# создание окна
size = width, height = 800, 800
screen = pygame.display.set_mode(size)

# Задержки для анимаций

waitStop = [100, 100, 100]  # Стоя
waitRun = [100, 100, 100]  # Набегу
waitJump = [100, 100, 100, 100, 100, 100]  # В прыжке
waitFire = [100, 100, 100, 100, 100, 100, 100, 100, 100]

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

bull = LoadImage.load_image('bullet.png', 'data')
person_sprites = pygame.sprite.GroupSingle()
all_sprites = pygame.sprite.Group()
tile_sprites = pygame.sprite.Group()
bullet_sprites = pygame.sprite.Group()
direction = False


class Person(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)
        # Начальные координаты персонажа
        self.pos_x = x
        self.re20 = False
        self.pos_y = y
        self.if_jump = False
        self.cur_frame = 0  # Номер кадра
        self.frames = personStop  # Анимация стоя
        self.num_wait = waitStop  # Задержки в анимации
        self.image = personStop[self.cur_frame]  # Изображение спрайта
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.pos_x, self.pos_y)  # Смещение в точку нахождения пули

    def run(self, keys):  # Бег
        global direction
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.frames = personRunLeft
            self.num_wait = waitRun
            self.rect.x = self.pos_x - 40  # Выравнивание анимации
            self.pos_x -= 8  # Смещение влево
            direction = True  # Персонаж смотрит влево
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.frames = personRun
            self.num_wait = waitRun
            self.pos_x += 8  # Смещение вправо
            direction = False  # Персонаж смотрит вправо
        self.rect.x = self.pos_x

    def stop(self):  # Отсутствие движения
        if direction:
            self.frames = personStopLeft
            self.num_wait = waitStop
        else:
            self.frames = personStop
            self.num_wait = waitStop

    def jump(self):  # Прыжок
        if direction:
            self.frames = personJumpLeft[:1]
            self.num_wait = waitJump[:1]
        else:
            self.frames = personJump[:1]
            self.num_wait = waitJump[:1]
        if self.jump_count > 0:
            if direction:
                self.frames = personJumpLeft[2:3]
                self.num_wait = waitJump[2:3]
            else:
                self.frames = personJump[2:3]
                self.num_wait = waitJump[2:3]
            self.rect.y -= self.jump_count ** 2 / 2
            self.jump_count -= 1
        else:
            if direction:
                self.frames = personJumpLeft[3:4]
                self.num_wait = waitJump[3:4]
            else:
                self.frames = personJump[3:4]
                self.num_wait = waitJump[3:4]
            self.rect.y += self.jump_count ** 2 / 2
            self.jump_count -= 1
        if self.jump_count == -10:
            if direction:
                self.frames = personJumpLeft[5:]
                self.num_wait = waitJump[5:]
            else:
                self.frames = personJump[5:]
                self.num_wait = waitJump[5:]
            self.if_jump = False
            self.re20 = True
            self.rect.y += 20

    def fire(self):  # Стрельба
        if direction:
            self.frames = personFireLeft
            self.rect.x = self.pos_x
            self.num_wait = waitFire
        else:
            self.frames = personFire
            self.rect.x = self.pos_x - 5  # Выравнивание
            self.num_wait = waitFire
        if self.cur_frame in [2, 4, 6]:  # Стрельба очерядями, в момент соответствующих кадров
            bul = Bullet(self.pos_x + 110, self.pos_y + 36, direction)  # Создание пули

    def wait(self):  # Задержка
        pygame.time.wait(self.num_wait[self.cur_frame - 1])

    def update(self):
        running = False
        keys = pygame.key.get_pressed()  # в этом списке лежат все нажатые кнопки
        if self.re20:
            self.rect.y += 55
            self.re20 = False
        if keys[pygame.K_RIGHT] or keys[pygame.K_a] or keys[pygame.K_LEFT] or keys[pygame.K_d]:  # Нажаты клавиши для
            # бега
            self.run(keys)
            running = True
        if not self.if_jump:
            if keys[pygame.K_UP] or keys[pygame.K_w]:  # Нажат прыжок
                self.if_jump = True
                self.jump_count = 10
                self.rect.y -= 20
            elif keys[pygame.K_h] and not running:  # Нажатие клавиши "h" для стрельбы
                self.fire()

            elif not (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_d]):
                self.stop()  # отсутствие движения
        else:
            self.jump()
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.wait()
        self.image = self.frames[self.cur_frame - 1]


class Bullet(pygame.sprite.Sprite):  # Класс пуль
    def __init__(self, x, y, direction_bul):
        super().__init__(bullet_sprites, all_sprites)
        self.x, self.y, self.direction_bul = x, y, direction_bul
        self.image = bull  # Изображение пули
        self.rect = self.image.get_rect()
        if direction_bul:  # Проверка направления и смещение координаты появления пули
            self.x -= 115
        self.rect = self.rect.move(self.x, self.y)

    def update(self, *args):
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


pers = Person(500, 500)  # Начальное положение персонажа


def main():  # главная функция
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)  # Отображение всех спрайтов
        all_sprites.update()  # Обновление спрайтов
        clock.tick(60)
        pygame.time.delay(10)
        pygame.display.flip()


# запуск главной функции
main()
quit()
