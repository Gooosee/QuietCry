import pygame
import LoadImage

pygame.init()
# создание окна
size = width, height = 800, 800
screen = pygame.display.set_mode(size)

# Задержки для анимаций

waitStop = [100, 100, 100]  # Стоя
waitRun = [100, 150, 100]  # Набегу
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
        self.pos_y = y

        self.cur_frame = 0  # Номер кадра
        self.frames = personStop
        self.num_wait = waitStop
        self.image = personStop[self.cur_frame]  # Изображение спрайта
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.pos_x, self.pos_y)

    def run(self, keys):  # Бег
        global direction
        if keys[pygame.K_LEFT]:
            self.frames = personRunLeft
            self.num_wait = waitRun
            self.rect.x = self.pos_x - 40
            self.pos_x -= 15
            direction = True  # Персонаж смотрит влево
        elif keys[pygame.K_RIGHT]:
            self.frames = personRun
            self.num_wait = waitRun
            self.pos_x += 15
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
        pass

    def fire(self):  # Стрельба
        if direction:
            self.frames = personFireLeft
            self.rect.x = self.pos_x - 5
            self.num_wait = waitFire
        else:
            self.frames = personFire
            self.rect.x = self.pos_x - 5
            self.num_wait = waitFire
        bul = Bullet(self.pos_x + 110, self.pos_y + 36, direction)

    def wait(self):
        print(self.cur_frame)
        pygame.time.wait(self.num_wait[self.cur_frame - 1])

    def update(self):
        keys = pygame.key.get_pressed()  # в этом списке лежат все нажатые кнопки
        if keys[pygame.K_UP]:  # Нажат прыжок
            self.jump()
        elif keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:  # Нажаты клавишь для бега
            self.run(keys)
        elif keys[pygame.K_h]:
            self.fire()
        else:
            self.stop()  # отсутствие движения
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.wait()
        self.image = self.frames[self.cur_frame - 1]


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction_bul):
        super().__init__(bullet_sprites, all_sprites)
        self.x, self.y, self.direction_bul = x, y, direction_bul
        self.image = bull
        self.rect = self.image.get_rect()
        if direction_bul:
            self.x -= 115
        self.rect = self.rect.move(self.x, self.y)

    def update(self, *args):
        if not self.direction_bul:
            if self.rect.x <= 600:
                self.rect.x += 40
            else:
                self.kill()
        else:
            if self.rect.x >= 0:
                self.rect.x -= 40
            else:
                self.kill()


pers = Person(500, 500)  # Начальное положение персонажа


def main():  # главная функция
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
        clock.tick(500)
        pygame.display.flip()


# запуск главной функции
main()
quit()
