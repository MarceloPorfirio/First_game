import pygame

pygame.init()
screen = pygame.display.set_mode((800,500))
pygame.display.set_caption('New Game')
clock = pygame.time.Clock()
running = True

dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Definir a cor da tela
    screen.fill('black')

    # Definir o circulo da posição do player
    pygame.draw.circle(screen,'white',player_pos,40)

    # Mover o circulo
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt

    # Exibir a tela
    pygame.display.flip()

    # Definir o tempo de movimento
    dt = clock.tick(60) / 1000





pygame.quit()
