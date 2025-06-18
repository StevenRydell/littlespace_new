import arcade
import math
import random
from camera import Camera, SCREEN_WIDTH, SCREEN_HEIGHT, WORLD_WIDTH, WORLD_HEIGHT, WINDOW_SCALE
from flight_prototype_variables import *

# Display window size (2x scale for visibility)
WINDOW_WIDTH = SCREEN_WIDTH * WINDOW_SCALE
WINDOW_HEIGHT = SCREEN_HEIGHT * WINDOW_SCALE

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity_x = 0
        self.velocity_y = 0
        self.angle = 0  # Ship rotation in degrees (0 = pointing up)
        self.size = SHIP_SIZE
        self.acceleration = ACCELERATION
        self.rotation_speed = ROTATION_SPEED
        self.friction = FRICTION
        
        # Thruster state
        self.thrusting_forward = False
        self.thrusting_backward = False
        
    def update(self, delta_time, keys_pressed):
        # Handle rotation and thrust (keyboard only)
        rotate_left = arcade.key.LEFT in keys_pressed
        rotate_right = arcade.key.RIGHT in keys_pressed
        thrust_forward = arcade.key.UP in keys_pressed
        thrust_backward = arcade.key.DOWN in keys_pressed
        
        if rotate_left:
            self.angle -= self.rotation_speed * delta_time
        if rotate_right:
            self.angle += self.rotation_speed * delta_time
            
        # Convert angle to radians for math functions
        angle_rad = math.radians(self.angle)
        
        # Handle thrust (forward/backward movement)
        self.thrusting_forward = thrust_forward
        self.thrusting_backward = thrust_backward
        
        if thrust_forward:
            # Thrust forward in the direction the ship is facing
            # When angle=0, ship points up (y+), when angle=90, ship points right (x+)
            thrust_x = math.sin(angle_rad) * self.acceleration * delta_time
            thrust_y = math.cos(angle_rad) * self.acceleration * delta_time
            self.velocity_x += thrust_x
            self.velocity_y += thrust_y
        if thrust_backward:
            # Thrust backward (reverse)
            thrust_x = -math.sin(angle_rad) * self.acceleration * delta_time
            thrust_y = -math.cos(angle_rad) * self.acceleration * delta_time
            self.velocity_x += thrust_x
            self.velocity_y += thrust_y
            
        # Apply friction
        self.velocity_x *= self.friction
        self.velocity_y *= self.friction
        
        # Apply max speed limit (different for forward and reverse)
        current_speed = math.sqrt(self.velocity_x**2 + self.velocity_y**2)
        
        # Determine if we're moving forward or backward relative to ship direction
        velocity_angle = math.atan2(self.velocity_x, self.velocity_y)
        ship_angle_rad = math.radians(self.angle)
        angle_diff = abs(velocity_angle - ship_angle_rad)
        
        # Normalize angle difference to 0-π
        if angle_diff > math.pi:
            angle_diff = 2 * math.pi - angle_diff
            
        # If angle difference is > π/2, we're moving backward relative to ship
        is_moving_backward = angle_diff > math.pi / 2
        
        max_allowed_speed = MAX_REVERSE_SPEED if is_moving_backward else MAX_SPEED
        
        if current_speed > max_allowed_speed:
            # Scale velocity down to max speed while preserving direction
            scale = max_allowed_speed / current_speed
            self.velocity_x *= scale
            self.velocity_y *= scale
        
        # Update position with world boundaries
        self.x += self.velocity_x * delta_time
        self.y += self.velocity_y * delta_time
        
        # Keep player within world bounds
        self.x = max(0, min(self.x, WORLD_WIDTH))
        self.y = max(0, min(self.y, WORLD_HEIGHT))
        
    def draw(self):
        # Draw thruster flame first (so it appears behind ship)
        self.draw_thruster()
        
        # Calculate rotated triangle points
        angle_rad = math.radians(self.angle)
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)
        
        # Original triangle points (pointing up)
        original_points = [
            (0, self.size),           # Top point
            (-self.size * 0.8, -self.size * 0.6),  # Bottom left
            (self.size * 0.8, -self.size * 0.6)    # Bottom right
        ]
        
        # Rotate and translate points
        rotated_points = []
        for px, py in original_points:
            # Rotate point around origin (corrected rotation matrix)
            rotated_x = px * cos_a + py * sin_a
            rotated_y = -px * sin_a + py * cos_a
            # Translate to ship position
            rotated_points.append((self.x + rotated_x, self.y + rotated_y))
        
        # Draw filled triangle
        arcade.draw_polygon_filled(rotated_points, SHIP_FILL_COLOR)
        
        # Draw triangle outline
        arcade.draw_polygon_outline(rotated_points, SHIP_BORDER_COLOR, BORDER_THICKNESS)
        
    def draw_thruster(self):
        """Draw blocky thruster when thrusting"""
        angle_rad = math.radians(self.angle)
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)
        
        # Draw forward thruster (blocky rectangle with gap)
        if self.thrusting_forward:
            gap = 1.5  # Gap between thruster and ship
            thruster_length = THRUSTER_LENGTH
            thruster_width = THRUSTER_WIDTH
            
            # Trapezoidal thruster behind ship with gap (wider at top, narrower at bottom)
            top_width = thruster_width
            bottom_width = thruster_width * 0.8  # 80% width at the bottom
            
            thruster_points = [
                (-top_width * 0.5, -self.size * 0.6 - gap),  # Top left (wide)
                (top_width * 0.5, -self.size * 0.6 - gap),   # Top right (wide)
                (bottom_width * 0.5, -self.size * 0.6 - gap - thruster_length),  # Bottom right (narrow)
                (-bottom_width * 0.5, -self.size * 0.6 - gap - thruster_length)  # Bottom left (narrow)
            ]
            
            # Rotate and translate thruster points
            rotated_thruster = []
            for px, py in thruster_points:
                rotated_x = px * cos_a + py * sin_a
                rotated_y = -px * sin_a + py * cos_a
                rotated_thruster.append((self.x + rotated_x, self.y + rotated_y))
            
            # Draw blocky thruster
            arcade.draw_polygon_filled(rotated_thruster, THRUSTER_COLOR)
        
        # Draw reverse thruster (behind ship, same position as forward thruster)
        if self.thrusting_backward and SHOW_REVERSE_THRUSTER:
            gap = 1.5  # Same gap as forward thruster
            thruster_length = REVERSE_THRUSTER_LENGTH
            thruster_width = THRUSTER_WIDTH * 0.8  # Slightly smaller than forward
            
            # Trapezoidal reverse thruster behind ship (same position as forward)
            top_width = thruster_width
            bottom_width = thruster_width * 0.8
            
            thruster_points = [
                (-top_width * 0.5, -self.size * 0.6 - gap),  # Top left (wide)
                (top_width * 0.5, -self.size * 0.6 - gap),   # Top right (wide)
                (bottom_width * 0.5, -self.size * 0.6 - gap - thruster_length),  # Bottom right (narrow)
                (-bottom_width * 0.5, -self.size * 0.6 - gap - thruster_length)  # Bottom left (narrow)
            ]
            
            # Rotate and translate thruster points
            rotated_thruster = []
            for px, py in thruster_points:
                rotated_x = px * cos_a + py * sin_a
                rotated_y = -px * sin_a + py * cos_a
                rotated_thruster.append((self.x + rotated_x, self.y + rotated_y))
            
            # Draw reverse thruster (different color to distinguish from forward)
            reverse_color = (100, 150, 255, 180)  # Blue-ish color for reverse
            arcade.draw_polygon_filled(rotated_thruster, reverse_color)

class Star:
    def __init__(self, x, y, size, opacity):
        self.x = x
        self.y = y
        self.size = size
        self.opacity = opacity
    
    def draw(self):
        # Create color with opacity (RGBA)
        color = (255, 255, 255, int(255 * self.opacity))
        arcade.draw_circle_filled(self.x, self.y, self.size, color)

class Planet:
    def __init__(self, x, y, size, color_data):
        self.x = x
        self.y = y
        self.size = size
        self.name, self.color, self.outline_color = color_data
        
    def draw(self):
        # Draw planet body
        arcade.draw_circle_filled(self.x, self.y, self.size, self.color)
        
        # Draw planet outline for depth
        arcade.draw_circle_outline(self.x, self.y, self.size, self.outline_color, 2)
        
        # Add some simple surface detail (crescent shadow)
        shadow_x = self.x + self.size * 0.3
        shadow_y = self.y
        arcade.draw_circle_filled(shadow_x, shadow_y, self.size * 0.9, (0, 0, 0, 100))

class StarField:
    def __init__(self, width, height, star_count=400):
        self.stars = []
        self.generate_stars(width, height, star_count)
    
    def generate_stars(self, width, height, star_count):
        for _ in range(star_count):
            x = random.randint(0, width)
            y = random.randint(0, height)
            
            # Simplified comic-style stars - just 2 types
            if random.random() < 0.8:  # Small stars (80%)
                size = 1.0
                opacity = 0.6
            else:  # Bright stars (20%)
                size = 1.5
                opacity = 1.0
            
            self.stars.append(Star(x, y, size, opacity))
    
    def draw(self):
        for star in self.stars:
            star.draw()

class FlightPrototype(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, "Little Space - Flight Prototype")
        arcade.set_background_color(arcade.color.BLACK)
        
        self.player = None
        self.starfield = None
        self.planets = []
        self.camera = None
        self.keys_pressed = set()
        
        print("=== FLIGHT PROTOTYPE STARTING ===")
        print(f"Game resolution: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        print(f"World size: {WORLD_WIDTH}x{WORLD_HEIGHT}")
        print(f"Window size: {WINDOW_WIDTH}x{WINDOW_HEIGHT} ({WINDOW_SCALE}x scale)")
        print("Controls: Arrow keys to fly, camera follows player")
        
    def setup(self):
        # Start player in center of world
        self.player = Player(WORLD_WIDTH // 2, WORLD_HEIGHT // 2)
        self.starfield = StarField(WORLD_WIDTH, WORLD_HEIGHT)
        self.camera = Camera()
        
        # Generate planets around the center of the world
        self.generate_planets()
    
    def on_draw(self):
        # Clear screen and start render
        arcade.start_render()
        
        # Apply camera view
        self.camera.use()
        
        # Draw starfield background first
        self.starfield.draw()
        
        # Draw planets
        for planet in self.planets:
            planet.draw()
        
        # Draw player ship on top
        self.player.draw()
        
        # Draw HUD elements (reset viewport for screen coordinates)
        arcade.set_viewport(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)
        self.draw_hud()
        
    def on_update(self, delta_time):
        # Update player
        self.player.update(delta_time, self.keys_pressed)
        
        # Update camera to follow player
        self.camera.follow_player(self.player.x, self.player.y)
        self.camera.update(delta_time)
        
    def generate_planets(self):
        """Generate planets around the center of the world"""
        center_x = WORLD_WIDTH // 2
        center_y = WORLD_HEIGHT // 2
        
        for i in range(PLANET_COUNT):
            # Position planets in a rough circle around center
            angle = (i / PLANET_COUNT) * 2 * math.pi
            distance = random.randint(200, 400)  # Distance from center
            
            x = center_x + distance * math.cos(angle)
            y = center_y + distance * math.sin(angle)
            
            # Random size
            size = random.randint(MIN_PLANET_SIZE, MAX_PLANET_SIZE)
            
            # Pick a color from our palette
            color_data = random.choice(PLANET_COLORS)
            
            planet = Planet(x, y, size, color_data)
            self.planets.append(planet)
            
    def draw_hud(self):
        """Draw HUD elements like coordinates"""
        # Draw coordinates in bottom right
        coord_text = f"X: {int(self.player.x)} Y: {int(self.player.y)}"
        arcade.draw_text(coord_text, 
                        WINDOW_WIDTH - 10,  # 10 pixels from right edge
                        10,                 # 10 pixels from bottom
                        arcade.color.WHITE,
                        12,                 # Font size
                        anchor_x="right")   # Right-aligned
        
    def on_key_press(self, key, _modifiers):
        self.keys_pressed.add(key)
        
    def on_key_release(self, key, _modifiers):
        self.keys_pressed.discard(key)

def main():
    game = FlightPrototype()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()