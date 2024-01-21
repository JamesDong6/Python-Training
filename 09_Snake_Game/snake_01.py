#!/usr/bin/env python3
import pygame
import time


if __name__ == "__main__":
    # create/initialize a user interface
    # initialize the game
    pygame.init()
    # create a window
    dis = pygame.display.set_mode((400, 300))
    # update the window
    pygame.display.update()
    time.sleep(5.0)
    # end the game
    pygame.quit()
    quit()
