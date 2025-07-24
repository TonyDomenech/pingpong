import pygame
import sys
import random

WIDTH, HEIGHT = 600, 400
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 60
BALL_SIZE = 10
PADDLE_SPEED = 5
BALL_SPEED_X = 4
BALL_SPEED_Y = 2


def ai_move(paddle_y, ball_y):
    center = paddle_y + PADDLE_HEIGHT / 2
    distance = abs(center - ball_y)
    fail_prob = min(0.3, distance / HEIGHT)
    if random.random() < fail_prob:
        if ball_y < center:
            paddle_y += PADDLE_SPEED
        else:
            paddle_y -= PADDLE_SPEED
    else:
        if ball_y < center:
            paddle_y -= PADDLE_SPEED
        elif ball_y > center:
            paddle_y += PADDLE_SPEED
        paddle_y += random.randint(-1, 1)
    return paddle_y

def show_menu(screen):
    font = pygame.font.Font(None, 36)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return False, False
                if event.key == pygame.K_2:
                    return False, True
                if event.key == pygame.K_3:
                    return True, True

        screen.fill((0, 0, 0))
        menu_text = [
            "1. Jugador vs Jugador",
            "2. Jugador vs IA",
            "3. IA vs IA",
        ]
        for i, text in enumerate(menu_text):
            rendered = font.render(text, True, (255, 255, 255))
            screen.blit(rendered, (80, 120 + i * 40))

        pygame.display.flip()


def game_loop(screen, clock, left_ai=False, right_ai=False):
    left_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
    right_y = left_y
    ball_x = WIDTH // 2
    ball_y = HEIGHT // 2
    ball_vx = BALL_SPEED_X
    ball_vy = BALL_SPEED_Y

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if left_ai:
            left_y = ai_move(left_y, ball_y)
        else:
            if keys[pygame.K_w]:
                left_y -= PADDLE_SPEED
            if keys[pygame.K_s]:
                left_y += PADDLE_SPEED

        if right_ai:
            right_y = ai_move(right_y, ball_y)
        else:
            if keys[pygame.K_UP]:
                right_y -= PADDLE_SPEED
            if keys[pygame.K_DOWN]:
                right_y += PADDLE_SPEED

        left_y = max(0, min(HEIGHT - PADDLE_HEIGHT, left_y))
        right_y = max(0, min(HEIGHT - PADDLE_HEIGHT, right_y))

        ball_x += ball_vx
        ball_y += ball_vy

        if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
            ball_vy *= -1

        if ball_x <= 20 and left_y <= ball_y <= left_y + PADDLE_HEIGHT:
            ball_vx *= -1
        if ball_x >= WIDTH - 20 - BALL_SIZE and right_y <= ball_y <= right_y + PADDLE_HEIGHT:
            ball_vx *= -1

        if ball_x < 0 or ball_x > WIDTH:
            ball_x = WIDTH // 2
            ball_y = HEIGHT // 2

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), (10, left_y, PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.rect(screen, (255, 255, 255), (WIDTH - 20, right_y, PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.rect(screen, (255, 255, 255), (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

        pygame.display.flip()
        clock.tick(60)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ping Pong")
    clock = pygame.time.Clock()

    left_ai, right_ai = show_menu(screen)
    game_loop(screen, clock, left_ai, right_ai)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
