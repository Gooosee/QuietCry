class Button:
    def __init__(self, x, y, dx, dy):
        self.x, self.y, self.dx, self.dy = x, y, dx, dy

    def draw(self, screen, image):
        self.screen = screen
        screen.blit(image, [self.x, self.y, self.dx, self.dy])

    def clicked(self, pos, imageA):
        if self.x <= pos[0] <= self.x + self.dx and self.y <= pos[1] <= self.y + self.dy:
            self.draw(self.screen, imageA)
            return True
        else:
            return False
