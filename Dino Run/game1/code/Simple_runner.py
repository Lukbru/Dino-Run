import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400)) # tworzenia okna
pygame.display.set_caption('Dino Run') # nazywanie okna
clock = pygame.time.Clock() # timer do framerate
test_font = pygame.font.Font(None,60)
game_active = True

sky_surface = pygame.image.load('graphics\sky.png').convert()
ground_surface = pygame.image.load('graphics\ground.png').convert()

text_surface = test_font.render('Dino Run', False, (64,64,64) )
text_rect = text_surface.get_rect(center = (400,50))

enemy1_surface = pygame.image.load('graphics\enemy1.png').convert_alpha()
enemy1_rect = enemy1_surface.get_rect(midbottom = (800,200))

player_surface = pygame.image.load('graphics\player_run1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0

while True:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         pygame.quit()
         exit()
        if game_active:
          if event.type == pygame.MOUSEBUTTONDOWN:
              if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                player_gravity = -20
          if event.type == pygame.KEYDOWN :
              if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                enemy1_rect.left = 800

    if game_active:
     screen.blit(sky_surface,(0,0)) # allows overlaping images + miejsce na oknie
     screen.blit(ground_surface, (0, 300))
     pygame.draw.rect(screen, '#c0e8ec', text_rect)
     pygame.draw.rect(screen,'#c0e8ec',text_rect,6)
     screen.blit(text_surface, text_rect)

     enemy1_rect.x -= 4
     if enemy1_rect.right <= 0:  enemy1_rect.left = 800

     screen.blit(enemy1_surface, enemy1_rect)

     player_gravity += 1
     player_rect.y += player_gravity
     if player_rect.bottom >= 300: player_rect.bottom = 300
     screen.blit(player_surface, player_rect)

     if enemy1_rect.colliderect(player_rect):
        game_active = False
    else:
        screen.fill('Black')

    pygame.display.update() # okno caly czas dziala
    clock.tick(60) #framerate
