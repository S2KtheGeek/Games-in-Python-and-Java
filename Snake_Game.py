import pygame
import time
import random

pygame.init()
clock = pygame.time.Clock()

col_orn = (255, 123, 7)
col_blk = (0, 0, 0)
col_red = (255, 0, 0)
col_grn = (0, 255, 0)
col_sky = (50, 153, 213)

d_width = 700
d_height = 700

display = pygame.display.set_mode((d_width, d_height))
pygame.display.set_caption("The Snake Game using Pygame")
display.fill(col_blk)


snake_size = 10
snake_speed = 20
snake_pos = []



def snake(snake_size, snake_pos):
    for x in snake_pos:
         pygame.draw.rect(display, col_orn, [x[0], x[1], snake_size, snake_size])



def snake_game():
    game_over = False
    game_end = False

    x1 = d_width / 2
    y1 = d_height / 2

    x1_ch = 0
    y1_ch = 0

    snake_list = []
    length_of_snake = 1


    foodx = round(random.randrange(0, d_width - snake_size) / 10.0) * 10.0
    foody = round(random.randrange(0, d_height - snake_size) / 10.0) * 10.0

    while not game_over:
        while game_end == True:
            display.fill(col_sky)
            font_style = pygame.font.SysFont("comicsansms", 20)
            msg = font_style.render("You Lost!! Wanna Play Again? Press Y to play again Or Press N to quit", True, col_red)
            display.blit(msg, [d_width / 20, d_height / 3])

            gameovr_font = pygame.font.SysFont("comicsansms", 40)
            gameovr = gameovr_font.render("   Game Over :)", True, col_red)
            display.blit(gameovr, [d_width / 4, d_height / 6])

            score = length_of_snake - 1
            score_font = pygame.font.SysFont("comicsansms", 40)
            value = score_font.render("Score: " + str(score), True, col_grn)
            display.blit(value, [d_width / 3, d_height / 4])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        snake_game()
                    elif event.key == pygame.K_n:
                        pygame.quit()
                        quit()


                if event.type == pygame.QUIT:
                    game_over = True
                    game_end = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            #print(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_ch = -snake_size
                    y1_ch = 0
                elif event.key == pygame.K_RIGHT:
                    x1_ch = snake_size
                    y1_ch = 0
                elif event.key == pygame.K_UP:
                    y1_ch = -snake_size
                    x1_ch = 0
                elif event.key == pygame.K_DOWN:
                    y1_ch = snake_size
                    x1_ch = 0

        if x1 >= d_width or x1 < 0 or y1 >= d_height or y1 < 0 :
            game_end = True

        x1 += x1_ch
        y1 += y1_ch

        display.fill(col_blk)
        pygame.draw.rect(display, col_grn, [foodx, foody, snake_size, snake_size])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_end = True
        snake(snake_size, snake_list)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, d_width - snake_size) / 10.0) * 10.0
            foody = round(random.randrange(0, d_height - snake_size) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


if __name__ == '__main__':
    snake_game()
