import pygame

try:
    n = input()
    if int(n) != float(n):
        raise ValueError

    n = int(n)
    pygame.init()
    size = width, height = 700, 300
    screen = pygame.display.set_mode(size)
    screen.fill("yellow")
    a = n // 2
    color = pygame.Color("orange")
    for i in range(0, width, a * 2):
        for j in range(0, height, a * 2):
            if i + a * 2 > width or j + a * 2 > height:
                continue
            points = [(i, j + a), (i + a, j), (i + a * 2, j + a), (i + a, j + a * 2)]
            pygame.draw.polygon(screen, color, points)

    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
except ValueError:
    print("Неправильный формат ввода")
