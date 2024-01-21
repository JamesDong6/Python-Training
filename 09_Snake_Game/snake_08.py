#!/usr/bin/env python3
import pygame
import math
import time
import random


# we observed one issue. Since one pixel is too small, it's hard to adjust direction
# such that the pixel position of the snake and the food exactly align.
# we need to fix it.

def message(msg, color, dis, displayPosX, displayPosY):
    font_style = pygame.font.SysFont(None, 50)
    msgStr = font_style.render(msg, True, color)
    dis.blit(msgStr, [displayPosX, displayPosY])


def checkCollision(posSnake: list, posFood: list, pixelUnit):
    """
    check whether the first grid of the snake collides with a food.
    """
    # these 4 points are the left bottom corner
    posXSnake = posSnake[0]
    posYSnake = posSnake[1]
    posXFood = posFood[0]
    posYFood = posFood[1]
    # convert to the center point of a square
    posXSnakeCenter = int(posXSnake + 0.5 * pixelUnit)
    posYSnakeCenter = int(posYSnake + 0.5 * pixelUnit)
    posXFoodCenter = int(posXFood + 0.5 * pixelUnit)
    posYFoodCenter = int(posYFood + 0.5 * pixelUnit)
    # check if two squares intersect with each other
    distance = math.sqrt((posXSnakeCenter-posXFoodCenter)**2 + (posYSnakeCenter-posYFoodCenter)**2)
    if distance > pixelUnit:
        collisionFlag = False
    else:
        collisionFlag = True
    return collisionFlag


if __name__ == "__main__":
    # create/initialize a user interface
    # initialize the game
    pygame.init()
    # create a window
    dis_width = 400
    dis_height = 300
    dis = pygame.display.set_mode((dis_width, dis_height))
    # update the window
    pygame.display.update()
    pygame.display.set_caption("Snake Game")

    white = (255, 255, 255)
    black = (0, 0, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)

    pos_x = int(dis_width / 2)
    pos_y = int(dis_height / 2)
    x_change = 0
    y_change = 0
    pixel_unit = 10

    numFood = 10
    posFoodList = list()
    for idx in range(numFood):
        # generate food for snake
        foodx = int(random.randrange(0, dis_width-pixel_unit))
        foody = int(random.randrange(0, dis_height-pixel_unit))
        posFoodList.append([foodx, foody])

    clock = pygame.time.Clock()
    freq = 5
    game_over = False
    game_quit = False
    eatFlag = False
    toEatIdx = 0
    print("toEatIdx: ", toEatIdx)
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

        if toEatIdx <= numFood - 0.5:
            if not eatFlag:
                eatFlag = checkCollision([pos_x, pos_y], posFoodList[toEatIdx], pixel_unit)
            if eatFlag:
                print("Yummy! Eat food: #", int(toEatIdx))
                toEatIdx = toEatIdx + 1
                eatFlag = False
        else:
            print("You eat all foods.")

        if pos_x >= dis_width or pos_x <0 or pos_y >= dis_height or pos_y < 0:
            game_over = True
        pos_x += x_change
        pos_y += y_change
        dis.fill(white)

        if toEatIdx <= numFood - 0.5:
            foodx = posFoodList[toEatIdx][0]
            foody = posFoodList[toEatIdx][1]
            pygame.draw.rect(dis, blue, [foodx, foody, pixel_unit, pixel_unit])

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
