import pygame
import random
pygame.init()
W, H = 1200, 800
FPS = 60
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

paddleW = 300
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)


ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1


game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)


collision_sound = pygame.mixer.Sound('catch.mp3')
def show_pause_menu():
    pause_done = False
    while not pause_done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:  # Продолжить игру
                    pause_done = True
                elif event.key == pygame.K_q:  # Выход из игры
                    return True
        
        # Экран меню паузы
        screen.fill((0, 0, 0))  # Заливаем экран чёрным цветом для меню паузы
        pause_text = game_score_fonts.render('Paused: C=Continue, Q=Quit', True, (255, 255, 255))
        pause_rect = pause_text.get_rect(center=(W / 2, H / 2))
        screen.blit(pause_text, pause_rect)
        pygame.display.flip()
        clock.tick(15)
    return False

        

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

class Brick:
    def __init__(self, rect, color, breakable=True, perk=None):
        self.rect = rect
        self.color = color
        self.breakable = breakable
        self.perk = perk

def apply_perk(perk):
    global paddleW, ballSpeed
    if perk == 'expand':
        paddleW = min(200, paddleW + 20)
    # Add other perks handling here

block_list = [
    Brick(pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50), 
          (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)),
          breakable=False if random.random() < 0.1 else True,  # 10% кирпичей будут неразрушаемыми
          perk='expand' if random.random() < 0.05 else None)  # 5% кирпичей дадут бонус
    for i in range(10) for j in range(4)
]

# Game over screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Win screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)
 
start_time = pygame.time.get_ticks()
time_interval = 10000

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                show_pause_menu()
    current_time = pygame.time.get_ticks()
    if current_time - start_time > time_interval:  # Каждые time_interval миллисекунд
        ballSpeed += 1  # Увеличить скорость мяча
        paddleW = max(50, paddleW - 5)  # Уменьшить размер ракетки, но не меньше 50
        paddle.width = paddleW  # Обновить размер ракетки в её свойстве
        start_time += time_interval  # Сбросить таймер

    screen.fill(bg)
    
    for brick in block_list:
        pygame.draw.rect(screen, brick.color, brick.rect)
        
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx

    if ball.centery < ballRadius + 50:
        dy = -dy

    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    for brick in block_list[:]:
        if ball.colliderect(brick.rect):
            if brick.breakable:
                block_list.remove(brick)
                game_score += 1
                collision_sound.play()
            dx, dy = detect_collision(dx, dy, ball, brick.rect)
            if brick.perk:
                apply_perk(brick.perk)
            break

    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)

    if ball.bottom > H:
        screen.fill(bg)
        screen.blit(losetext, losetextRect)
    elif not block_list:
        screen.fill(bg)
        screen.blit(wintext, wintextRect)

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    pygame.display.flip()
    clock.tick(FPS)
