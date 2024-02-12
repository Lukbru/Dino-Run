import pygame
from sys import exit
from random import randint

def show_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surface = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface,score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 200:  screen.blit(enemy1_surface,obstacle_rect)
            else :  screen.blit(enemy2_surface, obstacle_rect)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else: return []

def collision(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True

pygame.init()
screen = pygame.display.set_mode((800,400)) # tworzenia okna
pygame.display.set_caption('Dino Run') # nazywanie okna
clock = pygame.time.Clock() # timer do framerate
test_font = pygame.font.Font(None,60)
game_active = False
start_time = 0
score = 0
background_music = pygame.mixer.Sound('graphics\The Gardens.mp3')
background_music.set_volume(0.2)
background_music.play(loops = -1)

sky_surface = pygame.image.load('graphics\sky.png').convert()
ground_surface = pygame.image.load('graphics\ground.png').convert()

#text_surface = test_font.render('Dino Run', False, (64,64,64) )
#text_rect = text_surface.get_rect(center = (400,50))

#Obstacles
enemy1_surface = pygame.image.load('graphics\enemy1.png').convert_alpha()
enemy2_surface = pygame.image.load('graphics\enemy2.png').convert_alpha()

obstacle_rect_list = []

player_surface = pygame.image.load('graphics\player_run1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0
player_sound = pygame.mixer.Sound('graphics\Jump sound.mp3')
player_sound.set_volume(0.3)

#Player Game Over screen
player_stand = pygame.image.load('graphics\player_run1.png').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = test_font.render('Dino Runner',False,(160,220,240))
game_name_rect = game_name.get_rect(center = (400,80))
game_message = test_font.render('Press space to start the game',False,(160,220,240))
game_message_rect = game_message.get_rect(center = (400,320))

#Timer

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

while True:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         pygame.quit()
         exit()
        if game_active:
          if event.type == pygame.MOUSEBUTTONDOWN:
              if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                player_gravity = -20
                player_sound.play()
          if event.type == pygame.KEYDOWN :
              if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                player_gravity = -20
                player_sound.play()
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks()/1000)
        if event.type == obstacle_timer and game_active:
            if randint(0,2):
                obstacle_rect_list.append(enemy1_surface.get_rect(midbottom = (randint(800,1200),265)))
            else:
                obstacle_rect_list.append(enemy2_surface.get_rect(midbottom=(randint(800, 1200), 200)))

    if game_active:
     screen.blit(sky_surface,(0,0)) # allows overlaping images + miejsce na oknie
     screen.blit(ground_surface, (0, 300))
     #pygame.draw.rect(screen, '#c0e8ec', text_rect)
     #pygame.draw.rect(screen,'#c0e8ec',text_rect,6)
     #screen.blit(text_surface, text_rect)
     show_score()
     score = show_score()

     #enemy1_rect.x -= 4
     #if enemy1_rect.right <= 0:  enemy1_rect.left = 800
     #screen.blit(enemy1_surface, enemy1_rect)

     player_gravity += 1
     player_rect.y += player_gravity
     if player_rect.bottom >= 300: player_rect.bottom = 300
     screen.blit(player_surface, player_rect)

     #Obstacle movement
     obstacle_rect_list = obstacle_movement(obstacle_rect_list)

     game_active = collision(player_rect,obstacle_rect_list)

    else:
        screen.fill((96,142,53))
        screen.blit(player_stand,player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80,300)
        player_gravity = 0

        score_message = test_font.render(f'Your score: {score}',False,(160,220,240))
        score_message_rect = score_message.get_rect(center = (400,320))
        screen.blit(game_name,game_name_rect)
        if score == 0:
            screen.blit(game_message,game_message_rect)
        else:
            screen.blit(score_message,score_message_rect)

    pygame.display.update() # okno caly czas dziala
    clock.tick(60) #framerate
