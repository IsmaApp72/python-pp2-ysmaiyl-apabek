import pygame
import datetime

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

clock_face = pygame.image.load('clock_face.png')
minute_hand = pygame.image.load('minutes_hand.png').convert_alpha()
second_hand = pygame.image.load('seconds_hand.png').convert_alpha()
minute_hand.set_colorkey((255, 255, 255))
second_hand.set_colorkey((255, 255, 255))

center_x = 400
center_y = 300

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()
    minute_angle = now.minute * 6
    second_angle = now.second * 6

    minute_angle = 90 - minute_angle
    second_angle = 90 - second_angle

    rotated_minute_hand = pygame.transform.rotate(minute_hand, minute_angle)
    rotated_second_hand = pygame.transform.rotate(second_hand, second_angle)

    minute_hand_rect = rotated_minute_hand.get_rect(center=(center_x, center_y))
    second_hand_rect = rotated_second_hand.get_rect(center=(center_x, center_y))

    screen.fill((255, 255, 255))

    clock_face_rect = clock_face.get_rect(center=(center_x, center_y))
    screen.blit(clock_face, clock_face_rect.topleft)

    screen.blit(rotated_minute_hand, minute_hand_rect.topleft)
    screen.blit(rotated_second_hand, second_hand_rect.topleft)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
