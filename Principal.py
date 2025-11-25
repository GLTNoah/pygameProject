import pygame
import sys
import os
from Menu import Menu
from Menu import Font
from Niveau_1 import Niveau1

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Game dev")
        self.screen = pygame.display.set_mode((1080, 960))
        self.clock = pygame.time.Clock()
        
        curseur_path = os.path.join("Image", "Interface", "Curseur.png") 
        try:
            self.curseur_image = pygame.image.load(curseur_path).convert_alpha()
            pygame.mouse.set_visible(False)
            print("✓ Curseur personnalisé chargé")
        except (pygame.error, FileNotFoundError):
            self.curseur_image = None
            pygame.mouse.set_visible(True)
            print(f"✗ Curseur non trouvé: {curseur_path} - curseur par défaut")
        
        self.etat = "Menu"
        self.Menu = Menu()
        self.Fond = Font()
        self.Niveau1 = None

    def run(self):
        
        if self.curseur_image:
            pygame.mouse.set_visible(False)
            
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if self.etat == "Menu":
                    action = self.Menu.Click_Boutons(event)
                    
                    if action == "Jouer": 
                        print("Lancement du niveau 1...")
                        self.etat = "Niveau1"
                        self.Niveau1 = Niveau1()
                        
                    elif action == "Quitter":
                        pygame.quit()
                        sys.exit()
                        
                    elif action == "Scores":
                        print("Scores...")
                        
                    elif action == "Options":
                        print("Options...")
                
                elif self.etat == "Niveau1":
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:  
                            print("Retour au menu...")
                            self.etat = "Menu"
                            self.Niveau1 = None
                        elif event.key == pygame.K_g and self.Niveau1:
                            self.Niveau1.toggle_grid()
                            print(f"Grille: {'ON' if self.Niveau1.show_grid else 'OFF'}")
            
            self.screen.fill((0, 0, 0))
            
            if self.etat == "Menu":
                self.Fond.display()        
                self.Menu.display()
                
            elif self.etat == "Niveau1":
                if self.Niveau1:
                    keys = pygame.key.get_pressed()
                    self.Niveau1.update(keys) 
                    self.Niveau1.display()     
            self.curseur()
            pygame.display.update()
            self.clock.tick(60)

    def curseur(self):

        if self.curseur_image:
            x, y = pygame.mouse.get_pos()
            rect = self.curseur_image.get_rect(center=(x, y))
            self.screen.blit(self.curseur_image, rect)
    
if __name__ == "__main__":
    Game().run()