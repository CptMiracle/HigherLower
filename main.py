import random
import time

from data import *
import pygame
import sys


pygame.init()

# set the size for the surface (screen)
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
WARM = (255, 246, 237)

loop = True

intro = True
rules = False
rules2 = False
game = False
final = False
high_score = 0


def findrandom(visited):
    while True:
        newint = random.randint(0, 17)
        if visited[newint - 1] is False:
            break
    visited[newint - 1] = True
    return newint - 1


def checkiffilled(visited):
    a = False  # false = all are visited, true = unvisited
    for i in range(17):
        if visited[i] is False:
            a = True
            break
    if a is False:
        visited[:] = [False] * 17
    return findrandom(visited)


while loop:
    screen_W = screen.get_width()
    screen_H = screen.get_height()
    while intro:
        pos = pygame.mouse.get_pos()
        screen.fill(WHITE)
        imagelogo = pygame.image.load("../HigherLower/images/higherorlower.png")
        font_title = pygame.font.SysFont("arial bold", 80)
        title_text = font_title.render("Higher Lower", True, BLACK)

        font_title = pygame.font.SysFont("arial bold", 60)
        play_text = font_title.render("Play game", True, BLACK)

        logo_image = imagelogo.get_rect()
        logo_image.center = (screen_W / 2, screen_H / 2.8)
        screen.blit(imagelogo, logo_image)

        textRect2 = title_text.get_rect()
        textRect2.center = (screen_W / 1.83, screen_H - screen_H / 3)
        screen.blit(play_text, textRect2)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                intro = False
                rules = False
                game = False
                final = False
            if event.type == pygame.MOUSEBUTTONUP:
                if textRect2.collidepoint(pos):
                    intro = False
                    rules = True



    while rules:
        pos = pygame.mouse.get_pos()
        screen.fill(WHITE)
        font_title = pygame.font.SysFont("arial bold", 40)

        play_text = font_title.render("Continue", True, BLACK)
        rule1 = font_title.render("Se le mostrarán dos palabras o frases.", True, BLACK)
        rule2 = font_title.render("Tú decides si la palabra de la derecha tiene más o menos búsquedas que la palabra de la izquierda.", True, BLACK)
        rule3 = font_title.render("Si es más, escriba Más.", True, BLACK)
        rule4 = font_title.render("Si es menos, escriba Menos.", True, BLACK)
        rule5 = font_title.render("Si respondes bien la pregunta, obtienes un punto, de lo contrario, el juego termina.", True, BLACK)
        rule6 = font_title.render("Consejo: Si eres alguien en Internet, ¿buscarías esa palabra?", True, BLACK)
        textRect2 = play_text.get_rect()
        textRect2.center = (screen_W / 2, screen_H - screen_H / 6)
        screen.blit(play_text, textRect2)

        rule1rect = rule1.get_rect()
        rule1rect.center = (screen_W / 2, screen_H - screen_H / 1.2)
        screen.blit(rule1, rule1rect)

        rule2rect = rule2.get_rect()
        rule2rect.center = (screen_W / 2, screen_H - screen_H / 1.4)
        screen.blit(rule2, rule2rect)

        rule3rect = rule3.get_rect()
        rule3rect.center = (screen_W / 2, screen_H - screen_H / 1.6)
        screen.blit(rule3, rule3rect)

        rule4rect = rule4.get_rect()
        rule4rect.center = (screen_W / 2, screen_H - screen_H / 1.9)
        screen.blit(rule4, rule4rect)

        rule5rect = rule5.get_rect()
        rule5rect.center = (screen_W / 2, screen_H - screen_H / 2.3)
        screen.blit(rule5, rule5rect)

        rule6rect = rule6.get_rect()
        rule6rect.center = (screen_W / 2, screen_H - screen_H / 2.9)
        screen.blit(rule6, rule6rect)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                intro = False
                rules = False
                game = False
                final = False
            if event.type == pygame.MOUSEBUTTONUP:
                if textRect2.collidepoint(pos):
                    rules = False
                    rules2 = True

    while rules2:
        pos = pygame.mouse.get_pos()
        screen.fill(WHITE)
        font_title = pygame.font.SysFont("arial bold", 40)

        play_text = font_title.render("Continue", True, BLACK)
        rule1 = font_title.render("You will be shown two words/phrases.", True, BLACK)
        rule2 = font_title.render("You decide whether the word on the right has more or less searches than the word on the left.", True, BLACK)
        rule3 = font_title.render("If more, type Más.", True, BLACK)
        rule4 = font_title.render("If less, type Menos.", True, BLACK)
        rule5 = font_title.render("If you get the question right you get a point, otherwise the game is over.", True, BLACK)
        rule6 = font_title.render("Tip: If you are someone on the internet, would you search for that word?", True, BLACK)
        textRect2 = play_text.get_rect()
        textRect2.center = (screen_W / 2, screen_H - screen_H / 6)
        screen.blit(play_text, textRect2)

        rule1rect = rule1.get_rect()
        rule1rect.center = (screen_W / 2, screen_H - screen_H / 1.2)
        screen.blit(rule1, rule1rect)

        rule2rect = rule2.get_rect()
        rule2rect.center = (screen_W / 2, screen_H - screen_H / 1.4)
        screen.blit(rule2, rule2rect)

        rule3rect = rule3.get_rect()
        rule3rect.center = (screen_W / 2, screen_H - screen_H / 1.6)
        screen.blit(rule3, rule3rect)

        rule4rect = rule4.get_rect()
        rule4rect.center = (screen_W / 2, screen_H - screen_H / 1.9)
        screen.blit(rule4, rule4rect)

        rule5rect = rule5.get_rect()
        rule5rect.center = (screen_W / 2, screen_H - screen_H / 2.3)
        screen.blit(rule5, rule5rect)

        rule6rect = rule6.get_rect()
        rule6rect.center = (screen_W / 2, screen_H - screen_H / 2.9)
        screen.blit(rule6, rule6rect)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                intro = False
                rules = False
                rules2 = False
                game = False
                final = False
            if event.type == pygame.MOUSEBUTTONUP:
                if textRect2.collidepoint(pos):
                    rules2 = False
                    game = True

    new_word = True
    new_game = True
    left = 0
    right = 0
    score = 0
    display_buttons = True
    correct = False
    wrong = False
    pause = False
    clickable = True
    rect1 = 0
    rect2 = 0
    while game:
        pos = pygame.mouse.get_pos()
        screen.fill(WHITE)
        font_text = pygame.font.SysFont("arial", 40)
        font_buttons = pygame.font.SysFont("arial", 23)
        font_score = pygame.font.SysFont("arial", 18)
        Higher = font_buttons.render("Más", True, BLACK)
        Lower = font_buttons.render("Menos", True, BLACK)
        score_display = font_score.render(str(score), True, BLACK)
        score_current = font_score.render("Score: ", True, BLACK)
        highscore_display = font_score.render(str(high_score), True, BLACK)
        highscore = font_score.render("Highscore: ", True, BLACK)


        right_score = font_text.render(searches[right] + " búsquedas", True, BLACK)
        right_searches = right_score.get_rect()
        right_searches.center = (screen_W / 1.3, screen_H - screen_H / 1.8)



        if score > high_score:
            high_score = score

        imagecorrect = pygame.image.load("../HigherLower/images/correct.png")
        image_correct = imagecorrect.get_rect()
        image_correct.center = (screen_W / 2, screen_H / 2.8)

        imagewrong = pygame.image.load("../HigherLower/images/wrong.png")
        image_wrong = imagewrong.get_rect()
        image_wrong.center = (screen_W / 2, screen_H / 2.8)
        right_english = font_text.render(english[right], True, BLACK)
        right_english_text = right_english.get_rect()
        right_english_text.center = (screen_W / 1.3, screen_H - screen_H / 1.5)

        if pause is True:

            pygame.time.wait(4000)
            display_buttons = True
            pause = False
            clickable = True
            if wrong is True:
                pygame.time.wait(1000)
                game = False
                final = True
        if correct is True:
            screen.blit(imagecorrect, image_correct)
            screen.blit(right_score, right_searches)
            pause = True
            correct = False

        elif wrong is True:
            screen.blit(imagewrong, image_wrong)
            screen.blit(right_score, right_searches)
            pause = True


        Button1 = Higher.get_rect()
        Button2 = Lower.get_rect()
        screen_click = screen.get_rect()
        if display_buttons is True:
            rect1 = pygame.draw.rect(screen, GREEN, (1250, 400, 250, 80))
            rect2 = pygame.draw.rect(screen, RED, (1250, 550, 250, 80))


            Button1.center = (screen_W / 1.3, screen_H - screen_H / 1.95)
            screen.blit(Higher, Button1)

            Button2.center = (screen_W / 1.3, screen_H - screen_H / 2.9)
            screen.blit(Lower, Button2)

        if new_word is True and pause is False:
            left = right
            if new_game is True:
                left = checkiffilled(visited)
                new_game = False

            right = checkiffilled(visited)
            new_word = False

        left_text = font_text.render(spanish[left], True, BLACK)
        left_english = font_text.render(english[left], True, BLACK)
        left_score = font_text.render(searches[left] + " búsquedas", True, BLACK)
        right_text = font_text.render(spanish[right], True, BLACK)

        left_word = left_text.get_rect()
        left_word.center = (screen_W / 4, screen_H - screen_H / 1.3)
        screen.blit(left_text, left_word)

        left_english_text = left_english.get_rect()
        left_english_text.center = (screen_W / 4, screen_H - screen_H / 1.5)
        screen.blit(left_english, left_english_text)

        left_searches = left_score.get_rect()
        left_searches.center = (screen_W / 4, screen_H - screen_H / 1.8)
        screen.blit(left_score, left_searches)


        right_word = right_text.get_rect()
        right_word.center = (screen_W / 1.3, screen_H - screen_H / 1.3)
        screen.blit(right_text, right_word)

        score_text = score_current.get_rect()
        score_text.center = (screen_W / 1.1, screen_H - screen_H / 15)
        screen.blit(score_current, score_text)

        score_number = score_display.get_rect()
        score_number.center = (screen_W / 1.07, screen_H - screen_H / 15)
        screen.blit(score_display, score_number)

        highscore_text = highscore_display.get_rect()
        highscore_text.center = (screen_W / 1.2, screen_H - screen_H / 15)
        screen.blit(highscore_display, highscore_text)

        highscore_number = highscore.get_rect()
        highscore_number.center = (screen_W / 1.25, screen_H - screen_H / 15)
        screen.blit(highscore, highscore_number)

        screen.blit(right_english, right_english_text)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                intro = False
                rules = False
                game = False
                final = False
            if clickable:
                if event.type == pygame.MOUSEBUTTONUP:

                    if rect1.collidepoint(pos):  # higher

                        if int(searches[right]) >= int(searches[left]):
                            correct = True
                            score += 1
                        else:
                            wrong = True
                        new_word = True
                        display_buttons = False
                        clickable = False


                    elif rect2.collidepoint(pos):  # lower

                        if int(searches[left]) >= int(searches[right]):
                            correct = True
                            score += 1
                        else:
                            wrong = True
                        new_word = True
                        display_buttons = False
                        clickable = False


    while final:
        pos = pygame.mouse.get_pos()
        screen.fill(WHITE)
        font_title = pygame.font.SysFont("arial bold", 80)
        title_text = font_title.render("Your score: "+str(score), True, BLACK)
        highscore_text = font_title.render("High score: "+str(high_score), True, BLACK)
        play_again = font_title.render("Play again", True, BLACK)

        font_title = pygame.font.SysFont("arial bold", 60)
        play_text = font_title.render("Play again", True, BLACK)


        textRect2 = title_text.get_rect()
        textRect2.center = (screen_W / 2, screen_H - screen_H / 1.4)
        screen.blit(title_text, textRect2)

        textRect3 = title_text.get_rect()
        textRect3.center = (screen_W / 2, screen_H - screen_H / 1.7)
        screen.blit(highscore_text, textRect3)

        textRect4 = title_text.get_rect()
        textRect4.center = (screen_W / 2, screen_H - screen_H / 2.5)
        screen.blit(play_again, textRect4)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                intro = False
                rules = False
                game = False
                final = False
            if event.type == pygame.MOUSEBUTTONUP:
                if textRect4.collidepoint(pos):
                    final = False
                    game = True
                    loop = True


pygame.quit()
sys.exit()
