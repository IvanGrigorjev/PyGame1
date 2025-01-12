import pygame

try:
    n = input()
    if int(n) != float(n):
        raise ValueError
    n = int(n)
    pygame.init()
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    screen.fill("black")
    color = pygame.Color("white")

    s = 300 // n
    pygame.draw.ellipse(screen, color, (0, 0, 300, 300), 1)
    pygame.draw.ellipse(screen, color, (0, height // 2 - s // 2, 300, s), 1)
    pygame.draw.ellipse(screen, color, (width // 2 - s // 2, 0, s, 300), 1)

    for i in range(n - 1):
        pygame.draw.ellipse(screen, color, (0, height // 2 - s // 2 * (i + 1), 300, s * (i + 1)), 1)
        pygame.draw.ellipse(screen, color, (width // 2 - s // 2 * (i + 1), 0, s * (i + 1), 300), 1)

    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
except ValueError:
    print("Неправильный формат ввода")
