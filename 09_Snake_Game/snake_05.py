#!/usr/bin/env python3
import pygame
import time


if __name__ == "__main__":
    # create/initialize a user interface
    # initialize the game
    pygame.init()
    # create a window
    dis = pygame.display.set_mode((800, 600))
    # update the window
    pygame.display.update()
    pygame.display.set_caption("Snake Game")

    white = (255, 255, 255)
    black = (0, 0, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)

    pos_x = 300
    pos_y = 300
    x_change = 0
    y_change = 0

    clock = pygame.time.Clock()
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = 10
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -10
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 10
        pos_x += x_change
        pos_y += y_change
        dis.fill(white)
        pygame.draw.rect(dis, black, [pos_x, pos_y, 10, 10])
        pygame.display.update()
        clock.tick(5)
    # end the game
    pygame.quit()
    quit()
