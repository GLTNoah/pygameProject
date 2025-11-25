import pygame
from Cadrillage import Grille
from Personnage import Joueur

class Niveau1:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        
        # --- OPTIMISATION : Charger les éléments graphiques UNE FOIS ---
        self.text_font = pygame.font.Font(None, 36)
        self.ui_text = self.text_font.render("ESC = Menu | G = Grille | Fleches/ZQSD = Bouger | Espace = Sauter", True, "White")
        self.ui_rect = self.ui_text.get_rect(topleft=(10, 10))
        self.ui_bg = pygame.Surface((self.ui_rect.width + 10, self.ui_rect.height + 10))
        self.ui_bg.set_alpha(180)
        self.ui_bg.fill((0, 0, 0))
        
        self.grille = Grille(tile_size=60)
        
        # Position de la caméra (offset)
        self.world_shift = 0
        
        # Données du niveau (54 colonnes)
        self.level_data = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 41.1, 41.2, 41.3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 41.1, 41.2, 41.3, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 41.1, 41.2, 41.3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 41, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 31, 0, 0, 0, 0, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 31, 0, 0, 0, 0, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 31, 0, 0],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [4, 4.1, 4, 4.1, 4.1, 4, 4, 4, 4, 4, 4, 4.1, 4, 4, 4.1, 4, 4, 4, 4, 4.1, 4, 4.1, 4.1, 4, 4, 4, 4, 4, 4, 4.1, 4, 4, 4.1, 4, 4, 4, 4, 4.1, 4, 4.1, 4.1, 4, 4, 4, 4, 4, 4, 4.1, 4, 4, 4.1, 4, 4, 4],
            [1, 1, 1, 1, 1.1, 1.1, 1.1, 1, 1, 1.1, 1, 1, 1.1, 1.1, 1, 1, 1, 1.1, 1, 1, 1, 1, 1.1, 1.1, 1.1, 1, 1, 1.1, 1, 1, 1.1, 1.1, 1, 1, 1, 1.1, 1, 1, 1, 1, 1.1, 1.1, 1.1, 1, 1, 1.1, 1, 1, 1.1, 1.1, 1, 1, 1, 1.1],
        ]

        
        
        self.show_grid = False
        
        screen_width = self.display_surface.get_width()
        sol_y = 13 * 60
        start_x = screen_width // 2 - 20
        start_y = sol_y - 50
        
        self.player = Joueur(x=start_x, y=start_y, grille=self.grille)

    def toggle_grid(self):
        self.show_grid = not self.show_grid
        print(f"Grille: {'ON' if self.show_grid else 'OFF'}")

    def update(self, keys):
        # 1. Le joueur bouge normalement DANS LE MONDE (sa coordonnée x augmente/diminue)
        self.player.update(keys, self.level_data)
        
        # 2. La caméra regarde où est le joueur et se place en conséquence
        self.camera_scroll()

    def display(self):
        self.display_surface.fill((100, 206, 235))
        
        # On force un entier pour éviter le flou de mouvement
        offset_int = int(self.world_shift) #ca permet d'eviter que la camera se deplace en float (entre les pixels) et que ca creer un espece de truc saccadé
        
        self.grille.draw_level(self.level_data, show_borders=self.show_grid, offset_x=offset_int)
        
        if self.show_grid:  
            self.grille.draw_grid(show_numbers=False, offset_x=offset_int)
        
        # Le joueur est dessiné à sa position monde + le décalage caméra
        self.player.display(offset_x=offset_int)
        
        # Affichage optimisé de l'interface
        self.display_surface.blit(self.ui_bg, (5, 5))
        self.display_surface.blit(self.ui_text, self.ui_rect)

    def camera_scroll(self):
        player = self.player
        screen_width = self.display_surface.get_width()
        
        # --- 1. DEFINITION DE LA "BOITE" DE CAMÉRA ---
        # Si le joueur sort de cette zone (1/3 et 2/3), la caméra bouge
        limite_gauche = screen_width / 3
        limite_droite = screen_width - (screen_width / 3)
        
        # On calcule où se trouve le joueur SUR L'ÉCRAN
        # Position écran = Position Monde (player.x) + Décalage Caméra (world_shift)
        player_x_screen = player.x + self.world_shift
        player_center_x = player_x_screen + (player.width / 2)
        
        
        # Si le joueur pousse le bord DROIT de la caméra
        if player_center_x > limite_droite:
            # On décale le monde vers la gauche pour ramener le joueur vers la limite
            shift_amount = limite_droite - player_center_x
            self.world_shift += shift_amount
            
        # Si le joueur pousse le bord GAUCHE de la caméra
        elif player_center_x < limite_gauche:
            # On décale le monde vers la droite
            shift_amount = limite_gauche - player_center_x
            self.world_shift += shift_amount
            
        # --- 3. LIMITES DU MONDE (CLAMPING) ---
        
        TILE_SIZE = self.grille.tile_size
        NUM_COLS = len(self.level_data[0])
        WORLD_WIDTH = NUM_COLS * TILE_SIZE
        
        # Limite max (fin du niveau à droite). Valeur négative.
        MAX_SHIFT = screen_width - WORLD_WIDTH
        MIN_SHIFT = 0
        
        # On empêche la caméra de montrer le vide
        if self.world_shift > MIN_SHIFT:
            self.world_shift = MIN_SHIFT
        elif self.world_shift < MAX_SHIFT:
            self.world_shift = MAX_SHIFT
            
        #BLOCAGE PHYSIQUE DU JOUEUR (MUR INVISIBLE) ---
        #on vérifie si le joueur essaie de sortir du monde
        
        # Mur Gauche (0)
        if player.x < 0:
            player.x = 0
            
        # Mur Droit (Fin du monde)
        max_world_x = WORLD_WIDTH - player.width
        if player.x > max_world_x:
            player.x = max_world_x