import pygame

pygame.init()

window_width = 800
window_height = 600

window = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Halium b/0.1")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))

    pygame.display.update()

pygame.quit()
