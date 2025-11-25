import pygame
import os

class Grille:
    def __init__(self, tile_size=60):
        self.display_surface = pygame.display.get_surface()
        self.tile_size = tile_size
        self.cols = self.display_surface.get_width() // tile_size
        self.rows = self.display_surface.get_height() // tile_size
        self.colors = {
            0: None,              # Vide (transparent)
            
            # 1. SOL / HERBE / PENTES (Bloc 1 à 30)
            1: (139, 69, 19),     # Sol (Terre)
            2: (34, 139, 34),     # Herbe Top
            3: (34, 139, 34),     # Herbe Bottom
            
            # 2. OBJETS / DÉCOR FIXE (Bloc 31 à 40)
            31: (139, 69, 19),    # Arbre
            
            # 3. NUAGES (Bloc 41 à 50)
            41: (169, 169, 169),  # Nuage 0
            42: (169, 169, 169),  # Nuage 1.1
            43: (169, 169, 169),  # Nuage 1.2
            44: (169, 169, 169),  # Nuage 1.3
            
            # 4. AUTRES (Bloc 51 et suivants)
            51: (255, 215, 0),    # Pièce (or)
            52: (255, 0, 0),      # Ennemi (rouge)
        }
        
        self.images = {}
        self.load_images()
        
    def load_images(self):
        print("=" * 50)
        print("DEBUT DU CHARGEMENT DES IMAGES")
        print(f"Dossier actuel: {os.getcwd()}")
        print("=" * 50)
        
        try:
            print("\nContenu du dossier Image/Decors:")
            decors_path = os.path.join("Image", "Decors")
            for item in os.listdir(decors_path):
                print(f"  - {item}")
                if os.path.isdir(os.path.join(decors_path, item)):
                    print(f"    Contenu de {item}:")
                    for file in os.listdir(os.path.join(decors_path, item)):
                        print(f"      * {file}")
        except Exception as e:
            print(f"ERREUR lecture Image/Decors: {e}")
        
        print("\n" + "=" * 50)
        print("TENTATIVE DE CHARGEMENT:")
        print("=" * 50)
        
        image_files = {
            # 1. SOL / HERBE / PENTES (1 à 7)
            1: [os.path.join("Image", "Decors", "Sol", "Sol.png"), os.path.join("Image", "Decors", "Sol", "Sol.png")], # Sol (Terre)
            1.1: [os.path.join("Image", "Decors", "Sol", "Sol2.png"), os.path.join("Image", "Decors", "Sol", "Sol2.png")], # Sol (Terre)
            3: [os.path.join("Image", "Decors", "Herbe", "HerbeTop.png"), os.path.join("Image", "Decors", "Herbe", "HerbeTop.png")], # Herbe Top
            4: [os.path.join("Image", "Decors", "Herbe", "HerbeBottom.png"), os.path.join("Image", "Decors", "Herbe", "HerbeBottom.png")], # Herbe Bottom
            4.1: [os.path.join("Image", "Decors", "Herbe", "HerbeBottom2.png"), os.path.join("Image", "Decors", "Herbe", "HerbeBottom2.png")], # Herbe Bottom
            
            # 2. OBJETS / DÉCOR FIXE (31)
            31: [os.path.join("Image", "Decors", "Arbre", "Arbre0.png"), os.path.join("Image", "Decors", "Arbre", "Arbre0.png")], # Arbre
            
            # 3. NUAGES (41 à 44)
            41: [os.path.join("Image", "Decors", "Nuage", "Nuage0.png"), os.path.join("Image", "Decors", "Nuage", "Nuage0.png")], # Nuage 0
            41.1: [os.path.join("Image", "Decors", "Nuage", "Nuage1.1.png"), os.path.join("Image", "Decors", "Nuage", "Nuage1.1.png")], # Nuage 1.1
            41.2: [os.path.join("Image", "Decors", "Nuage", "Nuage1.2.png"), os.path.join("Image", "Decors", "Nuage", "Nuage1.2.png")], # Nuage 1.2
            41.3: [os.path.join("Image", "Decors", "Nuage", "Nuage1.3.png"), os.path.join("Image", "Decors", "Nuage", "Nuage1.3.png")], # Nuage 1.3
            
            # 4. AUTRES (51 à 52)
            51: [os.path.join("Image", "piece.png"), os.path.join("Image", "piece.png")], # Pièce
            52: [os.path.join("Image", "ennemi.png"), os.path.join("Image", "ennemi.png")], # Ennemi
        }
        
        for tile_type, paths in image_files.items():
            loaded = False
            for image_path in paths:
                print(f"\nTile {tile_type}: Test de '{image_path}'")
                print(f"  Fichier existe? {os.path.exists(image_path)}")
                try:
                    image = pygame.image.load(image_path).convert_alpha()
                    image = pygame.transform.scale(image, (self.tile_size, self.tile_size))
                    self.images[tile_type] = image
                    print(f"  ✓✓✓ SUCCES ✓✓✓")
                    loaded = True
                    break
                except (pygame.error, FileNotFoundError) as e:
                    print(f"  ✗ Echec: {e}")
                    continue
            
            if not loaded:
                self.images[tile_type] = None
                print(f"  ►►► Tile {tile_type}: AUCUNE IMAGE TROUVEE - couleur de secours")
        
        print("\n" + "=" * 50)
        print("FIN DU CHARGEMENT")
        print("=" * 50)
    
    def draw_grid(self, show_numbers=False):
        for row in range(self.rows + 1):
            pygame.draw.line(
                self.display_surface,
                (200, 200, 200),
                (0, row * self.tile_size),
                (self.display_surface.get_width(), row * self.tile_size),
                1
            )
        
        for col in range(self.cols + 1):
            pygame.draw.line(
                self.display_surface,
                (200, 200, 200),
                (col * self.tile_size, 0),
                (col * self.tile_size, self.display_surface.get_height()),
                1
            )
        
        if show_numbers:
            font = pygame.font.Font(None, 20)
            for row in range(self.rows):
                for col in range(self.cols):
                    text = font.render(f"{col},{row}", True, (150, 150, 150))
                    self.display_surface.blit(text, (col * self.tile_size + 5, row * self.tile_size + 5))

    def draw_level(self, level_data, show_borders=True, offset_x=0):
        # Paramètre 'offset_x' ajouté : C'est le décalage horizontal (world_shift) envoyé par Niveau1.
        
        for row_index, row in enumerate(level_data):
            for col_index, tile_type in enumerate(row):
                
                if tile_type != 0: 
                    
                    # 2. Calcul des positions de base (Coordonnées MONDE)
                    x = col_index * self.tile_size
                    y = row_index * self.tile_size
                    
                    # 3. Calcul de la position de dessin (Coordonnées ÉCRAN)
                    # La position finale à l'écran = position monde + décalage du monde.
                    final_x = x + offset_x
                    
                    # 4. OPTIMISATION : Ne pas dessiner les tuiles hors-champ. 
                    # Si la tuile est complètement à droite OU si elle est complètement à gauche.
                    if final_x > self.display_surface.get_width() or final_x + self.tile_size < 0:
                        continue # Passe à la tuile suivante sans exécuter le code de dessin.
                    
                    
                    # 5. Dessiner l'image (si elle existe)
                    if self.images.get(tile_type):
                        # On utilise la position 'final_x' pour décaler l'image.
                        self.display_surface.blit(self.images[tile_type], (final_x, y)) 
                    
                    # 6. Dessiner la couleur de secours (si image manquante)
                    else:
                        color = self.colors.get(tile_type, (255, 255, 255))
                        pygame.draw.rect(
                            self.display_surface,
                            color,
                            # On utilise 'final_x' pour décaler le rectangle.
                            (final_x, y, self.tile_size, self.tile_size)
                        )
                    
                    # 7. Dessiner la bordure (si show_borders est True)
                    if show_borders:
                        pygame.draw.rect(
                            self.display_surface,
                            (0, 0, 0),
                            # On utilise 'final_x' pour décaler la bordure.
                            (final_x, y, self.tile_size, self.tile_size),
                            2
                        )
    def get_tile_at_position(self, x, y):
        col = x // self.tile_size
        row = y // self.tile_size
        return (col, row)
    
    def get_position_from_tile(self, col, row):
        x = col * self.tile_size
        y = row * self.tile_size
        return (x, y)