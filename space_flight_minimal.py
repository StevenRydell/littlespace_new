import arcade
import math

# Screen and world settings
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 360
SCREEN_SCALE = 2
WINDOW_WIDTH = SCREEN_WIDTH * SCREEN_SCALE
WINDOW_HEIGHT = SCREEN_HEIGHT * SCREEN_SCALE

# World is larger than screen for exploration
WORLD_WIDTH = 2000
WORLD_HEIGHT = 2000

# Physics variables (from flight_old_variables.md)
ACCELERATION = 240
FRICTION = 0.995
MAX_SPEED = 50
MAX_REVERSE_SPEED = 50
ROTATION_SPEED = 90

# Ship appearance
SHIP_SIZE = 3.75
BORDER_THICKNESS = 1
SHIP_FILL_COLOR = (255, 255, 255, 128)
SHIP_BORDER_COLOR = (255, 255, 255, 255)

# Thruster settings
THRUSTER_LENGTH = 5
THRUSTER_WIDTH = 4
THRUSTER_COLOR = (255, 100, 50, 180)
SHOW_REVERSE_THRUSTER = True
REVERSE_THRUSTER_LENGTH = 4

# Shooting settings
BULLET_SPEED = 200
BULLET_COOLDOWN = 0.5
BULLET_COLOR = (255, 0, 0)  # Red
BULLET_LENGTH = 6
BULLET_WIDTH = 3

# Enemy settings
ENEMY_SPAWN_DISTANCE = 200
ENEMY_MIN_SIZE = 5
ENEMY_MAX_SIZE = 15
ENEMY_CIRCLE_COLOR = (255, 100, 100)  # Light red
ENEMY_SQUARE_COLOR = (100, 100, 255)  # Light blue

class Enemy:
    def __init__(self, x, y, enemy_type, size):
        self.x = x
        self.y = y
        self.type = enemy_type  # "circle" or "square"
        self.size = size
    
    def draw(self, camera_x, camera_y, game_window=None):
        screen_x = (self.x - camera_x) * SCREEN_SCALE
        screen_y = (self.y - camera_y) * SCREEN_SCALE
        screen_size = self.size * SCREEN_SCALE
        
        # Simple drawing without transformations
        
        if self.type == "circle":
            arcade.draw_circle_filled(screen_x, screen_y, screen_size, ENEMY_CIRCLE_COLOR)
        elif self.type == "square":
            # Draw square as polygon
            half_size = screen_size
            square_points = [
                (screen_x - half_size, screen_y - half_size),
                (screen_x + half_size, screen_y - half_size),
                (screen_x + half_size, screen_y + half_size),
                (screen_x - half_size, screen_y + half_size)
            ]
            arcade.draw_polygon_filled(square_points, ENEMY_SQUARE_COLOR)
    
    def check_collision_with_bullet(self, bullet):
        """Check if bullet collides with this enemy"""
        try:
            if self.type == "circle":
                # Circle collision - distance from center
                distance = math.sqrt((self.x - bullet.x)**2 + (self.y - bullet.y)**2)
                return distance <= self.size
            elif self.type == "square":
                # Square collision - check if bullet is within square bounds
                half_size = self.size
                return (abs(bullet.x - self.x) <= half_size and 
                        abs(bullet.y - self.y) <= half_size)
        except Exception:
            # If any error occurs, assume no collision
            return False
        return False

class Bullet:
    def __init__(self, x, y, velocity_x, velocity_y, angle):
        self.x = x
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.angle = angle  # Store angle for drawing orientation
    
    def update(self, delta_time):
        self.x += self.velocity_x * delta_time
        self.y += self.velocity_y * delta_time
    
    def is_off_screen(self):
        return (self.x < 0 or self.x > WORLD_WIDTH or 
                self.y < 0 or self.y > WORLD_HEIGHT)
    
    def draw(self, camera_x, camera_y, game_window=None):
        screen_x = (self.x - camera_x) * SCREEN_SCALE
        screen_y = (self.y - camera_y) * SCREEN_SCALE
        
        # Calculate line endpoints based on bullet angle and length
        angle_rad = math.radians(self.angle)
        half_length = BULLET_LENGTH / 2
        
        # Start and end points of the line
        start_x = screen_x - math.sin(angle_rad) * half_length * SCREEN_SCALE
        start_y = screen_y - math.cos(angle_rad) * half_length * SCREEN_SCALE
        end_x = screen_x + math.sin(angle_rad) * half_length * SCREEN_SCALE
        end_y = screen_y + math.cos(angle_rad) * half_length * SCREEN_SCALE
        
        # Simple drawing without transformations
        width = BULLET_WIDTH
        
        # Draw bullet as a red line
        arcade.draw_line(start_x, start_y, end_x, end_y, BULLET_COLOR, width)

class Star:
    def __init__(self, x, y, size, opacity):
        self.x = x
        self.y = y
        self.size = size
        self.opacity = opacity
    
    def draw(self, camera_x, camera_y, game_window=None):
        color = (255, 255, 255, int(255 * self.opacity))
        screen_x = (self.x - camera_x) * SCREEN_SCALE
        screen_y = (self.y - camera_y) * SCREEN_SCALE
        
        # Simple drawing without complex transformations
        size = self.size * SCREEN_SCALE
            
        arcade.draw_circle_filled(screen_x, screen_y, size, color)

class StarField:
    def __init__(self, width, height, star_count=300):  # Increased for more dense starfield
        self.stars = []
        self.generate_stars(width, height, star_count)
    
    def generate_stars(self, width, height, star_count):
        import random
        for _ in range(star_count):
            x = random.randint(0, width)
            y = random.randint(0, height)
            
            # 80% small dim stars, 20% bright larger stars
            if random.random() < 0.8:
                size = 1.0
                opacity = 0.6
            else:
                size = 1.5
                opacity = 1.0
            
            self.stars.append(Star(x, y, size, opacity))
    
    def draw(self, camera_x, camera_y, game_window=None):
        # Only draw stars that are visible on screen
        left = camera_x
        right = camera_x + SCREEN_WIDTH
        bottom = camera_y
        top = camera_y + SCREEN_HEIGHT
        
        for star in self.stars:
            if (star.x >= left and star.x <= right and 
                star.y >= bottom and star.y <= top):
                star.draw(camera_x, camera_y, game_window)

class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.target_x = 0
        self.target_y = 0
        self.smoothing = 0.1
    
    def follow_player(self, player_x, player_y):
        # Center camera on player
        self.target_x = player_x - SCREEN_WIDTH // 2
        self.target_y = player_y - SCREEN_HEIGHT // 2
        
        # Keep camera within world bounds
        self.target_x = max(0, min(self.target_x, WORLD_WIDTH - SCREEN_WIDTH))
        self.target_y = max(0, min(self.target_y, WORLD_HEIGHT - SCREEN_HEIGHT))
    
    def update(self, delta_time):
        # Smooth camera movement
        self.x += (self.target_x - self.x) * self.smoothing
        self.y += (self.target_y - self.y) * self.smoothing

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity_x = 0
        self.velocity_y = 0
        self.angle = 0  # 0 = pointing up
        self.size = SHIP_SIZE
        
        # Thruster state
        self.thrusting_forward = False
        self.thrusting_backward = False
        
        # Shooting state
        self.shoot_cooldown = 0.0
    
    def update(self, delta_time, keys_pressed, target_angle=None):
        # Clamp delta_time to prevent issues with large time steps
        delta_time = min(delta_time, 0.1)  # Max 100ms per frame
        
        # Handle rotation (keyboard)
        if arcade.key.LEFT in keys_pressed:
            self.angle -= ROTATION_SPEED * delta_time
        if arcade.key.RIGHT in keys_pressed:
            self.angle += ROTATION_SPEED * delta_time
        
        # Handle rotation (mouse steering)
        if target_angle is not None:
            # Calculate the shortest rotation direction
            angle_diff = target_angle - self.angle
            
            # Normalize angle difference to [-180, 180]
            while angle_diff > 180:
                angle_diff -= 360
            while angle_diff < -180:
                angle_diff += 360
            
            # Rotate toward target angle with smooth rotation speed
            rotation_speed = ROTATION_SPEED * 2  # Make mouse steering faster
            if abs(angle_diff) < rotation_speed * delta_time:
                # Close enough, snap to target
                self.angle = target_angle
            else:
                # Rotate in the correct direction
                if angle_diff > 0:
                    self.angle += rotation_speed * delta_time
                else:
                    self.angle -= rotation_speed * delta_time
        
        # Keep angle in reasonable range to prevent overflow
        self.angle = self.angle % 360
        
        # Convert angle to radians
        angle_rad = math.radians(self.angle)
        
        # Handle thrust
        self.thrusting_forward = arcade.key.UP in keys_pressed or arcade.key.W in keys_pressed
        self.thrusting_backward = arcade.key.DOWN in keys_pressed or arcade.key.S in keys_pressed
        
        if self.thrusting_forward:
            thrust_x = math.sin(angle_rad) * ACCELERATION * delta_time
            thrust_y = math.cos(angle_rad) * ACCELERATION * delta_time
            self.velocity_x += thrust_x
            self.velocity_y += thrust_y
        
        if self.thrusting_backward:
            thrust_x = -math.sin(angle_rad) * ACCELERATION * delta_time
            thrust_y = -math.cos(angle_rad) * ACCELERATION * delta_time
            self.velocity_x += thrust_x
            self.velocity_y += thrust_y
        
        # Apply friction
        self.velocity_x *= FRICTION
        self.velocity_y *= FRICTION
        
        # Clamp velocities to prevent runaway values
        self.velocity_x = max(-1000, min(1000, self.velocity_x))
        self.velocity_y = max(-1000, min(1000, self.velocity_y))
        
        # Apply speed limits
        try:
            current_speed = math.sqrt(self.velocity_x**2 + self.velocity_y**2)
            if current_speed > MAX_SPEED and current_speed > 0:
                scale = MAX_SPEED / current_speed
                self.velocity_x *= scale
                self.velocity_y *= scale
        except (ValueError, ZeroDivisionError):
            # Reset velocities if calculation fails
            self.velocity_x = 0
            self.velocity_y = 0
        
        # Update position with bounds checking
        try:
            new_x = self.x + self.velocity_x * delta_time
            new_y = self.y + self.velocity_y * delta_time
            
            # Validate new positions are reasonable
            if not (math.isnan(new_x) or math.isnan(new_y) or 
                    math.isinf(new_x) or math.isinf(new_y)):
                self.x = new_x
                self.y = new_y
        except (ValueError, OverflowError):
            # Keep current position if calculation fails
            pass
        
        # Keep within world bounds
        self.x = max(0, min(self.x, WORLD_WIDTH))
        self.y = max(0, min(self.y, WORLD_HEIGHT))
        
        # Update shoot cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= delta_time
    
    def draw(self, camera_x, camera_y, game_window=None):
        # Draw thruster first (behind ship)
        self.draw_thruster(camera_x, camera_y, game_window)
        
        # Calculate triangle points
        angle_rad = math.radians(self.angle)
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)
        
        # Triangle points (pointing up)
        original_points = [
            (0, self.size),                        # Top point
            (-self.size * 0.8, -self.size * 0.6),  # Bottom left
            (self.size * 0.8, -self.size * 0.6)    # Bottom right
        ]
        
        # Rotate and translate points
        rotated_points = []
        for px, py in original_points:
            rotated_x = px * cos_a + py * sin_a
            rotated_y = -px * sin_a + py * cos_a
            final_x = (self.x + rotated_x - camera_x) * SCREEN_SCALE
            final_y = (self.y + rotated_y - camera_y) * SCREEN_SCALE
            
            # No transformations needed
            
            rotated_points.append((final_x, final_y))
        
        # Simple border thickness
        border_thickness = BORDER_THICKNESS
        
        # Draw filled triangle
        arcade.draw_polygon_filled(rotated_points, SHIP_FILL_COLOR)
        
        # Draw triangle outline
        arcade.draw_polygon_outline(rotated_points, SHIP_BORDER_COLOR, border_thickness)
    
    def draw_thruster(self, camera_x, camera_y, game_window=None):
        angle_rad = math.radians(self.angle)
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)
        
        # Forward thruster
        if self.thrusting_forward:
            gap = 1.5
            thruster_length = THRUSTER_LENGTH
            thruster_width = THRUSTER_WIDTH
            
            # Trapezoidal thruster shape
            top_width = thruster_width
            bottom_width = thruster_width * 0.8
            
            thruster_points = [
                (-top_width * 0.5, -self.size * 0.6 - gap),
                (top_width * 0.5, -self.size * 0.6 - gap),
                (bottom_width * 0.5, -self.size * 0.6 - gap - thruster_length),
                (-bottom_width * 0.5, -self.size * 0.6 - gap - thruster_length)
            ]
            
            # Rotate and translate thruster points
            rotated_thruster = []
            for px, py in thruster_points:
                rotated_x = px * cos_a + py * sin_a
                rotated_y = -px * sin_a + py * cos_a
                final_x = (self.x + rotated_x - camera_x) * SCREEN_SCALE
                final_y = (self.y + rotated_y - camera_y) * SCREEN_SCALE
                
                # No transformations needed
                
                rotated_thruster.append((final_x, final_y))
            
            arcade.draw_polygon_filled(rotated_thruster, THRUSTER_COLOR)
        
        # Reverse thruster
        if self.thrusting_backward and SHOW_REVERSE_THRUSTER:
            gap = 1.5
            thruster_length = REVERSE_THRUSTER_LENGTH
            thruster_width = THRUSTER_WIDTH * 0.8
            
            top_width = thruster_width
            bottom_width = thruster_width * 0.8
            
            thruster_points = [
                (-top_width * 0.5, -self.size * 0.6 - gap),
                (top_width * 0.5, -self.size * 0.6 - gap),
                (bottom_width * 0.5, -self.size * 0.6 - gap - thruster_length),
                (-bottom_width * 0.5, -self.size * 0.6 - gap - thruster_length)
            ]
            
            rotated_thruster = []
            for px, py in thruster_points:
                rotated_x = px * cos_a + py * sin_a
                rotated_y = -px * sin_a + py * cos_a
                final_x = (self.x + rotated_x - camera_x) * SCREEN_SCALE
                final_y = (self.y + rotated_y - camera_y) * SCREEN_SCALE
                
                # No transformations needed
                
                rotated_thruster.append((final_x, final_y))
            
            reverse_color = (100, 150, 255, 180)  # Blue for reverse
            arcade.draw_polygon_filled(rotated_thruster, reverse_color)
    
    def can_shoot(self):
        return self.shoot_cooldown <= 0
    
    def shoot(self):
        if not self.can_shoot():
            return None
        
        # Reset cooldown
        self.shoot_cooldown = BULLET_COOLDOWN
        
        # Calculate bullet spawn position at exact tip of ship triangle
        angle_rad = math.radians(self.angle)
        # The tip is at the "top point" which is (0, self.size) in the triangle definition
        bullet_x = self.x + math.sin(angle_rad) * self.size
        bullet_y = self.y + math.cos(angle_rad) * self.size
        
        # Calculate bullet velocity
        bullet_velocity_x = math.sin(angle_rad) * BULLET_SPEED
        bullet_velocity_y = math.cos(angle_rad) * BULLET_SPEED
        
        return Bullet(bullet_x, bullet_y, bullet_velocity_x, bullet_velocity_y, self.angle)


class SpaceFlightGame(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, "Little Space - Minimal Flight", resizable=True)
        arcade.set_background_color(arcade.color.BLACK)
        
        # Hide the mouse cursor
        self.set_mouse_visible(False)
        
        # Set frame rate to prevent performance issues
        self.set_update_rate(1/60)  # 60 FPS limit
        
        # Create Camera2D for proper fullscreen scaling
        self.world_camera = arcade.Camera2D()
        self.gui_camera = arcade.Camera2D()
        
        self.player = None
        self.starfield = None
        self.camera = None
        self.keys_pressed = set()
        self.bullets = []
        self.enemies = []
        
        # Mouse control variables
        self.mouse_x = 0
        self.mouse_y = 0
        self.mouse_steering = True  # Enable mouse steering
        self.mouse_pressed = set()  # Track mouse button states
        
        # Performance and safety limits
        self.max_bullets = 8   # Reduced further to prevent performance issues
        self.max_enemies = 2   # Reduced to 2 for better performance
        self.collision_check_timer = 0  # Throttle collision checks
        self.draw_call_count = 0  # Track draw calls for performance monitoring
        
        # Fullscreen state (simple)
        self.is_fullscreen = False
        
        # Track base resolution for scaling
        self.base_width = WINDOW_WIDTH
        self.base_height = WINDOW_HEIGHT
        
        # HUD text objects - positioned relative to screen
        self.fps_text = arcade.Text("FPS: --", 
                                   10, 
                                   WINDOW_HEIGHT - 30, 
                                   arcade.color.GREEN, 
                                   16)
        
        # Coordinates display  
        self.coords_text = arcade.Text("X: 0 Y: 0", 
                                      10, 
                                      20, 
                                      arcade.color.WHITE, 
                                      12)
    
    def setup(self):
        # Start player in center of world
        self.player = Player(WORLD_WIDTH // 2, WORLD_HEIGHT // 2)
        self.starfield = StarField(WORLD_WIDTH, WORLD_HEIGHT)
        self.camera = Camera()
        
        # Spawn initial enemy
        self.spawn_enemy()
    
    def spawn_enemy(self):
        """Spawn a random enemy around the player"""
        import random
        
        # Limit total enemies to prevent memory issues
        if len(self.enemies) >= self.max_enemies:
            return
        
        # Safety check - ensure player exists
        if not self.player:
            return
            
        # Try multiple times to find a valid position
        for attempt in range(5):  # Max 5 attempts to prevent infinite loops
            try:
                # Random angle and distance from player
                angle = random.uniform(0, 2 * math.pi)
                distance = random.uniform(50, ENEMY_SPAWN_DISTANCE)
                
                # Calculate enemy position
                enemy_x = self.player.x + math.cos(angle) * distance
                enemy_y = self.player.y + math.sin(angle) * distance
                
                # Keep enemy within world bounds with proper margin
                margin = ENEMY_MAX_SIZE + 10  # Extra margin for safety
                enemy_x = max(margin, min(enemy_x, WORLD_WIDTH - margin))
                enemy_y = max(margin, min(enemy_y, WORLD_HEIGHT - margin))
                
                # Validate position is reasonable
                if (enemy_x > margin and enemy_x < WORLD_WIDTH - margin and 
                    enemy_y > margin and enemy_y < WORLD_HEIGHT - margin):
                    
                    # Random enemy type and size
                    enemy_type = random.choice(["circle", "square"])
                    enemy_size = random.uniform(ENEMY_MIN_SIZE, ENEMY_MAX_SIZE)
                    
                    enemy = Enemy(enemy_x, enemy_y, enemy_type, enemy_size)
                    self.enemies.append(enemy)
                    return  # Success, exit
                    
            except Exception:
                # If any error occurs, try again
                continue
        
        # If all attempts failed, just don't spawn an enemy this time
    
    def transform_coords(self, x, y):
        """Simple pass-through - no transformation to prevent performance issues"""
        return x, y
    
    def on_draw(self):
        self.clear()
        
        # Use world camera for game objects
        self.world_camera.use()
        
        # Draw starfield (background)
        self.starfield.draw(self.camera.x, self.camera.y, self)
        
        # Draw enemies
        for enemy in self.enemies:
            enemy.draw(self.camera.x, self.camera.y, self)
        
        # Draw bullets
        for bullet in self.bullets:
            bullet.draw(self.camera.x, self.camera.y, self)
        
        # Draw player ship
        self.player.draw(self.camera.x, self.camera.y, self)
        
        # Use GUI camera for HUD
        self.gui_camera.use()
        
        # Draw HUD
        self.fps_text.draw()
        self.coords_text.draw()
    
    def on_update(self, delta_time):
        # Update FPS and coordinates display
        fps_value = f"FPS: {1/delta_time:.1f}" if delta_time > 0 else "FPS: --"
        self.fps_text.text = fps_value
        
        coord_text = f"X: {int(self.player.x)} Y: {int(self.player.y)}"
        self.coords_text.text = coord_text
        
        # Handle shooting with limits (keyboard and mouse)
        shooting = (arcade.key.SPACE in self.keys_pressed or 
                   arcade.MOUSE_BUTTON_LEFT in self.mouse_pressed)
        if shooting and len(self.bullets) < self.max_bullets:
            bullet = self.player.shoot()
            if bullet:
                self.bullets.append(bullet)
        
        # Calculate target angle from mouse position
        target_angle = None
        if self.mouse_steering:
            # Convert screen coordinates to world coordinates
            world_mouse_x = (self.mouse_x / SCREEN_SCALE) + self.camera.x
            world_mouse_y = (self.mouse_y / SCREEN_SCALE) + self.camera.y
            
            # Calculate angle from player to mouse cursor
            dx = world_mouse_x - self.player.x
            dy = world_mouse_y - self.player.y
            
            # Calculate target angle in degrees (atan2 returns radians)
            target_angle = math.degrees(math.atan2(dx, dy))
        
        # Update player with safety check
        try:
            self.player.update(delta_time, self.keys_pressed, target_angle)
        except Exception:
            # Reset player if update fails
            self.player = Player(WORLD_WIDTH // 2, WORLD_HEIGHT // 2)
        
        # Update bullets and check collisions (optimized and safe)
        try:
            # Update all bullets first
            bullets_to_remove = []
            enemies_to_remove = []
            
            for i, bullet in enumerate(self.bullets):
                if bullet and hasattr(bullet, 'update'):
                    bullet.update(delta_time)
                    
                    # Check if bullet is off screen
                    if hasattr(bullet, 'is_off_screen') and bullet.is_off_screen():
                        bullets_to_remove.append(i)
            
            # Throttle collision checks to every few frames for performance
            self.collision_check_timer += delta_time
            if self.collision_check_timer >= 0.016:  # Check ~60fps max
                self.collision_check_timer = 0
                
                # Check collisions (limit checks to prevent performance issues)
                for i, bullet in enumerate(self.bullets[:self.max_bullets]):  # Limit iterations
                    if i in bullets_to_remove:
                        continue
                        
                    bullet_hit = False
                    for j, enemy in enumerate(self.enemies[:self.max_enemies]):  # Limit iterations
                        if j in enemies_to_remove:
                            continue
                            
                        try:
                            if (bullet and enemy and 
                                hasattr(enemy, 'check_collision_with_bullet') and
                                enemy.check_collision_with_bullet(bullet)):
                                
                                # Mark for removal
                                if i not in bullets_to_remove:
                                    bullets_to_remove.append(i)
                                if j not in enemies_to_remove:
                                    enemies_to_remove.append(j)
                                bullet_hit = True
                                break
                        except Exception:
                            # Skip this collision check if error occurs
                            continue
            
            # Safely remove objects (in reverse order to maintain indices)
            for i in sorted(set(bullets_to_remove), reverse=True):
                if 0 <= i < len(self.bullets):
                    self.bullets.pop(i)
            
            enemies_destroyed = 0
            for j in sorted(set(enemies_to_remove), reverse=True):
                if 0 <= j < len(self.enemies):
                    self.enemies.pop(j)
                    enemies_destroyed += 1
            
            # Spawn new enemies for destroyed ones (but not more than max)
            for _ in range(min(enemies_destroyed, self.max_enemies - len(self.enemies))):
                self.spawn_enemy()
                
        except Exception:
            # If anything goes wrong, clear problematic objects to prevent crashes
            self.bullets = [b for b in self.bullets if b and hasattr(b, 'x')]
            self.enemies = [e for e in self.enemies if e and hasattr(e, 'x')]
        
        # Update camera to follow player
        self.camera.follow_player(self.player.x, self.player.y)
        self.camera.update(delta_time)
    
    def on_key_press(self, key, modifiers):
        self.keys_pressed.add(key)
        
        # Handle fullscreen toggle
        if key == arcade.key.F:
            self.toggle_fullscreen()
    
    def on_key_release(self, key, modifiers):
        self.keys_pressed.discard(key)
    
    def on_mouse_motion(self, x, y, dx, dy):
        """Handle mouse movement for ship steering"""
        self.mouse_x = x
        self.mouse_y = y
    
    def on_mouse_press(self, x, y, button, modifiers):
        """Handle mouse button press"""
        self.mouse_pressed.add(button)
    
    def on_mouse_release(self, x, y, button, modifiers):
        """Handle mouse button release"""
        self.mouse_pressed.discard(button)
    
    def toggle_fullscreen(self):
        """Toggle between fullscreen and windowed mode"""
        self.set_fullscreen(not self.fullscreen)
    
    def on_resize(self, width, height):
        """Handle window resize with proper aspect ratio preservation"""
        super().on_resize(width, height)
        
        # Calculate aspect ratios
        game_aspect = self.base_width / self.base_height
        window_aspect = width / height
        
        if window_aspect > game_aspect:
            # Window is wider - scale by height and center horizontally
            scale = height / self.base_height
            viewport_width = self.base_width * scale
            viewport_height = height
            viewport_x = (width - viewport_width) / 2
            viewport_y = 0
        else:
            # Window is taller - scale by width and center vertically
            scale = width / self.base_width
            viewport_width = width
            viewport_height = self.base_height * scale
            viewport_x = 0
            viewport_y = (height - viewport_height) / 2
        
        # Configure world camera viewport for proper scaling
        self.world_camera.viewport_left = viewport_x
        self.world_camera.viewport_bottom = viewport_y
        self.world_camera.viewport_width = viewport_width
        self.world_camera.viewport_height = viewport_height
        
        # GUI camera uses full window
        self.gui_camera.viewport_left = 0
        self.gui_camera.viewport_bottom = 0
        self.gui_camera.viewport_width = width
        self.gui_camera.viewport_height = height
        
        # Update HUD text positions for new window size
        if self.fps_text:
            self.fps_text.x = 10
            self.fps_text.y = height - 30
        if self.coords_text:
            self.coords_text.x = 10
            self.coords_text.y = 20

def main():
    game = SpaceFlightGame()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()