#!/usr/bin/env python3
import pygame
import time


def message(msg, color, dis, displayPosX, displayPosY):
    font_style = pygame.font.SysFont(None, 50)
    msgStr = font_style.render(msg, True, color)
    dis.blit(msgStr, [displayPosX, displayPosY])


if __name__ == "__main__":
    # create/initialize a user interface
    # initialize the game
    pygame.init()
    # create a window
    dis_width = 800
    dis_height = 600
    dis = pygame.display.set_mode((dis_width, dis_height))
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
    pixel_unit = 10

    clock = pygame.time.Clock()
    freq = 10
    game_over = False
    game_quit = False
    while not game_over:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                game_over = True
                game_quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -pixel_unit
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = pixel_unit
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -pixel_unit
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = pixel_unit
        
        if pos_x >= dis_width or pos_x <0 or pos_y >= dis_height or pos_y < 0:
            game_over = True
        pos_x += x_change
        pos_y += y_change
        dis.fill(white)
        pygame.draw.rect(dis, black, [pos_x, pos_y, pixel_unit, pixel_unit])
        pygame.display.update()
        clock.tick(freq)

    if not game_quit:
        message("You lost", red, dis, dis_width/2, dis_height/2)
        pygame.display.update()
        time.sleep(1)
    # end the game
    pygame.quit()
    quit()
