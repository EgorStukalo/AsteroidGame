import random

import pygame
import pygame.freetype
pygame.init()
window = pygame.display.set_mode([1000,700])
ball = pygame.rect.Rect([500,100],[50,50])
enemy = pygame.rect.Rect([950, 100],[20,200])
player = pygame.rect.Rect([50, 100],[20,200])
#pygame.draw.ellipse(window,[11,122,233],ball)
#pygame.display.update()
a = 0
text = pygame.freetype.Font("items/BodoniFLF-Roman.ttf", 120)
score_text = pygame.freetype.Font("items/BodoniFLF-Roman.ttf", 30)
hit_sound = pygame.mixer.Sound("items/jojo-punch.mp3")
#score_sound = pygame.mixer.Sound("")
game_end_sound = pygame.mixer.Sound("items/to_be_continued.mp3")
background_sound = pygame.mixer.Sound("items/background_sound_pingpong.mp3")
finish = 0
speedx = 3
speedy = 3.8286348347
enemy_speedy = 3.8286348347
time = pygame.time.Clock()
ochki = pygame.image.load("items/2933534184626(2)-new-1000x1000.webp")

x = 100
player_score = 0
enemy_score = 0
score_change = 0
background_sound.play(-1)
while a == 0:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            a = 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                finish = 0
                player_score = 0
                enemy_score = 0

    if finish != 1:

        ball.x += speedx
        if ball.right >= 1000:
            speedx = -3
        if ball.x <= 0:
            speedx = 3

        ball.y += speedy
        if ball.bottom >= 700:
            speedy = -3.8286348347
        if ball.y <= 0:
            speedy = 3.8286348347


        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            player.y += -3
        if pressed[pygame.K_s]:
            player.y += 3
        if pressed[pygame.K_a]:
            player.x += -3
        if pressed[pygame.K_d]:
            player.x += 3
        if pressed[pygame.K_f]:
            x = 1
        else:
            x = 100

    if ball.colliderect(player):
        speedx = -speedx + 2
        hit_sound.play()



    if enemy.y <= 0:
        enemy_speedy = 0
    if enemy.y >= 700:
        enemy_speedy = 0

    if ball.colliderect(enemy):
        speedx = speedx -2
        hit_sound.play()

    if speedx > 0:
        if ball.centery > enemy.centery and speedy > 0:
            enemy.y += 3
        if ball.centery < enemy.centery and speedy < 0:
            enemy.y += -3

    if ball.right >= 1000:
        ball.x = 500
        player_score += 1
        score_change = 1

    if ball.x <= 0:
        ball.x = 500
        enemy_score += 1
        score_change = 1



    window.fill([123, 234, 255])
    pygame.draw.rect(window, [0, 15, 255], enemy)
    pygame.draw.rect(window, [255, 15, 255], player)
    pygame.draw.ellipse(window, [11, 122, 233], ball)

    if score_change == 1:
        print("Игрок-",player_score," ","Противник-",enemy_score)
        print(" ")
        score_text.render_to(window, [20, 600], "player has "+str(player_score)+" points",[0,0,0])
        score_text.render_to(window, [700, 600], "enemy has " + str(enemy_score) + " points", [0, 0, 0])

    if enemy_score == 5:
        if finish == 0:
            game_end_sound.play()
            background_sound.stop()
        finish = 1
        text.render_to(window, [250, 280], "enemy won", [random.randint(1,255), random.randint(1,255), random.randint(1,255)])
        x = 7
    if player_score == 2:
        if finish == 0:
            game_end_sound.play()
            background_sound.stop()
        finish = 1
        text.render_to(window, [250, 280], "player won", [random.randint(1,255), random.randint(1,255), random.randint(1,255)])
        x = 7


    pygame.display.set_caption(str(time.get_fps()))
    pygame.display.update()
    time.tick(x)

