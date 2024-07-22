import pygame
import settings as s
import sprite as sp
import pygame.freetype
pygame.init()

def collision_of_a_spaceship_with_a_meteor():
    for meteor in meteor_list:
        if starship.hitbox_for_collisions_with_meteors_and_any_other_objects.colliderect(meteor.hitbox):
            meteor_list.remove(meteor)
            starship.hp -= 1

def collision_of_a_laser_with_a_meteor():
    for meteor in meteor_list:
        for laser in laser_list:
            if laser.hitbox_for_collisions.colliderect(meteor.hitbox):
                meteor_list.remove(meteor)
                laser_list.remove(laser)
                starship.number_of_destroyed_meteors += 1
                break
time_now = 0
text = pygame.freetype.Font("items/BodoniFLF-Roman.ttf",16)
time_since_a_laser_spawned = 0
background_menu = pygame.image.load("items/menu image.jpg")
background_menu = pygame.transform.scale(background_menu, [s.WIDTH, s.HEIGHT])
game_mode = 0
background = pygame.image.load("items/Stars.png")
laser_sound = pygame.mixer.Sound("items/Космические коты - звук лазера.wav")
laser_sound.set_volume(0.33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333)
background_sound = pygame.mixer.Sound("items/Космические коты - музыка.wav")
background_sound.set_volume(0.3)
background = pygame.transform.scale(background, [s.WIDTH, s.HEIGHT])
window = pygame.display.set_mode([s.WIDTH, s.HEIGHT])
starship = sp.Starship()
hearts = []
pos_x = -50
for hp in range(0, starship.hp):
    pos_x += 50
    heart = sp.Heart(pos_x, 0)
    hearts.append(heart)
button_green = pygame.image.load("items/PNG/UI/buttonGreen.png")
button_green = pygame.transform.scale(button_green, [200, 70])
button_resume = sp.Button(400,300,button_green,"resume")

button_yellow = pygame.image.load("items/PNG/UI/buttonYellow.png")
button_yellow = pygame.transform.scale(button_yellow, [200, 70])
button_new = sp.Button(400,400,button_yellow,"new game")

button_red = pygame.image.load("items/PNG/UI/buttonRed.png")
button_red = pygame.transform.scale(button_red, [200, 70])
button_quit = sp.Button(400,500,button_red,"quit")

pygame.display.update()
a = 0
laser_list = []
meteor_list = []
time = pygame.time.Clock()
meteor_event = pygame.USEREVENT
pygame.time.set_timer(meteor_event, 300)
background_sound.play(-1)
while a == 0:
    time_now = pygame.time.get_ticks()
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            a = 1
        if event.type == pygame.MOUSEBUTTONDOWN and time_now - time_since_a_laser_spawned >= 400 and game_mode != 1:
            time_since_a_laser_spawned = time_now
            laser = sp.Lasers(starship.hitbox.centerx, starship.hitbox.centery-27)
            laser_list.append(laser)
            laser_sound.play()

        if event.type == meteor_event and game_mode == 0:
            meteor = sp.Meteors()
            meteor_list.append(meteor)

        if event.type == pygame.MOUSEBUTTONDOWN and game_mode == 1:
            if button_new.hitbox.collidepoint(event.pos):
                game_mode = 0
                starship.hp = 3
                starship.hitbox.x = 150
                starship.hitbox.y = 350
                meteor_list = []
                laser_list = []
            if button_quit.hitbox.collidepoint(event.pos):
                a = 1

            if button_resume.hitbox.collidepoint(event.pos):
                game_mode = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_mode = not game_mode


    if game_mode == 0:
        starship.ehaing()

        for laser in laser_list:
            laser.ehaing()
        for meteor in meteor_list:
            meteor.ehaing()
        collision_of_a_spaceship_with_a_meteor()
        collision_of_a_laser_with_a_meteor()
        if starship.hp <= 0:
            game_mode = 1
        window.blit(background,[0,0])
        pygame.display.set_caption(str(time.get_fps()))
        for heart in hearts[0:starship.hp]:
            heart.drawing(window)
        starship.drawing(window)
        for laser in laser_list:
            laser.drawing(window)
        for meteor in meteor_list:
            meteor.drawing(window)

        text.render_to(window,[0,650],"you destroyed "+str(starship.number_of_destroyed_meteors)+" meteors", [255,255,255])


    else:
        window.blit(background_menu, [0, 0])
        button_resume.drawing(window)
        button_new.drawing(window)
        button_quit.drawing(window)
    pygame.display.update()
    time.tick(150)
