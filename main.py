import random
import time

from data import *
import pygame
import sys

# We create three arrays, one for the spanish words, another for the english words, and another for visited
# we also create integer arrays for the words
# we need to keep track of the score
# we start off with two random words (add them to visited) and keep note of what index/position those words are
# we access the integer arrays (monthly searches) using the index
# when button higher or lower is pressed, we compute and check
# if correct, add point, wait a bit, get rid of the left word (add to visited) and move the right word to the left
# use randomizer and check condition to see if next word has already been visited
# if all words have been visited, make all unvisited and make the left word visited before getting a new word for the right side

# if incorrect, end game, go to final screen display score, and choose play again button

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
        if visited[newint - 1] is False:
            break
    visited[newint - 1] = True
    return newint - 1


def checkiffilled(visited):
    a = False  # false = all are visited, true = unvisited
    for i in range(19):
        if visited[i] is False:
            a = True
            break
    if a is False:
        visited[:] = [False] * 19
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

    new_word = True
    new_game = True
    left = 0
    right = 0
    score = 0
    while game:
        pos = pygame.mouse.get_pos()
        screen.fill(WHITE)
        readBoard = open('../HigherLower/score', 'r')
        font_text = pygame.font.SysFont("arial", 40)
        font_buttons = pygame.font.SysFont("arial", 23)
        font_score = pygame.font.SysFont("arial", 18)
        Higher = font_buttons.render("Más", True, BLACK)
        Lower = font_buttons.render("Menos", True, BLACK)
        score_display = font_score.render(str(score), True, BLACK)
        highscore_display = font_score.render(str(readBoard.read()), True, BLACK)


        if score > int(float(readBoard.read())):
            writeBoard = open('../HigherLower/score', 'w')
            writeBoard.write(str(score))


        pygame.draw.rect(screen, GREEN, (1250, 350, 250, 80))
        pygame.draw.rect(screen, RED, (1250, 480, 250, 80))
        pygame.draw.line(screen, BLACK, (screen_W / 2, 0), (screen_W / 2, screen_H - 30), 5)

        Button1 = Higher.get_rect()
        Button1.center = (screen_W / 1.3, screen_H - screen_H / 1.77)
        screen.blit(Higher, Button1)

        Button2 = Lower.get_rect()
        Button2.center = (screen_W / 1.3, screen_H - screen_H / 2.35)
        screen.blit(Lower, Button2)

        if new_word is True:
            left = right
            if new_game is True:
                left = checkiffilled(visited)
                new_game = False

            right = checkiffilled(visited)
            new_word = False

        left_text = font_text.render(spanish[left], True, BLACK)
        left_english = font_text.render(english[left], True, BLACK)
        left_score = font_text.render(searches[left] + " búsquedas", True, BLACK)

        left_word = left_text.get_rect()
        left_word.center = (screen_W / 4, screen_H - screen_H / 1.3)
        screen.blit(left_text, left_word)

        left_english_text = left_english.get_rect()
        left_english_text.center = (screen_W / 4, screen_H - screen_H / 1.5)
        screen.blit(left_english, left_english_text)

        left_searches = left_score.get_rect()
        left_searches.center = (screen_W / 4, screen_H - screen_H / 1.8)
        screen.blit(left_score, left_searches)



        right_text = font_text.render(spanish[right], True, BLACK)

        right_word = right_text.get_rect()
        right_word.center = (screen_W / 1.3, screen_H - screen_H / 1.3)
        screen.blit(right_text, right_word)


        score_text = score_display.get_rect()
        score_text.center = (screen_W / 1.1, screen_H - screen_H / 15)
        screen.blit(score_display, score_text)

        highscore_text = highscore_display.get_rect()
        highscore_text.center = (screen_W / 1.3, screen_H - screen_H / 15)
        screen.blit(highscore_display, highscore_text)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                intro = False
                game = False
                final = False
            if event.type == pygame.MOUSEBUTTONUP:
                if Button1.collidepoint(pos):  # higher
                    if searches[right] >= searches[left]:
                        score += 1
                        print("correct")
                        new_word = True
                    else:
                        loop = False
                        game = False

                elif Button2.collidepoint(pos):  # lower
                    if searches[right] <= searches[left]:
                        score += 1
                        print("correct")
                        new_word = True
                    else:
                        loop = False
                        game = False

pygame.quit()
sys.exit()
