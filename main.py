# main.py

import pygame
from engine.objects import Paddle, Ball

# Inisialisasi Pygame
pygame.init()

# Pengaturan layar
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('2D Ping Pong Game')

# Warna
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Inisialisasi pemain dan bola
paddle1 = Paddle(position=[50, 300])
paddle2 = Paddle(position=[750, 300])
ball = Ball(position=[400, 300])

# Skor
score1 = 0
score2 = 0
font = pygame.font.Font(None, 74)

# Waktu
clock = pygame.time.Clock()

def reset_game():
    global score1, score2, game_over, paddle1, paddle2, ball
    score1 = 0
    score2 = 0
    game_over = False
    paddle1 = Paddle(position=[50, 300])
    paddle2 = Paddle(position=[750, 300])
    ball = Ball(position=[400, 300])

def display_winner():
    global score1, score2
    winner_text = "Player 1 Wins!" if score1 == 10 else "Player 2 Wins!"
    score_text = f"{score1} - {score2}"
    title = font.render(winner_text, True, WHITE)
    score = font.render(score_text, True, WHITE)
    repeat_button = font.render("Repeat", True, WHITE)
    screen.blit(title, (235, 180))
    screen.blit(score, (335, 280))
    screen.blit(repeat_button, (310, 380))
    pygame.display.flip()

# Loop utama
running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and game_over:
            mouse_pos = event.pos
            if 325 <= mouse_pos[0] <= 475 and 400 <= mouse_pos[1] <= 474:
                reset_game()

    if not game_over:
        # Cek input untuk pemain 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1.move_up()
        if keys[pygame.K_s]:
            paddle1.move_down()

        # Cek input untuk pemain 2
        if keys[pygame.K_UP]:
            paddle2.move_up()
        if keys[pygame.K_DOWN]:
            paddle2.move_down()

        # Update posisi pemain dan bola
        paddle1.update()
        paddle2.update()
        ball.update()

        # Deteksi tumbukan dengan dinding atas dan bawah
        if ball.position[1] <= 80 or ball.position[1] >= 470:
            ball.velocity[1] = -ball.velocity[1]

        # Deteksi tumbukan dengan paddle
        if paddle1.rect.colliderect(ball.rect) or paddle2.rect.colliderect(ball.rect):
            ball.velocity[0] = -ball.velocity[0]

        # Deteksi jika bola melewati pemain
        if ball.position[0] <= 0:
            score2 += 1
            ball.reset_position()
        elif ball.position[0] >= 770:
            score1 += 1
            ball.reset_position()

        # Periksa jika ada yang menang
        if score1 == 10 or score2 == 10:
            game_over = True

    # Menggambar
    screen.fill(BLACK)

    if not game_over:
        pygame.draw.rect(screen, WHITE, paddle1.rect)
        pygame.draw.rect(screen, WHITE, paddle2.rect)
        pygame.draw.ellipse(screen, WHITE, ball.rect)

        # Menggambar skor
        score_text = font.render(f"{score1} - {score2}", True, WHITE)
        screen.blit(score_text, (350, 10))

    # Menggambar dinding atas dan bawah
    pygame.draw.line(screen, WHITE, (0, 80), (800, 80), 5)
    pygame.draw.line(screen, WHITE, (0, 500), (800, 500), 5)

    if game_over:
        display_winner()

    pygame.display.flip()

    # Batasi frame rate
    clock.tick(60)

pygame.quit()
