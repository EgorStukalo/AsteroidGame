import random
import settings
import pygame
import pygame.freetype


class Starship:
    def __init__(self):
        self.image = pygame.image.load("items/Right_starsheep.png")
        x = self.image.get_width()
        y = self.image.get_height()
        self.image = pygame.transform.scale(self.image,[x/13,y/13])
        x = self.image.get_width()
        y = self.image.get_height()
        self.hitbox = pygame.rect.Rect([150,350],[x,y])
        self.hitbox_for_collisions_with_meteors_and_any_other_objects = pygame.rect.Rect([150,350],[x/2,y/2])
        self.hp = 3
        self.number_of_destroyed_meteors = 0

    def drawing(self, window):
        #pygame.draw.rect(window,[15,255,20],self.hitbox_for_collisions_with_meteors_and_any_other_objects)
        window.blit(self.image, self.hitbox)

    def ehaing(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.hitbox.y += -3
        if pressed[pygame.K_s]:
            self.hitbox.y += 3
        if pressed[pygame.K_a]:
            self.hitbox.x += -3
        if pressed[pygame.K_d]:
            self.hitbox.x += 3
        self.hitbox_for_collisions_with_meteors_and_any_other_objects.center = self.hitbox.center

class Lasers:
    def __init__(self, posx, posy):
        self.image = pygame.image.load("items/lasers.png")
        x = self.image.get_width()
        y = self.image.get_height()
        self.image = pygame.transform.scale(self.image, [x / 8, y / 8])
        self.image = pygame.transform.rotate(self.image, -90)
        self.hitbox = pygame.rect.Rect([posx, posy], self.image.get_size())
        self.hitbox_for_collisions = pygame.rect.Rect([posx, posy], [x/6,y/20])
        self.speed = 9
    def drawing(self, window):
        #pygame.draw.rect(window, [15, 255, 20], self.hitbox_for_collisions)
        window.blit(self.image, self.hitbox)

    def ehaing(self):
        self.hitbox.x += self.speed
        self.hitbox_for_collisions.center = self.hitbox.center

class Meteors:
    def __init__(self):
        self.image = pygame.image.load("items/Meteors.png")
        x = self.image.get_width()
        y = self.image.get_height()
        a = random.uniform(7.5,14.1)
        self.image = pygame.transform.scale(self.image, [x / a, y / a])
        x = self.image.get_width()
        y = self.image.get_height()
        #self.image = pygame.transform.rotate(self.image, -90)
        self.hitbox = pygame.rect.Rect([settings.WIDTH, random.randint(0 , settings.HEIGHT - y)], self.image.get_size())
        self.speedx = random.randint(-5,-2)
        self.speedy = random.randint(-1,1)

    def drawing(self, window):
        window.blit(self.image, self.hitbox)

    def ehaing(self):
        self.hitbox.x += self.speedx
        self.hitbox.y += self.speedy

class Heart:
    def __init__(self, pos_x, pos_y):
        self.image = pygame.image.load("items/Heart.png")
        x = self.image.get_width()
        y = self.image.get_height()
        self.image = pygame.transform.scale(self.image, [x / 4, y / 4])
        self.hitbox = pygame.rect.Rect([pos_x, pos_y], [x / 2, y / 2])

    def drawing(self, window):
        window.blit(self.image, self.hitbox)

class Button:
    def __init__(self, pos_x, pos_y,picture,text):
        self.image = picture
        self.text = text
        x = self.image.get_width()
        y = self.image.get_height()
        self.hitbox = pygame.rect.Rect([pos_x, pos_y], [x, y])
        self.font = pygame.freetype.Font("items/BodoniFLF-Roman.ttf",40)
        self.image_and_hitbox = self.font.render(text)
        self.image_and_hitbox[1].center = self.hitbox.center

    def drawing(self, window):
        window.blit(self.image, self.hitbox)
        window.blit(self.image_and_hitbox[0], self.image_and_hitbox[1])

