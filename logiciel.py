import pygame
pygame.init()

couleur = {
    "noir" : pygame.Color(0, 0, 0),
    "blanc" : pygame.Color(255, 255, 255),
    "rouge" : pygame.Color(255, 0, 0),
    "vert" : pygame.Color(0, 255, 0),
    "bleu" : pygame.Color(0, 0, 255)
}

# Fenêtre
largeur = 400
hauteur = 400
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("logiciel de dessin")
screen.fill(couleur["blanc"])

running = True
debut_ligne = (0, 0)
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE :
                running = False
        elif event.type == pygame.MOUSEMOTION:
            fin_ligne = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed() == (1, 0, 0):
                pygame.draw.line(screen, couleur["noir"], debut_ligne, fin_ligne, 1)
            debut_ligne = fin_ligne
        pygame.display.flip()

pygame.quit()