from sys import stdin
import pygame

try:
    lines = []
    for line in stdin:
        lines.append(line.rstrip("\n"))
    w, n = map(int, lines[0].split())
    # print(w, n)
except ValueError:
    print('Неправильный формат ввода')
else:
    central_point = w * n
    # print(central_point)

    COLORS_base = ['red', 'green', 'blue'] * (n // 3 + 1)
    COLORS = []
    k = 0
    for color in COLORS_base:
        COLORS.append(color)
        k += 1
        if k == n:
            break
    COLORS = COLORS[::-1]
    # print(COLORS)

    if __name__ == '__main__':
        pygame.init()
        size = width, height = 600, 600
        screen = pygame.display.set_mode(size)

        for i in range(n):
            pygame.draw.circle(screen, COLORS[i - (3 * (i // 3))], (central_point, central_point),
                               central_point - (w * i))

        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
