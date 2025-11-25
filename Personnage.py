import pygame
import os

class Joueur:
    
    def __init__(self, x, y, grille=None):
        self.display_surface = pygame.display.get_surface()
        self.grille = grille
        
        self.x = float(x)
        self.y = float(y)
        
        self.width = 40
        self.height = 50
        
        self.speed = 5
        self.jump_power = 10
        self.gravity = 0.8
        self.max_fall_speed = 15
        
        self.velocity_x = 0
        self.velocity_y = 0
        self.on_ground = False
        
        self.facing_right = True
        
        self.animations = {
            'idle_right': [],
            'idle_left': [],
            'walk_right': [],
            'walk_left': [],
            'jump_right': [], 
            'jump_left': []    
        }
        
        self.current_animation = 'idle_right'
        self.animation_index = 0
        self.animation_speed = 0.15
        
        self.load_animations()
        
        self.color = (255, 100, 100)
    
    def load_animations(self):
        animation_path = os.path.join("Image", "Joueur")
        
        idle_files = ['Immobile1.png', 'Immobile2.png']
        
        walk_files = ['Immobile1.png', 'Immobile2.png'] 
        
        jump_files = ['Saut1.png', 'Saut2.png']
        
        def load_and_mirror(files_list, right_key, left_key):
            for filename in files_list:
                try:
                    img_path = os.path.join(animation_path, filename)
                    image = pygame.image.load(img_path).convert_alpha()
                    image = pygame.transform.scale(image, (self.width, self.height))
                    self.animations[right_key].append(image)
                    
                    flipped_image = pygame.transform.flip(image, True, False)
                    self.animations[left_key].append(flipped_image)
                except:
                    pass

        load_and_mirror(idle_files, 'idle_right', 'idle_left')
        load_and_mirror(walk_files, 'walk_right', 'walk_left')
        load_and_mirror(jump_files, 'jump_right', 'jump_left')
        
        if self.animations['idle_right']:
            print(f"Animations loaded: {len(self.animations['idle_right'])} idle, {len(self.animations['walk_right'])} walk, {len(self.animations['jump_right'])} jump")
        else:
            print("No animations found - fallback rectangle used")
    
    def handle_input(self, keys):
        self.velocity_x = 0
        
        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.velocity_x = -self.speed
            self.facing_right = False
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.velocity_x = self.speed
            self.facing_right = True
        
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_z]) and self.on_ground:
            self.velocity_y = -self.jump_power
            self.on_ground = False
    
    def set_animation_state(self):
        
        if not self.on_ground:
            if self.facing_right:
                self.current_animation = 'jump_right'
            else:
                self.current_animation = 'jump_left'
        
        else:
            if self.velocity_x != 0:
                if self.facing_right:
                    self.current_animation = 'walk_right'
                else:
                    self.current_animation = 'walk_left'
            else:
                if self.facing_right:
                    self.current_animation = 'idle_right'
                else:
                    self.current_animation = 'idle_left'

    
    def apply_gravity(self):
        self.velocity_y += self.gravity
        if self.velocity_y > self.max_fall_speed:
            self.velocity_y = self.max_fall_speed
    
    def animate(self):
        animation = self.animations[self.current_animation]
        
        if len(animation) > 0:
            self.animation_index += self.animation_speed
            
            if self.animation_index >= len(animation):
                self.animation_index = 0
    
    def update(self, keys, level_data=None):
        self.handle_input(keys)
        self.apply_gravity()
        
        self.set_animation_state() 
        self.animate()
        
        self.x += self.velocity_x
        
        if level_data and self.grille:
            self.check_horizontal_collisions(level_data)
        
        self.y += self.velocity_y
        
        if level_data and self.grille:
            self.check_vertical_collisions(level_data)
        
        screen_width = self.display_surface.get_width()
        screen_height = self.display_surface.get_height()
        
        #if self.x < 0:
            #self.x = 0
        #if self.x + self.width > screen_width:
            #self.x = screen_width - self.width
        
        if self.y > screen_height:
            self.y = 0
            self.velocity_y = 0
    
    def check_horizontal_collisions(self, level_data):
        rect = self.get_rect()
        solid_tiles = [1, 1.1, 2, 3] 
        
        if self.velocity_x > 0:
            right_top_col = rect.right // self.grille.tile_size
            right_top_row = (rect.top + 5) // self.grille.tile_size
            right_bottom_col = rect.right // self.grille.tile_size
            right_bottom_row = (rect.bottom - 5) // self.grille.tile_size
            
            if self.is_solid_tile(level_data, right_top_row, right_top_col, solid_tiles) or \
               self.is_solid_tile(level_data, right_bottom_row, right_bottom_col, solid_tiles):
                self.x = right_top_col * self.grille.tile_size - self.width - 1
        
        elif self.velocity_x < 0:
            left_top_col = rect.left // self.grille.tile_size
            left_top_row = (rect.top + 5) // self.grille.tile_size
            left_bottom_col = rect.left // self.grille.tile_size
            left_bottom_row = (rect.bottom - 5) // self.grille.tile_size
            
            if self.is_solid_tile(level_data, left_top_row, left_top_col, solid_tiles) or \
               self.is_solid_tile(level_data, left_bottom_row, left_bottom_col, solid_tiles):
                self.x = (left_top_col + 1) * self.grille.tile_size + 1
    
    def check_vertical_collisions(self, level_data):
        rect = self.get_rect()
        solid_tiles = [1,1.1, 2, 3]
        
        if self.velocity_y > 0:
            bottom_left_col = (rect.left + 5) // self.grille.tile_size
            bottom_left_row = rect.bottom // self.grille.tile_size
            bottom_right_col = (rect.right - 5) // self.grille.tile_size
            bottom_right_row = rect.bottom // self.grille.tile_size
            
            if self.is_solid_tile(level_data, bottom_left_row, bottom_left_col, solid_tiles) or \
               self.is_solid_tile(level_data, bottom_right_row, bottom_right_col, solid_tiles):
                self.y = bottom_left_row * self.grille.tile_size - self.height
                self.velocity_y = 0
                self.on_ground = True
            else:
                self.on_ground = False
        
        elif self.velocity_y < 0:
            top_left_col = (rect.left + 5) // self.grille.tile_size
            top_left_row = rect.top // self.grille.tile_size
            top_right_col = (rect.right - 5) // self.grille.tile_size
            top_right_row = rect.top // self.grille.tile_size
            
            if self.is_solid_tile(level_data, top_left_row, top_left_col, solid_tiles) or \
               self.is_solid_tile(level_data, top_right_row, top_right_col, solid_tiles):
                self.y = (top_left_row + 1) * self.grille.tile_size
                self.velocity_y = 0
    
    def is_solid_tile(self, level_data, row, col, solid_tiles):

        if 0 <= row < len(level_data) and 0 <= col < len(level_data[0]):
            return level_data[row][col] in solid_tiles
        return False
    

    def get_rect(self):
        return pygame.Rect(int(self.x), int(self.y), self.width, self.height)
    

    def get_rect_display(self, offset_x=0, offset_y=0):
        # Utiliser self.x (position monde) + offset_x
        return pygame.Rect(int(self.x + offset_x), int(self.y + offset_y), self.width, self.height)
    
    def display(self, offset_x=0):
        rect = self.get_rect_display(offset_x=offset_x)
        
        animation = self.animations[self.current_animation]
        
        if len(animation) > 0:
            image = animation[int(self.animation_index)]
            self.display_surface.blit(image, rect)  
        else:
            
            pygame.draw.rect(self.display_surface, self.color, rect)
            
            
            eye_color = (255, 255, 255)
            if self.facing_right:
                pygame.draw.circle(self.display_surface, eye_color, 
                                 (rect.centerx + 8, rect.centery - 5), 4)
            else:
                pygame.draw.circle(self.display_surface, eye_color, 
                                 (rect.centerx - 8, rect.centery - 5), 4)