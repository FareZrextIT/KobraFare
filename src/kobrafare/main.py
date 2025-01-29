import random
import sys

import pygame

speed = 15

# velicina prozora
# Dodat cu funkciju za prilagodjavanje rezolucije
frame_size_x = 720
frame_size_y = 480

check_errors = pygame.init()

if check_errors[1] > 0:
    print("Greska " + check_errors[1])
else:
    print("Igra uspjesno inicijalizirana")

# Inicijalizacija prozora igre
pygame.display.set_caption("Igra Zmija")
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))


# boje
blue = pygame.Color(0, 0, 255)
yellow = pygame.Color(255, 255, 0)
gray = pygame.Color(128, 128, 128)
red = pygame.Color(255, 0, 0)
brightgreen = pygame.Color(106, 190, 48)
green = pygame.Color(2, 48, 32)
cyan = pygame.Color(0, 255, 255)
white = pygame.Color(255, 255, 255)
brown = pygame.Color(160, 128, 96)

fps_controller = pygame.time.Clock()
# jedna zmijina velicina kruga
square_size = 20

paused = False


def init_vars():
    global head_pos, snake_body, food_pos, food_spawn, score, direction
    direction = "RIGHT"
    head_pos = [120, 60]
    snake_body = [[120, 60]]
    food_pos = [
        random.randrange(1, (frame_size_x // square_size)) * square_size,
        random.randrange(1, (frame_size_y // square_size)) * square_size,
    ]
    food_spawn = True
    score = 0


init_vars()


def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render("Rezultat: " + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x / 10, 15)
    else:
        score_rect.midtop = (frame_size_x / 2, frame_size_y / 1.25)

    game_window.blit(score_surface, score_rect)


def show_menu():
    font = pygame.font.SysFont("consolas", 40)
    while True:
        game_window.fill(green)
        title = font.render("Dobrodošli u igru Zmija!", True, white)
        prompt = font.render("Pritisnite SPACE za početak", True, yellow)
        game_window.blit(
            title, (frame_size_x / 2 - title.get_width() / 2, frame_size_y / 3)
        )
        game_window.blit(
            prompt, (frame_size_x / 2 - prompt.get_width() / 2, frame_size_y / 2)
        )
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return


# prikaz menija
show_menu()

# definisemo pocetni smjer
direction = "RIGHT"
# petlja igre

paused = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused

        if not paused:
            if event.type == pygame.KEYDOWN:
                if (
                    event.key == pygame.K_w or event.key == ord("w")
                ) and direction != "DOWN":
                    direction = "UP"
                elif (
                    event.key == pygame.K_s or event.key == ord("s")
                ) and direction != "UP":
                    direction = "DOWN"
                elif (
                    event.key == pygame.K_a or event.key == ord("a")
                ) and direction != "RIGHT":
                    direction = "LEFT"
                elif (
                    event.key == pygame.K_d or event.key == ord("d")
                ) and direction != "LEFT":
                    direction = "RIGHT"

    if paused:
        # Pauza - prikazivanje menija za pauzu
        font = pygame.font.SysFont("consolas", 40)
        while paused:
            game_window.fill(green)
            pause_title = font.render("Pauza", True, white)
            resume_text = font.render("Pritisnite P za nastavak ", True, yellow)
            game_window.blit(
                pause_title,
                (frame_size_x / 2 - pause_title.get_width() / 2, frame_size_y / 3),
            )
            game_window.blit(
                resume_text,
                (frame_size_x / 2 - resume_text.get_width() / 2, frame_size_y / 2),
            )
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    paused = False

    else:
        # Ako igra nije na pauzi, nastavi sa logikom igre
        if direction == "UP":
            head_pos[1] -= square_size
        elif direction == "DOWN":
            head_pos[1] += square_size
        elif direction == "LEFT":
            head_pos[0] -= square_size
        else:
            head_pos[0] += square_size

        if head_pos[0] < 0:
            head_pos[0] = frame_size_x - square_size
        elif head_pos[0] > frame_size_x - square_size:
            head_pos[0] = 0
        elif head_pos[1] < 0:
            head_pos[1] = frame_size_y - square_size
        elif head_pos[1] > frame_size_y - square_size:
            head_pos[1] = 0

        # jedenje jabuke
        snake_body.insert(0, list(head_pos))
        if head_pos[0] == food_pos[0] and head_pos[1] == food_pos[1]:
            score += 1
            food_spawn = False
        else:
            snake_body.pop()

        # spawnanje hrane
        if not food_spawn:
            food_pos = [
                random.randrange(1, (frame_size_x // square_size)) * square_size,
                random.randrange(1, (frame_size_y // square_size)) * square_size,
            ]
            food_spawn = True

        # GFX
        game_window.fill((2, 48, 32))
        for pos in snake_body:
            pygame.draw.rect(
                game_window,
                brightgreen,
                pygame.Rect(pos[0] + 2, pos[1] + 2, square_size - 2, square_size),
            )

        pygame.draw.rect(
            game_window,
            gray,
            pygame.Rect(food_pos[0], food_pos[1], square_size, square_size),
        )

        # kraj igre
        for block in snake_body[1:]:
            if head_pos[0] == block[0] and head_pos[1] == block[1]:
                init_vars()

        show_score(1, white, "consolas", 20)
        pygame.display.update()
        fps_controller.tick(speed)
