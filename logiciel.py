import pygame
pygame.init()

# Fenêtre
largeur = 400
hauteur = 400
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("logiciel de dessin")
noir = pygame.Color(0, 0, 0)
screen.fill(noir)

running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE :
                running = False

pygame.quit()