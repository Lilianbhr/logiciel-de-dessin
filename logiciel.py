import pygame
pygame.init()

# Fenêtre
largeur = 400
hauteur = 400
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("logiciel de dessin")
blanc = pygame.Color(255, 255, 255)
screen.fill(blanc)