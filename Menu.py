import pygame
import sys
from Cadrillage import Grille

class Menu:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.grille = Grille(tile_size=60)
        
        self.menu_decor = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 41.1, 41.2, 41.3, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 31, 0, 0],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [4, 4.1, 4, 4.1, 4.1, 4, 4, 4, 4, 4, 4, 4.1, 4, 4, 4.1, 4, 4, 4],
            [1, 1, 1, 1, 1.1, 1.1, 1.1, 1, 1, 1.1, 1, 1, 1.1, 1.1, 1, 1, 1, 1.1],
        ]
        
        self.Panneau_Buttons()
        self.Menu_Titre_Jeu()

    def Panneau_Buttons(self):
        WINDOW_WIDTH = self.display_surface.get_width()
        WINDOW_HEIGHT = self.display_surface.get_height()
        size = 200
        x = WINDOW_WIDTH // 3 - size 
        y = WINDOW_HEIGHT // 3 - size
        self.rect = pygame.Rect(x, y // 2, WINDOW_HEIGHT - size, WINDOW_WIDTH // 1.5 - size)

        marge_bouton = 20
        button_width = 150
        button_height = 75
 
        self.bouton_jouer = pygame.Rect(self.rect.x * 1.5 + marge_bouton, self.rect.y + marge_bouton, button_width, button_height * 2)
        self.bouton_options = pygame.Rect(self.rect.x / 2 + self.rect.width - button_width - marge_bouton, self.rect.y + marge_bouton, button_width, button_height * 2)
        self.bouton_quitter = pygame.Rect(self.rect.x * 1.5 + marge_bouton, self.rect.y + self.rect.height - (button_height * 2) - marge_bouton, button_width, button_height * 2)
        self.bouton_scores = pygame.Rect(self.rect.x / 2 + self.rect.width - button_width - marge_bouton, self.rect.y + self.rect.height - (button_height * 2) - marge_bouton, button_width, button_height * 2)

    def Text_Boutons(self):
        font = pygame.font.Font(None, 36)
        texte_jouer = font.render("Jouer", True, "Black")
        texte_quitter = font.render("Quitter", True, "Black")
        texte_scores = font.render("Scores", True, "Black")
        texte_options = font.render("Options", True, "Black")
        self.display_surface.blit(texte_jouer, texte_jouer.get_rect(center=self.bouton_jouer.center))
        self.display_surface.blit(texte_quitter, texte_quitter.get_rect(center=self.bouton_quitter.center))
        self.display_surface.blit(texte_scores, texte_scores.get_rect(center=self.bouton_scores.center))
        self.display_surface.blit(texte_options, texte_options.get_rect(center=self.bouton_options.center))

    def Menu_Titre_Jeu(self):
        self.titre_jeu = pygame.font.Font(None, 74)
        self.title_surface = self.titre_jeu.render("Mario de Wish", True, "White") 
        self.title_rect = self.title_surface.get_rect(center=self.rect.center)
    
    def Click_Boutons(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if self.bouton_jouer.collidepoint(pygame.mouse.get_pos()):
                print("Bouton jouer cliqué!")
                return "Jouer"
            if self.bouton_quitter.collidepoint(pygame.mouse.get_pos()):
                print("Bouton quitter cliqué!")
                return "Quitter"
            if self.bouton_scores.collidepoint(pygame.mouse.get_pos()):
                print("Bouton scores cliqué!")
                return "Scores"
            if self.bouton_options.collidepoint(pygame.mouse.get_pos()):
                print("Bouton options cliqué!")
                return "Options"
        return None
        
    def display(self):
        self.display_surface.fill((100, 206, 205))
        self.grille.draw_level(self.menu_decor, show_borders=False)
        s = pygame.Surface((self.rect.width, self.rect.height))
        s.set_alpha(200)
        s.fill((30, 30, 80))
        self.display_surface.blit(s, self.rect.topleft)
        pygame.draw.rect(self.display_surface, "White", self.rect, 3)
        self.display_surface.blit(self.title_surface, self.title_rect)  
        pygame.draw.rect(self.display_surface, "Yellow", self.bouton_jouer)
        pygame.draw.rect(self.display_surface, "Green", self.bouton_options)
        pygame.draw.rect(self.display_surface, "Red", self.bouton_quitter)
        pygame.draw.rect(self.display_surface, "Purple", self.bouton_scores)
        self.Text_Boutons()


class Font:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.Sol_Menu()
    
    def Sol_Menu(self):
        WINDOW_WIDTH = self.display_surface.get_width()
        WINDOW_HEIGHT = self.display_surface.get_height()
        size = 100
        self.sol = pygame.Rect(0, WINDOW_HEIGHT - size, WINDOW_WIDTH, size)
        
    def display(self):
        pass