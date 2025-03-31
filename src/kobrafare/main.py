import random

import sys

import os

import pygame

# Brzina igre
speed = 13

# Veličina kvadrata zmije
square_size = 30

# Veličina prozora
frame_size_x = 720
frame_size_y = 480


# Inicijalizacija igre
check_errors = pygame.init()
if check_errors[1] > 0:
    print("Greska " + str(check_errors[1]))
else:
    print("Igra uspjesno inicijalizirana")

# Učitavanje muzike
pygame.mixer.music.load("Cat_C418.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
    

# Inicijalizacija prozora igre
pygame.display.set_caption("Igra Zmija")
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

# Učitavanje slika za zmijinu glavu i svaki smjer
snake_head_imgs = {
    "RIGHT": pygame.transform.scale(pygame.image.load("snake_head_right.png"), (square_size, square_size)),
    "LEFT": pygame.transform.scale(pygame.image.load("snake_head_left.png"), (square_size, square_size)),
    "UP": pygame.transform.scale(pygame.image.load("snake_head_up.png"), (square_size, square_size)),
    "DOWN": pygame.transform.scale(pygame.image.load("snake_head.png"), (square_size, square_size)),
}

# Početna slika zmijine glave 
snake_head_img = snake_head_imgs["RIGHT"]

# Slika za rep zmije 
snake_tail_img = pygame.image.load("snake_tail.png")

# Skaliranje Slike
snake_tail_img = pygame.transform.scale(snake_tail_img, (square_size, square_size))



# Učitavanje slike za hranu
food_img = pygame.image.load("food.png")

food_img = pygame.transform.scale(food_img, (square_size, square_size))

# Boje
blue = pygame.Color(0, 0, 255)
yellow = pygame.Color(255, 255, 0)
gray = pygame.Color(128, 128, 128)
brightgreen = pygame.Color(106, 190, 48)
red = pygame.Color(255, 0, 0)
green = pygame.Color(2, 48, 32)
white = pygame.Color(255, 255, 255)
brown = pygame.Color(160, 128, 96)


# Kontroler brzine igre
fps_controller = pygame.time.Clock()
paused = False
music_paused = False

# Inicijalizacija varijabli igre
def init_vars():
    global head_pos, snake_body, food_pos, food_spawn, score, direction, snake_head_img
    direction = "RIGHT"
    head_pos = [120, 60]
    snake_body = [[120, 60]]
    food_pos = [
        random.randrange(1, (frame_size_x // square_size)) * square_size,

        random.randrange(1, (frame_size_y // square_size)) * square_size,
    ]

    food_spawn = True
    score = 0
    snake_head_img = snake_head_imgs["RIGHT"]

init_vars()

# Funkcija za pauziranje muzike
def toggle_music():
    global music_paused
    if music_paused:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()
    music_paused = not music_paused

# Prikaz rezultata
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render("Rezultat: " + str(score), True, color)
    score_rect = score_surface.get_rect()

    if choice == 1:
        score_rect.midtop = (frame_size_x / 10, 15)
    else:
        score_rect.midtop = (frame_size_x / 2, frame_size_y / 1.25)
    game_window.blit(score_surface, score_rect)

# Prikaz menija igre
def show_menu():
    font = pygame.font.SysFont("consolas", 40)
    while True:
        game_window.fill(green)
        title = font.render("Dobrodošli u igru Zmija!", True, white)
        prompt = font.render("Pritisnite SPACE za početak", True, yellow)

        game_window.blit(title, (frame_size_x / 2 - title.get_width() / 2, frame_size_y / 3))
        game_window.blit(prompt, (frame_size_x / 2 - prompt.get_width() / 2, frame_size_y / 2))

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return

# Prikaz menija
show_menu()

direction = "RIGHT"
paused = False


# Glavna petlja igre
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
                toggle_music()
            if not paused:
                if (event.key == pygame.K_w or event.key 
                    == ord("w")) and direction != "DOWN":
                    direction = "UP"
                    snake_head_img = snake_head_imgs["UP"]
                elif (event.key == pygame.K_s or event.key 
                      == ord("s")) and direction != "UP":
                    direction = "DOWN"
                    snake_head_img = snake_head_imgs["DOWN"]
                elif (event.key == pygame.K_a or event.key 
                      == ord("a")) and direction != "RIGHT":
                    direction = "LEFT"
                    snake_head_img = snake_head_imgs["LEFT"]
                elif (event.key == pygame.K_d or event.key 
                      == ord("d")) and direction != "LEFT":
                    direction = "RIGHT"
                    snake_head_img = snake_head_imgs["RIGHT"]

    if paused:
        font = pygame.font.SysFont("consolas", 40)
        while paused:
            game_window.fill(green)
            pause_title = font.render("Pauza", True, white)

            resume_text = font.render("Pritisnite P za nastavak", True, yellow)

            game_window.blit(pause_title, (frame_size_x / 2 - pause_title.get_width() / 2, frame_size_y / 3))
            game_window.blit(resume_text, (frame_size_x / 2 - resume_text.get_width() / 2, frame_size_y / 2))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    paused = False
                    toggle_music()
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
            snake_head_img=snake_head_img

        if head_pos[0] < 0:
            head_pos[0] = frame_size_x - square_size
        elif head_pos[0] > frame_size_x - square_size:
            head_pos[0] = 0
        elif head_pos[1] < 0:
            head_pos[1] = frame_size_y - square_size
        elif head_pos[1] > frame_size_y - square_size:
            head_pos[1] = 0

        # Jedenje hrane
        snake_body.insert(0, list(head_pos))
        if head_pos == food_pos:
            score += 1
            food_spawn = False
        else:
            snake_body.pop()

        # Spawnanje hrane
        if not food_spawn:
            food_pos = [random.randrange(1, (frame_size_x // square_size)) * square_size, random.randrange(1, (frame_size_y // square_size)) * square_size]
            food_spawn = True
        
        # Prikaz igre
        game_window.fill(green)
        game_window.blit(snake_head_img, (snake_body[0][0], snake_body[0][1]))
       
        for i, pos in enumerate(snake_body):
             if i == 0:  # Glava zmije (prvi segment)
                game_window.blit(snake_head_img, (pos[0], pos[1]))
             elif i == len(snake_body) - 1:  # Rep zmije (posljednji segment)
                game_window.blit(snake_tail_img, (pos[0], pos[1]))
             else:  # Tijelo zmije (srednji segmenti)
                pygame.draw.rect(game_window, brightgreen, pygame.Rect(pos[0], pos[1], square_size, square_size))




        # Prikazivanje hrane 
        game_window.blit(food_img, (food_pos[0], food_pos[1]))
        
        # Provjera sudara
        for block in snake_body[1:]:
            if head_pos == block:
                init_vars()
        
        show_score(1, white, "consolas", 20)

        pygame.display.update()

        fps_controller.tick(speed)

