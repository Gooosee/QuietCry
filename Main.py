import pygame
import LoadImage

pygame.init()
# создание окна
size = width, height = 500, 500
screen = pygame.display.set_mode(size)

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

person_sprites = pygame.sprite.GroupSingle()
all_sprites = pygame.sprite.Group()
tile_sprites = pygame.sprite.Group()


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, frames, x, y):
        super().__init__(person_sprites)
        self.frames = frames
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)

    def wait(self):
        pass

    def update(self):
        self.image = self.frames[self.cur_frame]
        self.cur_frame += 1


class Person:
    def __init__(self, pos_x, pos_y):
        self.anim = AnimatedSprite
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.front = 'right' #Направление взгляда, для того, чтобы прыжок был в нужную сторону

    def run(self, args):
        if args[0].key == pygame.K_LEFT:
            self.pos_x -= 30
            self.anim(personRunLeft, self.pos_x, self.pos_y)
            self.front = 'left'
        elif args[0].key == pygame.K_RIGHT:
            self.pos_x += 30
            self.anim(personRun, self.pos_x, self.pos_y)
            self.front = 'right'

    def stop(self):
        pass

    def jump(self, args):
        if args[0].key == pygame.K_UP or args[0].key == pygame.K_SPACE:
            self.pos_y -= 50
            if self.front == 'right':
                self.anim(personJump, self.pos_x, self.pos_y - 40)
            else:
                self.anim(personJumpLeft, self.pos_x, self.pos_y - 40)

    def fire(self):
        pass

    def update(self, *args):
        if args[0].key == pygame.K_LEFT or args[0].key == pygame.K_RIGHT:
            self.run(args)
        elif args[0].key == pygame.K_UP or args[0].key == pygame.K_SPACE:
            self.jump(args)


pers = Person(50, 250)


def main():  # главная функция
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                pers.update(event)
        screen.fill((0, 0, 0))
        person_sprites.draw(screen)
        pygame.display.flip()


# запуск главной функции
main()
quit()
