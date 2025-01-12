from sys import stdin
import pygame

try:
    lines = []
    for line in stdin:
        lines.append(line.rstrip("\n"))
    w, h = map(int, lines[0].split())
except ValueError:
    print('Неправильный формат ввода')
else:

    if __name__ == '__main__':
        pygame.init()
        size = width, height = w, h
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Крест')

        pygame.draw.line(screen, 'white', (0, 0), (w, h), width=5)
        pygame.draw.line(screen, 'white', (0, h), (w, 0), width=5)

        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
