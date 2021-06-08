import random
import time

import pygame
import sys
from data import *
from score import *


# We create three arrays, one for the spanish words, another for the english words, and another for visited
#we also create integer arrays for the words
#we need to keep track of the score
#we start off with two random words (add them to visited) and keep note of what index/position those words are
#we access the integer arrays (monthly searches) using the index
#when button higher or lower is pressed, we compute and check
#if correct, add point, wait a bit, get rid of the left word (add to visited) and move the right word to the left
#use randomizer and check condition to see if next word has already been visited
#if all words have been visited, make all unvisited and make the left word visited before getting a new word for the right side

#if incorrect, end game, go to final screen display score, and choose play again button

pygame.init()

# set the size for the surface (screen)
# MUST BE PLAYED ON 1000 x 800
screen = pygame.display.set_mode((1800, 900), 0)
# set the caption for the screen
pygame.display.set_caption("Higher Lower")
# define colours you will be using
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (153, 204, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
loop = True
intro = True
game = True
final = True
print(english[10])
print(searches[10])

def findrandom(visited):
    while True:
        newint = random.randint(0, 19)
        if visited[newint] is False:
            break
    return newint


def checkiffilled(visited):
    a = False #false = all are visited, true = unvisited
    for i in range(19):
        if visited[i] is False:
            a = True
            break
    if a is False:
        visited[:] = [False]*19
    return findrandom(visited)




while loop:
    screen_W = screen.get_width()
    screen_H = screen.get_height()
    while intro:
        pos = pygame.mouse.get_pos()
        screen.fill(WHITE)
        image = pygame.image.load("../HigherLower/images/higherorlower.png")
        font_title = pygame.font.SysFont("arial bold", 80)
        title_text = font_title.render("Higher Lower", True, BLACK)

        font_title = pygame.font.SysFont("arial bold", 60)
        play_text = font_title.render("Play game", True, BLACK)

        logo_image = image.get_rect()
        logo_image.center = (screen_W / 2, screen_H / 2.8)
        screen.blit(image, logo_image)

        textRect2 = title_text.get_rect()
        textRect2.center = (screen_W / 1.83, screen_H - screen_H / 3)
        screen.blit(play_text, textRect2)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                intro = False
                game = False
                final = False
            if event.type == pygame.MOUSEBUTTONUP:
                if textRect2.collidepoint(pos):
                    intro = False

    while game:
        pos = pygame.mouse.get_pos()
        screen.fill(WHITE)
        readBoard = open('../HigherLower/data.txt', 'r')


        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                intro = False
                game = False
                final = False
            if event.type == pygame.MOUSEBUTTONUP:
                loop = False



pygame.quit()
sys.exit()