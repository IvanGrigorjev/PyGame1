from sys import stdin
import pygame

try:
    w, h = map(int, input().split())
except ValueError:
    print('Неправильный формат ввода')
else:
    if __name__ == '__main__':
        pygame.init()
        size = width, height = w, h
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Прямоугольник')

        pygame.draw.rect(screen, 'red', (1, 1, w - 2, h - 2), 0)

        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
