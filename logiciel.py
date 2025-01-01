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
current_color = couleur["noir"]
epaisseur = 1
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE :
                running = False
            elif event.key == pygame.K_r:
                current_color = couleur["rouge"]
            elif event.key == pygame.K_v:
                current_color = couleur["vert"]
            elif event.key == pygame.K_b:
                current_color = couleur["bleu"]
            elif event.key == pygame.K_n:
                current_color = couleur["noir"]
            elif event.key == pygame.K_p:
                epaisseur += 1
            elif event.key == pygame.K_m:
                epaisseur -= 1
                if epaisseur < 1 :
                    epaisseur = 1
            elif event.key == pygame.K_s:
                name = input("entrez le nom du fichier : ")
                pygame.image.save(screen, f"saved/{name}.png")
        elif event.type == pygame.MOUSEMOTION:
            fin_ligne = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed() == (1, 0, 0):
                pygame.draw.line(screen, current_color, debut_ligne, fin_ligne, epaisseur)
            debut_ligne = fin_ligne
        pygame.display.flip()

pygame.quit()