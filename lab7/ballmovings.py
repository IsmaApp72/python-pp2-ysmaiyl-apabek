import pygame
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Move the Ball")
ball_color = (255, 0, 0)
ball_radius = 25
ball_pos = [screen_width // 2, screen_height // 2]
ball_move = 20
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ball_pos[1] -= ball_move
    if keys[pygame.K_DOWN]:
        ball_pos[1] += ball_move
    if keys[pygame.K_LEFT]:
        ball_pos[0] -= ball_move
    if keys[pygame.K_RIGHT]:
        ball_pos[0] += ball_move
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)
    pygame.display.flip()
pygame.quit()
