import pygame
pygame.init()

# Fenêtre
largeur = 400
hauteur = 400
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("logiciel de dessin")
noir = pygame.Color(0, 0, 0)
blanc = pygame.Color(255, 255, 255)
screen.fill(blanc)

running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE :
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            debut_ligne = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            fin_ligne = pygame.mouse.get_pos()
            pygame.draw.line(screen, noir, debut_ligne, fin_ligne, 1)
        pygame.display.flip()

pygame.quit()