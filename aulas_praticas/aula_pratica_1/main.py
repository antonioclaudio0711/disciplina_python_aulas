import pygame
from pygame import Surface, Rect

WINDOW_WIDTH = 576
WINDOW_HEIGHT = 324

# Inicializar o módulo do PyGame
pygame.init()

# Criação de janela do PyGame
window: Surface = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

# Carregar imagem e gerar uma superfície
bg_surf: Surface = pygame.image.load('./asset/bg.png').convert_alpha()
player1_surf: Surface = pygame.image.load('./asset/player1.png').convert_alpha()

# Obter o retângulo da superfície
bg_rect: Rect = bg_surf.get_rect(left=0, top=0)
player1_rect: Rect = player1_surf.get_rect(left=100, top=100)

# Desenhar a imagem na janela (window)
window.blit(source=bg_surf, dest=bg_rect)
window.blit(source=player1_surf, dest=player1_rect)

# Atualizar a janela
pygame.display.flip()

# Colocar um relógio no nosso jogo
clock = pygame.time.Clock()

# Carregar música e deixá-la tocando
pygame.mixer_music.load('./asset/fase1.mp3')
pygame.mixer_music.play(-1)
pygame.mixer_music.set_volume(0.2)

while True:
    clock.tick(140)  # Esse loop está acontecendo a uma taxa de 140 quadros por segundo
    # print(f'{clock.get_fps():.0f}') ---> Mostrar ao usuário a taxa de quadros por segundo (FPS)

    window.blit(source=bg_surf, dest=bg_rect)
    window.blit(source=player1_surf, dest=player1_rect)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_w]:
        player1_rect.centery -= 1
    if pressed_key[pygame.K_s]:
        player1_rect.centery += 1
    if pressed_key[pygame.K_a]:
        player1_rect.centerx -= 1
    if pressed_key[pygame.K_d]:
        player1_rect.centerx += 1
        pass
