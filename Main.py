import pygame
import LoadImage

pygame.init()
# создание окна
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
cur_frame = 0

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

person_sprites = pygame.sprite.GroupSingle()
all_sprites = pygame.sprite.Group()
tile_sprites = pygame.sprite.Group()
direction = False


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, frames, x, y, num_wait):
        super().__init__(person_sprites)
        self.num_wait = num_wait
        global cur_frame
        self.frames = frames
        if cur_frame >= len(self.frames):
            cur_frame = 0
        self.image = self.frames[cur_frame]
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)

    def wait(self):
        pygame.time.wait(self.num_wait[cur_frame - 1])

    def update(self):
        global cur_frame
        self.wait()
        self.image = self.frames[cur_frame]
        cur_frame += 1
        print(cur_frame)


class Person:
    def __init__(self, pos_x, pos_y):
        self.anim = AnimatedSprite
        self.pos_x = pos_x
        self.pos_y = pos_y

    def run(self, keys):  # Бег
        global direction
        if keys[pygame.K_LEFT]:
            self.pos_x = self.pos_x - 15
            self.anim(personRunLeft, self.pos_x - 30, self.pos_y, [100, 150, 100]).update()
            direction = False  # Персонаж смотрит влево
        elif keys[pygame.K_RIGHT]:
            self.pos_x = self.pos_x + 15
            self.anim(personRun, self.pos_x, self.pos_y, [100, 150, 100]).update()
            direction = True  # Персонаж смотрит вправо

    def stop(self):  # Отсутствие движения
        if direction:
            self.anim(personStop, self.pos_x, self.pos_y, [100, 100, 100]).update()
        else:
            self.anim(personStopLeft, self.pos_x - 30, self.pos_y, [100, 100, 100]).update()

    def jump(self):  # Прыжок
        pass

    def fire(self):  # Стрельба
        pass

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

# Начальное положение персонажа


pers = Person(500, 500)


def main():  # главная функция
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pers.update()
        screen.fill((0, 0, 0))
        person_sprites.draw(screen)
        clock.tick(50)
        pygame.display.flip()


# запуск главной функции
main()
quit()
