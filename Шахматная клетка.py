from sys import stdin
import pygame

try:
    a, n = map(int, input().split())
except ValueError:
    print('Неправильный формат ввода')
else:
    if __name__ == '__main__':
        pygame.init()
        size = width, height = a, a
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Шахматная клетка')

        d = a // n
        if n % 2 == 0:
            color = ['black', 'white']
        else:
            color = ['white', 'black']
        for i in range(n):
            color = color[::-1]
            for j in range(n):
                pygame.draw.rect(screen, color[j - (2 * (j // 2))], (d * j, d * i, d * j + d, d * i + d), 0)

        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
