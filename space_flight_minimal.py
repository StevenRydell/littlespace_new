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
BULLET_COLOR = (100, 200, 255)  # Light blue
BULLET_LENGTH = 6
BULLET_WIDTH = 3

# Mouse control settings
MAX_ROTATION_PER_FRAME = 4.0  # Maximum degrees of rotation per frame

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
    def __init__(self, x, y, velocity_x, velocity_y, angle, color=None):
        self.x = x
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.angle = angle  # Store angle for drawing orientation
        self.color = color if color else BULLET_COLOR  # Use provided color or default
    
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
        
        # Draw bullet as a line (color depends on who shot it)
        arcade.draw_line(start_x, start_y, end_x, end_y, self.color, width)

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
    
    def update(self, delta_time, keys_pressed):
        # Clamp delta_time to prevent issues with large time steps
        delta_time = min(delta_time, 0.1)  # Max 100ms per frame
        
        # Handle rotation (keyboard only)
        if arcade.key.LEFT in keys_pressed:
            self.angle -= ROTATION_SPEED * delta_time
        if arcade.key.RIGHT in keys_pressed:
            self.angle += ROTATION_SPEED * delta_time
        
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


class EnemyShip:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity_x = 0
        self.velocity_y = 0
        self.angle = 0  # 0 = pointing up
        self.size = SHIP_SIZE
        
        # AI state
        self.thrusting_forward = False
        self.thrusting_backward = False
        
        # Shooting state
        self.shoot_cooldown = 0.0
        self.min_shoot_interval = 0.8  # Minimum time between shots
        self.max_shoot_interval = 2.5  # Maximum time between shots
        self.next_shoot_time = 0.0  # When enemy can shoot next
        self.last_player_distance = 0  # Track player distance for shooting decisions
        
        # AI parameters
        self.follow_distance = 100  # Preferred distance from player
        self.turn_speed = ROTATION_SPEED * 0.8  # Slightly slower than player
        self.separation_distance = 150  # Minimum distance from other enemies
        self.collision_radius = self.size * 3  # Absolute no-touch zone (triple ship size)
    
    def update(self, delta_time, player, other_enemies=None):
        # Clamp delta_time to prevent issues with large time steps
        delta_time = min(delta_time, 0.1)  # Max 100ms per frame
        
        # Calculate distance and angle to player
        dx_to_player = player.x - self.x
        dy_to_player = player.y - self.y
        distance_to_player = math.sqrt(dx_to_player*dx_to_player + dy_to_player*dy_to_player)
        
        # Calculate separation force from other enemies
        separation_x = 0
        separation_y = 0
        emergency_avoidance = False
        
        if other_enemies:
            for other_enemy in other_enemies:
                if other_enemy != self:  # Don't separate from self
                    dx_to_other = self.x - other_enemy.x
                    dy_to_other = self.y - other_enemy.y
                    distance_to_other = math.sqrt(dx_to_other*dx_to_other + dy_to_other*dy_to_other)
                    
                    if distance_to_other > 0:  # Avoid division by zero
                        # Emergency collision avoidance - absolute priority
                        if distance_to_other < self.collision_radius:
                            emergency_avoidance = True
                            # Very strong emergency force
                            emergency_force = 10.0 * (self.collision_radius - distance_to_other) / self.collision_radius
                            separation_x += (dx_to_other / distance_to_other) * emergency_force
                            separation_y += (dy_to_other / distance_to_other) * emergency_force
                        # Normal separation force
                        elif distance_to_other < self.separation_distance:
                            force_strength = (self.separation_distance - distance_to_other) / self.separation_distance
                            separation_x += (dx_to_other / distance_to_other) * force_strength
                            separation_y += (dy_to_other / distance_to_other) * force_strength
        
        # Combine player following with separation
        if emergency_avoidance:
            # In emergency mode, ONLY avoid collision - ignore player
            desired_x = separation_x
            desired_y = separation_y
        else:
            # Normal mode - combine following and separation
            follow_strength = 0.4  # Further reduced follow strength
            separation_strength = 8.0  # Even stronger separation force
            
            desired_x = dx_to_player * follow_strength + separation_x * separation_strength
            desired_y = dy_to_player * follow_strength + separation_y * separation_strength
        
        # Calculate angle toward desired direction
        if abs(desired_x) > 0.01 or abs(desired_y) > 0.01:  # Avoid division by zero
            target_angle = math.degrees(math.atan2(desired_x, desired_y))
        else:
            # If no clear direction, just face the player
            target_angle = math.degrees(math.atan2(dx_to_player, dy_to_player))
        
        # Calculate shortest rotation direction
        angle_diff = target_angle - self.angle
        while angle_diff > 180:
            angle_diff -= 360
        while angle_diff < -180:
            angle_diff += 360
        
        # Rotate toward player
        if abs(angle_diff) > 5:  # Only rotate if not close enough
            rotation_speed = self.turn_speed * delta_time
            if abs(angle_diff) < rotation_speed:
                self.angle = target_angle
            else:
                if angle_diff > 0:
                    self.angle += rotation_speed
                else:
                    self.angle -= rotation_speed
        
        # Keep angle in range
        self.angle = self.angle % 360
        
        # Convert angle to radians for physics
        angle_rad = math.radians(self.angle)
        
        # AI movement logic
        if distance_to_player > self.follow_distance:
            # Too far - move toward player
            self.thrusting_forward = True
            self.thrusting_backward = False
        elif distance_to_player < self.follow_distance * 0.5:
            # Too close - back away
            self.thrusting_forward = False
            self.thrusting_backward = True
        else:
            # Good distance - stop thrusting
            self.thrusting_forward = False
            self.thrusting_backward = False
        
        # Apply thrust
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
        
        # Clamp velocities
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
            self.velocity_x = 0
            self.velocity_y = 0
        
        # Update position
        try:
            new_x = self.x + self.velocity_x * delta_time
            new_y = self.y + self.velocity_y * delta_time
            
            if not (math.isnan(new_x) or math.isnan(new_y) or 
                    math.isinf(new_x) or math.isinf(new_y)):
                self.x = new_x
                self.y = new_y
        except (ValueError, OverflowError):
            pass
        
        # Keep within world bounds
        self.x = max(0, min(self.x, WORLD_WIDTH))
        self.y = max(0, min(self.y, WORLD_HEIGHT))
        
        # Update shoot cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= delta_time
        
        # Store player distance for shooting decisions
        self.last_player_distance = distance_to_player
    
    def can_shoot(self, player, current_time):
        # Basic cooldown check
        if self.shoot_cooldown > 0:
            return False
        
        # Calculate factors that influence shooting decision
        distance_to_player = self.last_player_distance
        
        # Don't shoot if player is too far away (waste of ammo)
        if distance_to_player > 200:
            return False
        
        # Calculate how well we're aimed at the player
        dx_to_player = player.x - self.x
        dy_to_player = player.y - self.y
        player_angle = math.degrees(math.atan2(dx_to_player, dy_to_player))
        
        # Normalize angle difference
        angle_diff = abs(player_angle - self.angle)
        while angle_diff > 180:
            angle_diff = 360 - angle_diff
        
        # Better aim = higher chance to shoot
        if angle_diff < 10:  # Very good aim
            shoot_chance = 0.8
        elif angle_diff < 30:  # Good aim
            shoot_chance = 0.4
        elif angle_diff < 60:  # Decent aim
            shoot_chance = 0.1
        else:  # Poor aim
            shoot_chance = 0.02
        
        # Distance factor - closer = more likely to shoot
        distance_factor = max(0.3, 1.0 - (distance_to_player / 200.0))
        shoot_chance *= distance_factor
        
        # Random element for varied timing
        import random
        return random.random() < shoot_chance
    
    def shoot(self, target_player):
        # Set cooldown with random variation
        import random
        self.shoot_cooldown = random.uniform(self.min_shoot_interval, self.max_shoot_interval)
        
        # Calculate bullet spawn position at tip of ship
        ship_angle_rad = math.radians(self.angle)
        bullet_x = self.x + math.sin(ship_angle_rad) * self.size
        bullet_y = self.y + math.cos(ship_angle_rad) * self.size
        
        # Calculate shooting angle with predictive targeting
        import random
        
        # 70% chance for predictive targeting, 30% for direct aiming
        use_prediction = random.random() < 0.7
        
        if use_prediction:
            # Calculate where player will be when bullet arrives
            distance_to_player = math.sqrt((target_player.x - bullet_x)**2 + (target_player.y - bullet_y)**2)
            time_to_target = distance_to_player / BULLET_SPEED
            
            # Predict player position
            predicted_x = target_player.x + target_player.velocity_x * time_to_target
            predicted_y = target_player.y + target_player.velocity_y * time_to_target
            
            # Aim at predicted position
            dx_to_target = predicted_x - bullet_x
            dy_to_target = predicted_y - bullet_y
        else:
            # Direct aiming (current position)
            dx_to_target = target_player.x - bullet_x
            dy_to_target = target_player.y - bullet_y
        
        shooting_angle = math.degrees(math.atan2(dx_to_target, dy_to_target))
        shooting_angle_rad = math.radians(shooting_angle)
        
        # Calculate bullet velocity using direct aim angle
        bullet_velocity_x = math.sin(shooting_angle_rad) * BULLET_SPEED
        bullet_velocity_y = math.cos(shooting_angle_rad) * BULLET_SPEED
        
        # Enemy bullets are red
        enemy_bullet_color = (255, 50, 50)  # Red
        return Bullet(bullet_x, bullet_y, bullet_velocity_x, bullet_velocity_y, shooting_angle, enemy_bullet_color)
    
    def draw(self, camera_x, camera_y, game_window=None):
        # Draw thruster first (behind ship)
        self.draw_thruster(camera_x, camera_y, game_window)
        
        # Calculate triangle points (same as player)
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
            rotated_points.append((final_x, final_y))
        
        border_thickness = BORDER_THICKNESS
        
        # Draw filled triangle (red color for enemy)
        enemy_fill_color = (255, 100, 100, 128)  # Red tint
        enemy_border_color = (255, 100, 100, 255)  # Red border
        
        arcade.draw_polygon_filled(rotated_points, enemy_fill_color)
        arcade.draw_polygon_outline(rotated_points, enemy_border_color, border_thickness)
    
    def draw_thruster(self, camera_x, camera_y, game_window=None):
        angle_rad = math.radians(self.angle)
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)
        
        # Forward thruster (same as player)
        if self.thrusting_forward:
            gap = 1.5
            thruster_length = THRUSTER_LENGTH
            thruster_width = THRUSTER_WIDTH
            
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
                rotated_thruster.append((final_x, final_y))
            
            reverse_color = (100, 150, 255, 180)  # Blue for reverse
            arcade.draw_polygon_filled(rotated_thruster, reverse_color)
    
    def check_collision_with_bullet(self, bullet):
        """Check if bullet collides with this enemy ship"""
        try:
            # Simple distance-based collision
            distance = math.sqrt((self.x - bullet.x)**2 + (self.y - bullet.y)**2)
            return distance <= self.size
        except Exception:
            return False


class SpaceFlightGame(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, "Little Space - Minimal Flight", resizable=True)
        arcade.set_background_color(arcade.color.BLACK)
        
        # Show the mouse cursor (no longer using mouse for controls)
        self.set_mouse_visible(True)
        
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
        self.enemies = []  # Keep old enemies for compatibility
        self.enemy_ships = []  # Multiple enemy ships
        self.enemy_bullets = []  # Enemy bullets
        self.max_enemy_ships = 2  # Maximum number of enemy ships
        
        # Mouse control variables (for shooting only)
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
        
        # Spawn initial enemies
        self.spawn_enemy()  # Old enemy system
        
        # Spawn initial enemy ships (2 of them)
        for _ in range(self.max_enemy_ships):
            self.spawn_enemy_ship()
    
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
    
    def spawn_enemy_ship(self):
        """Spawn an enemy ship near the player"""
        import random
        
        if not self.player or len(self.enemy_ships) >= self.max_enemy_ships:
            return
        
        # Spawn enemy ship at a distance from player
        angle = random.uniform(0, 2 * math.pi)
        distance = 150 + random.uniform(-50, 50)  # Vary distance slightly
        
        enemy_x = self.player.x + math.cos(angle) * distance
        enemy_y = self.player.y + math.sin(angle) * distance
        
        # Keep within world bounds
        enemy_x = max(50, min(enemy_x, WORLD_WIDTH - 50))
        enemy_y = max(50, min(enemy_y, WORLD_HEIGHT - 50))
        
        new_enemy = EnemyShip(enemy_x, enemy_y)
        self.enemy_ships.append(new_enemy)
    
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
        
        # Draw enemy ships
        for enemy_ship in self.enemy_ships:
            enemy_ship.draw(self.camera.x, self.camera.y, self)
        
        # Draw enemy bullets
        for bullet in self.enemy_bullets:
            bullet.draw(self.camera.x, self.camera.y, self)
        
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
        
        # Pure keyboard controls - no mouse steering
        
        # Update player with safety check
        try:
            self.player.update(delta_time, self.keys_pressed)
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
        
        # Update enemy ships
        enemy_ships_to_remove = []
        for i, enemy_ship in enumerate(self.enemy_ships):
            try:
                # Pass all enemy ships for separation behavior
                enemy_ship.update(delta_time, self.player, self.enemy_ships)
                
                # Enemy shooting with intelligent timing
                if enemy_ship.can_shoot(self.player, delta_time):
                    enemy_bullet = enemy_ship.shoot(self.player)
                    if enemy_bullet:
                        self.enemy_bullets.append(enemy_bullet)
            except Exception:
                # If enemy ship update fails, mark for removal
                enemy_ships_to_remove.append(i)
        
        # Remove failed enemy ships
        for i in sorted(enemy_ships_to_remove, reverse=True):
            if 0 <= i < len(self.enemy_ships):
                self.enemy_ships.pop(i)
        
        # Update enemy bullets
        try:
            enemy_bullets_to_remove = []
            for i, bullet in enumerate(self.enemy_bullets):
                if bullet and hasattr(bullet, 'update'):
                    bullet.update(delta_time)
                    if hasattr(bullet, 'is_off_screen') and bullet.is_off_screen():
                        enemy_bullets_to_remove.append(i)
            
            # Remove off-screen enemy bullets
            for i in sorted(enemy_bullets_to_remove, reverse=True):
                if 0 <= i < len(self.enemy_bullets):
                    self.enemy_bullets.pop(i)
                    
        except Exception:
            # Clear problematic enemy bullets
            self.enemy_bullets = [b for b in self.enemy_bullets if b and hasattr(b, 'x')]
        
        # Check collisions between player bullets and enemy ships
        bullets_to_remove = []
        enemy_ships_to_remove = []
        
        for bullet_idx, bullet in enumerate(self.bullets):
            if not bullet:
                continue
                
            for enemy_idx, enemy_ship in enumerate(self.enemy_ships):
                if enemy_ship and enemy_ship.check_collision_with_bullet(bullet):
                    bullets_to_remove.append(bullet_idx)
                    enemy_ships_to_remove.append(enemy_idx)
                    break  # Bullet can only hit one enemy
        
        # Remove bullets that hit enemy ships
        for i in sorted(set(bullets_to_remove), reverse=True):
            if 0 <= i < len(self.bullets):
                self.bullets.pop(i)
        
        # Remove destroyed enemy ships
        for i in sorted(set(enemy_ships_to_remove), reverse=True):
            if 0 <= i < len(self.enemy_ships):
                self.enemy_ships.pop(i)
        
        # Spawn new enemy ships to maintain the count
        while len(self.enemy_ships) < self.max_enemy_ships:
            self.spawn_enemy_ship()
        
        # Check collisions between enemy bullets and player (no damage for now)
        try:
            enemy_bullets_to_remove = []
            for i, bullet in enumerate(self.enemy_bullets):
                if bullet and self.player:
                    # Simple distance-based collision with player
                    distance = math.sqrt((self.player.x - bullet.x)**2 + (self.player.y - bullet.y)**2)
                    if distance <= self.player.size:
                        enemy_bullets_to_remove.append(i)
                        # TODO: Add player damage/destruction here later
                        # For now, just remove the bullet
            
            # Remove enemy bullets that hit player
            for i in sorted(enemy_bullets_to_remove, reverse=True):
                if 0 <= i < len(self.enemy_bullets):
                    self.enemy_bullets.pop(i)
                    
        except Exception:
            # Clear problematic collisions
            pass
        
        # Update camera to follow player
        self.camera.follow_player(self.player.x, self.player.y)
        self.camera.update(delta_time)
    
    def on_key_press(self, key, modifiers):
        self.keys_pressed.add(key)
        
        # Handle fullscreen toggle
        if key == arcade.key.F:
            self.toggle_fullscreen()
        
        # Handle escape key to exit
        if key == arcade.key.ESCAPE:
            self.close()
    
    def on_key_release(self, key, modifiers):
        self.keys_pressed.discard(key)
    
    def on_mouse_motion(self, x, y, dx, dy):
        """Mouse motion handler (no longer used for controls)"""
        pass
    
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