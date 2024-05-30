import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Настройки экрана и шрифта
screen_width, screen_height = 600, 600
font = pygame.font.SysFont('arial', 36)

# Настройка экрана
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Змейка')

# Начальные параметры игры
clock = pygame.time.Clock()
snake_speed = 15

# Загрузка фонового изображения
background_img = pygame.image.load('path_to_your_background_image.jpg')


# Функция для отображения счетчика очков
def show_score(score):
    value = font.render("Счет: " + str(score), True, BLUE)
    screen.blit(value, [0, 0])


# Основная функция игры
def game_loop():
    game_over = False
    game_close = False

    x1 = screen_width / 2
    y1 = screen_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Генерация первого яблока
    foodx = round(random.randrange(0, screen_width - 10) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - 10) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            game_over_message = font.render("lose.Нажмите Q для выхода", True, RED)
            screen.blit(game_over_message, [screen_width / 9, screen_height / 6])
            show_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.blit(background_img, (0, 0))

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        for x in snake_list:
            pygame.draw.rect(screen, GREEN, [x[0], x[1], 10, 10])

        pygame.draw.rect(screen, RED, [foodx, foody, 10, 10])
        show_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - 10) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - 10) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()


game_loop()
