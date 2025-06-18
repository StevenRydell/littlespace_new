import arcade
import math
import random

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
ROTATION_SPEED = 180

# Ship appearance
SHIP_SIZE = 5
BORDER_THICKNESS = 1
SHIP_FILL_COLOR = (255, 255, 255, 128)
SHIP_BORDER_COLOR = (255, 255, 255, 255)

# Thruster settings
THRUSTER_LENGTH = 5
THRUSTER_WIDTH = 4
THRUSTER_COLOR = (255, 100, 50, 180)
SHOW_REVERSE_THRUSTER = True
REVERSE_THRUSTER_LENGTH = 4

class Star:
    def __init__(self, x, y, size, opacity):
        self.x = x
        self.y = y
        self.size = size
        self.opacity = opacity
    
    def draw(self, camera_x, camera_y):
        color = (255, 255, 255, int(255 * self.opacity))
        screen_x = (self.x - camera_x) * SCREEN_SCALE
        screen_y = (self.y - camera_y) * SCREEN_SCALE
        arcade.draw_circle_filled(screen_x, screen_y, self.size * SCREEN_SCALE, color)

class StarField:
    def __init__(self, width, height, star_count=200):  # Reduced from 400 to 200
        self.stars = []
        self.generate_stars(width, height, star_count)
    
    def generate_stars(self, width, height, star_count):
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
    
    def draw(self, camera_x, camera_y):
        # Only draw stars that are visible on screen
        left = camera_x
        right = camera_x + SCREEN_WIDTH
        bottom = camera_y
        top = camera_y + SCREEN_HEIGHT
        
        for star in self.stars:
            if (star.x >= left and star.x <= right and 
                star.y >= bottom and star.y <= top):
                star.draw(camera_x, camera_y)

class Planet:
    def __init__(self, x, y, size, color_scheme):
        self.x = x
        self.y = y
        self.size = size
        self.name, self.color, self.outline_color, self.detail_color = color_scheme
    
    def draw(self, camera_x, camera_y):
        screen_x = (self.x - camera_x) * SCREEN_SCALE
        screen_y = (self.y - camera_y) * SCREEN_SCALE
        screen_size = self.size * SCREEN_SCALE
        
        # Draw planet body
        arcade.draw_circle_filled(screen_x, screen_y, screen_size, self.color)
        
        # Draw planet outline for depth
        arcade.draw_circle_outline(screen_x, screen_y, screen_size, self.outline_color, 2)
        
        # Add surface detail (crescent shadow)
        shadow_x = screen_x + screen_size * 0.3
        shadow_y = screen_y
        arcade.draw_circle_filled(shadow_x, shadow_y, screen_size * 0.9, (0, 0, 0, 80))
        
        # Add some surface features (small circles for variety)
        if self.size > 20:  # Only on larger planets
            feature_x = screen_x - screen_size * 0.4
            feature_y = screen_y + screen_size * 0.2
            arcade.draw_circle_filled(feature_x, feature_y, screen_size * 0.15, self.detail_color)

class SpaceFog:
    def __init__(self, x, y, width, height, color, density):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.density = density
        self.particles = []
        
        # Generate fog particles
        for _ in range(int(density * 50)):
            px = x + random.uniform(-width/2, width/2)
            py = y + random.uniform(-height/2, height/2)
            size = random.uniform(3, 8)
            opacity = random.uniform(0.1, 0.3)
            self.particles.append((px, py, size, opacity))
    
    def draw(self, camera_x, camera_y):
        for px, py, size, opacity in self.particles:
            screen_x = (px - camera_x) * SCREEN_SCALE
            screen_y = (py - camera_y) * SCREEN_SCALE
            
            # Create color with opacity
            r, g, b = self.color
            fog_color = (r, g, b, int(255 * opacity))
            arcade.draw_circle_filled(screen_x, screen_y, size * SCREEN_SCALE, fog_color)

class EnergyAnomaly:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.rotation = 0
        self.pulse = 0
    
    def update(self, delta_time):
        self.rotation += 45 * delta_time  # Rotate 45 degrees per second
        self.pulse += 3 * delta_time      # Pulse cycle
    
    def draw(self, camera_x, camera_y):
        screen_x = (self.x - camera_x) * SCREEN_SCALE
        screen_y = (self.y - camera_y) * SCREEN_SCALE
        
        # Pulsing effect
        pulse_scale = 1.0 + 0.3 * math.sin(self.pulse)
        current_size = self.size * pulse_scale * SCREEN_SCALE
        
        # Draw spinning energy rings
        for ring in range(3):
            ring_size = current_size * (0.6 + ring * 0.2)
            ring_opacity = 100 - ring * 20
            
            r, g, b = self.color
            ring_color = (r, g, b, ring_opacity)
            
            # Draw multiple circles to create energy effect
            arcade.draw_circle_outline(screen_x, screen_y, ring_size, ring_color, 2)

class AsteroidCluster:
    def __init__(self, x, y, count, spread):
        self.x = x
        self.y = y
        self.asteroids = []
        
        for _ in range(count):
            ax = x + random.uniform(-spread, spread)
            ay = y + random.uniform(-spread, spread)
            size = random.uniform(2, 6)
            gray_value = random.randint(100, 180)
            color = (gray_value, gray_value, gray_value)
            self.asteroids.append((ax, ay, size, color))
    
    def draw(self, camera_x, camera_y):
        for ax, ay, size, color in self.asteroids:
            screen_x = (ax - camera_x) * SCREEN_SCALE
            screen_y = (ay - camera_y) * SCREEN_SCALE
            
            # Draw asteroid as irregular shape (approximated with polygon)
            points = []
            for i in range(6):
                angle = (i / 6) * 2 * math.pi
                # Add some randomness to make it irregular
                radius = size * SCREEN_SCALE * (0.8 + 0.4 * math.sin(i * 2.3))
                px = screen_x + radius * math.cos(angle)
                py = screen_y + radius * math.sin(angle)
                points.append((px, py))
            
            arcade.draw_polygon_filled(points, color)

class BaseStation:
    def __init__(self, x, y, size, station_type):
        self.x = x
        self.y = y
        self.size = size
        self.station_type = station_type
        self.blink_timer = 0
        self.rotation = 0
        self.pulse = 0
        self.main_blink = True
        self.secondary_blink = False
    
    def update(self, delta_time):
        self.blink_timer += delta_time
        self.rotation += 30 * delta_time
        self.pulse += 2 * delta_time
        
        # Main lights blink every 2 seconds
        if self.blink_timer >= 2.0:
            self.main_blink = not self.main_blink
            self.blink_timer = 0
        
        # Secondary lights blink every 1 second (offset)
        self.secondary_blink = (self.blink_timer % 1.0) < 0.5
    
    def draw(self, camera_x, camera_y):
        screen_x = (self.x - camera_x) * SCREEN_SCALE
        screen_y = (self.y - camera_y) * SCREEN_SCALE
        screen_size = self.size * SCREEN_SCALE
        
        if self.station_type == "command":
            self.draw_command_station(screen_x, screen_y, screen_size)
        elif self.station_type == "fuel":
            self.draw_fuel_station(screen_x, screen_y, screen_size)
        elif self.station_type == "bar":
            self.draw_space_bar(screen_x, screen_y, screen_size)
        elif self.station_type == "mining":
            self.draw_mining_station(screen_x, screen_y, screen_size)
        elif self.station_type == "research":
            self.draw_research_station(screen_x, screen_y, screen_size)
        elif self.station_type == "trade":
            self.draw_trade_station(screen_x, screen_y, screen_size)
        elif self.station_type == "military":
            self.draw_military_station(screen_x, screen_y, screen_size)
        elif self.station_type == "shipyard":
            self.draw_shipyard_station(screen_x, screen_y, screen_size)
        elif self.station_type == "medical":
            self.draw_medical_station(screen_x, screen_y, screen_size)
        elif self.station_type == "casino":
            self.draw_casino_station(screen_x, screen_y, screen_size)
    
    def draw_command_station(self, x, y, size):
        # Large hexagonal command center with rotating sections
        points = []
        for i in range(6):
            angle = (i / 6) * 2 * math.pi
            px = x + size * math.cos(angle)
            py = y + size * math.sin(angle)
            points.append((px, py))
        
        arcade.draw_polygon_filled(points, (120, 120, 140))
        arcade.draw_polygon_outline(points, (200, 200, 220), 3)
        
        # Central command module
        arcade.draw_circle_filled(x, y, size * 0.5, (100, 100, 120))
        arcade.draw_circle_outline(x, y, size * 0.5, (150, 150, 170), 2)
        
        # Rotating communication arrays
        for i in range(4):
            angle = math.radians(self.rotation + i * 90)
            array_x = x + size * 0.7 * math.cos(angle)
            array_y = y + size * 0.7 * math.sin(angle)
            arcade.draw_circle_filled(array_x, array_y, 4, (255, 255, 100))
        
        # Command lights
        if self.main_blink:
            arcade.draw_circle_filled(x, y, 5, (255, 200, 0))
    
    def draw_fuel_station(self, x, y, size):
        # Cylindrical fuel tanks with connecting tubes
        # Main tanks
        for i in range(3):
            angle = (i / 3) * 2 * math.pi
            tank_x = x + size * 0.6 * math.cos(angle)
            tank_y = y + size * 0.6 * math.sin(angle)
            
            # Tank body
            arcade.draw_circle_filled(tank_x, tank_y, size * 0.3, (150, 100, 50))
            arcade.draw_circle_outline(tank_x, tank_y, size * 0.3, (200, 150, 100), 2)
            
            # Fuel level indicator
            if self.secondary_blink:
                arcade.draw_circle_filled(tank_x, tank_y, size * 0.15, (255, 150, 0))
        
        # Central hub with fuel pumps
        arcade.draw_circle_filled(x, y, size * 0.25, (100, 100, 100))
        
        # Fuel lines (connecting tubes)
        for i in range(3):
            angle = (i / 3) * 2 * math.pi
            end_x = x + size * 0.6 * math.cos(angle)
            end_y = y + size * 0.6 * math.sin(angle)
            arcade.draw_line(x, y, end_x, end_y, (100, 150, 100), 3)
    
    def draw_space_bar(self, x, y, size):
        # Torus-shaped rotating bar with neon lights
        # Main ring structure
        arcade.draw_circle_outline(x, y, size, (150, 100, 200), 8)
        arcade.draw_circle_outline(x, y, size * 0.6, (150, 100, 200), 6)
        
        # Central hub (dance floor/bar area)
        arcade.draw_circle_filled(x, y, size * 0.4, (80, 50, 120))
        
        # Rotating neon lights
        for i in range(8):
            angle = math.radians(self.rotation * 2 + i * 45)
            light_x = x + size * 0.8 * math.cos(angle)
            light_y = y + size * 0.8 * math.sin(angle)
            
            # Neon colors cycle
            hue = (self.pulse + i * 0.5) % 3
            if hue < 1:
                color = (255, int(255 * hue), 255)
            elif hue < 2:
                color = (255, 255, int(255 * (2 - hue)))
            else:
                color = (int(255 * (3 - hue)), 255, 255)
            
            arcade.draw_circle_filled(light_x, light_y, 3, color)
        
        # Party lights in center
        if self.secondary_blink:
            arcade.draw_circle_filled(x, y, 8, (255, 0, 255))
    
    def draw_mining_station(self, x, y, size):
        # Industrial mining platform with drilling arms
        # Main platform (square base)
        square_size = size * 0.8
        # Draw square as polygon instead
        half_size = square_size
        square_points = [
            (x - half_size, y - half_size),
            (x + half_size, y - half_size),
            (x + half_size, y + half_size),
            (x - half_size, y + half_size)
        ]
        arcade.draw_polygon_filled(square_points, (100, 80, 60))
        arcade.draw_polygon_outline(square_points, (150, 120, 90), 2)
        
        # Drilling arms extending outward
        for i in range(4):
            angle = math.radians(45 + i * 90)
            arm_length = size * 0.7
            end_x = x + arm_length * math.cos(angle)
            end_y = y + arm_length * math.sin(angle)
            
            # Arm structure
            arcade.draw_line(x, y, end_x, end_y, (120, 100, 80), 4)
            
            # Drill head
            arcade.draw_circle_filled(end_x, end_y, 6, (200, 150, 100))
            
            # Sparks when active
            if self.main_blink and i % 2 == 0:
                arcade.draw_circle_filled(end_x, end_y, 3, (255, 255, 100))
        
        # Central processing unit
        arcade.draw_circle_filled(x, y, size * 0.3, (80, 60, 40))
    
    def draw_research_station(self, x, y, size):
        # Scientific research station with rotating lab modules
        # Central core
        arcade.draw_circle_filled(x, y, size * 0.4, (100, 120, 150))
        arcade.draw_circle_outline(x, y, size * 0.4, (150, 180, 220), 2)
        
        # Research modules orbiting the core
        for i in range(6):
            angle = math.radians(self.rotation + i * 60)
            module_x = x + size * 0.7 * math.cos(angle)
            module_y = y + size * 0.7 * math.sin(angle)
            
            # Research lab module
            arcade.draw_circle_filled(module_x, module_y, size * 0.15, (120, 150, 200))
            
            # Experiment lights
            if (self.pulse + i) % 4 < 2:
                arcade.draw_circle_filled(module_x, module_y, 3, (0, 255, 255))
        
        # Data transmission beams
        if self.secondary_blink:
            for i in range(3):
                angle = math.radians(i * 120)
                beam_end_x = x + size * 1.2 * math.cos(angle)
                beam_end_y = y + size * 1.2 * math.sin(angle)
                arcade.draw_line(x, y, beam_end_x, beam_end_y, (0, 255, 255, 100), 2)
    
    def draw_trade_station(self, x, y, size):
        # Commercial trading hub with docking bays
        # Main marketplace (octagon)
        points = []
        for i in range(8):
            angle = (i / 8) * 2 * math.pi
            px = x + size * math.cos(angle)
            py = y + size * math.sin(angle)
            points.append((px, py))
        
        arcade.draw_polygon_filled(points, (150, 120, 80))
        arcade.draw_polygon_outline(points, (200, 160, 120), 2)
        
        # Docking bays
        for i in range(4):
            angle = (i / 4) * 2 * math.pi + math.pi/4
            bay_x = x + size * 0.8 * math.cos(angle)
            bay_y = y + size * 0.8 * math.sin(angle)
            
            # Docking port
            dock_points = [
                (bay_x - 4, bay_y - 6),
                (bay_x + 4, bay_y - 6),
                (bay_x + 4, bay_y + 6),
                (bay_x - 4, bay_y + 6)
            ]
            arcade.draw_polygon_filled(dock_points, (100, 150, 100))
            
            # Docking lights
            if self.main_blink:
                arcade.draw_circle_filled(bay_x, bay_y, 3, (0, 255, 0))
        
        # Central market
        arcade.draw_circle_filled(x, y, size * 0.3, (120, 100, 60))
        
        # Trade route indicators
        if self.secondary_blink:
            arcade.draw_circle_outline(x, y, size * 1.1, (255, 255, 0), 2)
    
    def draw_military_station(self, x, y, size):
        # Fortified military outpost with defense turrets
        # Main fortress (diamond shape)
        points = [
            (x, y + size),
            (x + size * 0.7, y),
            (x, y - size),
            (x - size * 0.7, y)
        ]
        arcade.draw_polygon_filled(points, (100, 100, 100))
        arcade.draw_polygon_outline(points, (150, 150, 150), 3)
        
        # Defense turrets
        for i in range(4):
            angle = math.radians(i * 90 + self.rotation * 0.5)
            turret_x = x + size * 0.6 * math.cos(angle)
            turret_y = y + size * 0.6 * math.sin(angle)
            
            # Turret base
            arcade.draw_circle_filled(turret_x, turret_y, 8, (80, 80, 80))
            
            # Turret barrel
            barrel_end_x = turret_x + 12 * math.cos(angle + self.pulse)
            barrel_end_y = turret_y + 12 * math.sin(angle + self.pulse)
            arcade.draw_line(turret_x, turret_y, barrel_end_x, barrel_end_y, (120, 120, 120), 3)
        
        # Command center
        arcade.draw_circle_filled(x, y, size * 0.25, (60, 60, 60))
        
        # Alert lights
        if self.main_blink:
            arcade.draw_circle_filled(x, y, 4, (255, 0, 0))
    
    def draw_shipyard_station(self, x, y, size):
        # Shipbuilding facility with construction arms
        # Main shipyard frame
        frame_width = size
        frame_height = size * 0.6
        frame_points = [
            (x - frame_width, y - frame_height),
            (x + frame_width, y - frame_height),
            (x + frame_width, y + frame_height),
            (x - frame_width, y + frame_height)
        ]
        arcade.draw_polygon_outline(frame_points, (150, 150, 150), 4)
        
        # Construction framework
        for i in range(3):
            frame_y = y - size * 0.4 + i * size * 0.4
            arcade.draw_line(x - size, frame_y, x + size, frame_y, (120, 120, 120), 2)
        
        # Ship under construction (center)
        ship_progress = (math.sin(self.pulse) + 1) / 2  # 0 to 1
        ship_length = size * 0.6 * ship_progress
        
        if ship_length > 0:
            arcade.draw_line(x - ship_length/2, y, x + ship_length/2, y, (100, 150, 200), 6)
        
        # Construction arms
        for i in range(2):
            arm_x = x + (i * 2 - 1) * size * 0.8
            arcade.draw_line(arm_x, y + size * 0.6, arm_x, y - size * 0.6, (100, 100, 100), 3)
            
            # Welding sparks
            if self.secondary_blink and ship_progress > 0.3:
                spark_x = arm_x + random.uniform(-5, 5)
                spark_y = y + random.uniform(-5, 5)
                arcade.draw_circle_filled(spark_x, spark_y, 2, (255, 255, 100))
        
        # Control tower
        tower_width = size * 0.15
        tower_height = size * 0.1
        tower_points = [
            (x - tower_width, y + size * 0.8 - tower_height),
            (x + tower_width, y + size * 0.8 - tower_height),
            (x + tower_width, y + size * 0.8 + tower_height),
            (x - tower_width, y + size * 0.8 + tower_height)
        ]
        arcade.draw_polygon_filled(tower_points, (80, 100, 120))
    
    def draw_medical_station(self, x, y, size):
        # Medical facility with healing bays
        # Main medical cross structure
        cross_size = size * 0.8
        
        # Vertical bar
        v_width = cross_size * 0.2
        v_height = cross_size
        v_points = [
            (x - v_width, y - v_height),
            (x + v_width, y - v_height),
            (x + v_width, y + v_height),
            (x - v_width, y + v_height)
        ]
        arcade.draw_polygon_filled(v_points, (200, 200, 200))
        
        # Horizontal bar
        h_width = cross_size
        h_height = cross_size * 0.2
        h_points = [
            (x - h_width, y - h_height),
            (x + h_width, y - h_height),
            (x + h_width, y + h_height),
            (x - h_width, y + h_height)
        ]
        arcade.draw_polygon_filled(h_points, (200, 200, 200))
        
        # Medical bay modules at cross ends
        for i in range(4):
            angle = math.radians(i * 90)
            bay_x = x + size * 0.7 * math.cos(angle)
            bay_y = y + size * 0.7 * math.sin(angle)
            
            # Medical bay
            arcade.draw_circle_filled(bay_x, bay_y, size * 0.2, (180, 220, 180))
            
            # Healing effect
            pulse_scale = 1.0 + 0.3 * math.sin(self.pulse + i)
            if self.secondary_blink:
                arcade.draw_circle_outline(bay_x, bay_y, size * 0.2 * pulse_scale, (0, 255, 100), 2)
        
        # Central medical core with red cross
        arcade.draw_circle_filled(x, y, size * 0.3, (240, 240, 240))
        arcade.draw_circle_filled(x, y, size * 0.15, (255, 50, 50))
        
        # Life sign monitors
        if self.main_blink:
            for i in range(4):
                angle = math.radians(i * 90 + 45)
                monitor_x = x + size * 0.25 * math.cos(angle)
                monitor_y = y + size * 0.25 * math.sin(angle)
                arcade.draw_circle_filled(monitor_x, monitor_y, 2, (0, 255, 0))
    
    def draw_casino_station(self, x, y, size):
        # Luxury casino with flashy lights
        # Main casino ring
        arcade.draw_circle_outline(x, y, size, (255, 215, 0), 6)
        arcade.draw_circle_filled(x, y, size * 0.8, (50, 0, 50))
        
        # VIP sections
        for i in range(6):
            angle = (i / 6) * 2 * math.pi
            vip_x = x + size * 0.6 * math.cos(angle)
            vip_y = y + size * 0.6 * math.sin(angle)
            
            # VIP room
            arcade.draw_circle_filled(vip_x, vip_y, size * 0.15, (100, 0, 100))
            
        # Central gaming floor
        arcade.draw_circle_filled(x, y, size * 0.4, (80, 0, 80))
        
        # Flashy casino lights (rainbow effect)
        for i in range(12):
            angle = math.radians(self.rotation * 3 + i * 30)
            light_x = x + size * 0.9 * math.cos(angle)
            light_y = y + size * 0.9 * math.sin(angle)
            
            # Rainbow cycling
            hue = (self.pulse * 2 + i * 0.3) % 6
            if hue < 1:
                color = (255, int(255 * hue), 0)
            elif hue < 2:
                color = (int(255 * (2 - hue)), 255, 0)
            elif hue < 3:
                color = (0, 255, int(255 * (hue - 2)))
            elif hue < 4:
                color = (0, int(255 * (4 - hue)), 255)
            elif hue < 5:
                color = (int(255 * (hue - 4)), 0, 255)
            else:
                color = (255, 0, int(255 * (6 - hue)))
            
            arcade.draw_circle_filled(light_x, light_y, 4, color)
        
        # Jackpot indicator
        if self.main_blink:
            arcade.draw_circle_filled(x, y, 8, (255, 255, 0))

class Pulsar:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.rotation = 0
        self.pulse = 0
    
    def update(self, delta_time):
        self.rotation += 90 * delta_time  # Fast rotation
        self.pulse += 4 * delta_time      # Fast pulse
    
    def draw(self, camera_x, camera_y):
        screen_x = (self.x - camera_x) * SCREEN_SCALE
        screen_y = (self.y - camera_y) * SCREEN_SCALE
        
        # Pulsing core
        pulse_scale = 1.0 + 0.5 * math.sin(self.pulse)
        core_size = self.size * pulse_scale * SCREEN_SCALE * 0.3
        
        # Draw bright core
        arcade.draw_circle_filled(screen_x, screen_y, core_size, self.color)
        
        # Draw rotating energy beams
        for beam in range(4):
            beam_angle = math.radians(self.rotation + beam * 90)
            beam_length = self.size * SCREEN_SCALE * 2
            
            # Beam start and end points
            start_x = screen_x + core_size * math.cos(beam_angle)
            start_y = screen_y + core_size * math.sin(beam_angle)
            end_x = screen_x + beam_length * math.cos(beam_angle)
            end_y = screen_y + beam_length * math.sin(beam_angle)
            
            # Draw beam with fading opacity
            r, g, b = self.color
            beam_color = (r, g, b, 120)
            arcade.draw_line(start_x, start_y, end_x, end_y, beam_color, 3)

class WarningBeacon:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.blink_timer = 0
        self.is_on = True
    
    def update(self, delta_time):
        self.blink_timer += delta_time
        if self.blink_timer >= 0.5:  # Blink every 0.5 seconds
            self.is_on = not self.is_on
            self.blink_timer = 0
    
    def draw(self, camera_x, camera_y):
        screen_x = (self.x - camera_x) * SCREEN_SCALE
        screen_y = (self.y - camera_y) * SCREEN_SCALE
        
        # Draw beacon base
        arcade.draw_circle_filled(screen_x, screen_y, 4 * SCREEN_SCALE, (100, 100, 100))
        
        if self.is_on:
            # Draw bright warning light
            arcade.draw_circle_filled(screen_x, screen_y, 6 * SCREEN_SCALE, (255, 150, 0))
            # Draw glow effect
            arcade.draw_circle_filled(screen_x, screen_y, 12 * SCREEN_SCALE, (255, 200, 0, 50))

class SpaceDebris:
    def __init__(self, x, y, count, spread):
        self.x = x
        self.y = y
        self.debris = []
        
        for _ in range(count):
            dx = x + random.uniform(-spread, spread)
            dy = y + random.uniform(-spread, spread)
            size = random.uniform(1, 4)
            rotation = random.uniform(0, 360)
            rotation_speed = random.uniform(-45, 45)
            
            # Different debris colors
            debris_colors = [
                (150, 150, 120),  # Metal
                (100, 80, 60),    # Rusty
                (80, 100, 120),   # Blue metal
                (120, 100, 80)    # Brown
            ]
            color = random.choice(debris_colors)
            
            self.debris.append([dx, dy, size, rotation, rotation_speed, color])
    
    def update(self, delta_time):
        for debris in self.debris:
            debris[3] += debris[4] * delta_time  # Update rotation
    
    def draw(self, camera_x, camera_y):
        for dx, dy, size, rotation, rotation_speed, color in self.debris:
            screen_x = (dx - camera_x) * SCREEN_SCALE
            screen_y = (dy - camera_y) * SCREEN_SCALE
            
            # Draw rotating debris as small rectangles
            angle_rad = math.radians(rotation)
            cos_a = math.cos(angle_rad)
            sin_a = math.sin(angle_rad)
            
            # Rectangle corners
            half_size = size * SCREEN_SCALE
            corners = [
                (-half_size, -half_size * 0.5),
                (half_size, -half_size * 0.5),
                (half_size, half_size * 0.5),
                (-half_size, half_size * 0.5)
            ]
            
            # Rotate and translate corners
            rotated_corners = []
            for cx, cy in corners:
                rx = cx * cos_a - cy * sin_a
                ry = cx * sin_a + cy * cos_a
                rotated_corners.append((screen_x + rx, screen_y + ry))
            
            arcade.draw_polygon_filled(rotated_corners, color)

class SolarFlare:
    def __init__(self, x, y, direction, length):
        self.x = x
        self.y = y
        self.direction = direction  # angle in degrees
        self.length = length
        self.intensity = 0
        self.pulse_timer = 0
    
    def update(self, delta_time):
        self.pulse_timer += delta_time * 2
        self.intensity = 0.5 + 0.5 * math.sin(self.pulse_timer)
    
    def draw(self, camera_x, camera_y):
        screen_x = (self.x - camera_x) * SCREEN_SCALE
        screen_y = (self.y - camera_y) * SCREEN_SCALE
        
        angle_rad = math.radians(self.direction)
        end_x = screen_x + self.length * SCREEN_SCALE * math.cos(angle_rad)
        end_y = screen_y + self.length * SCREEN_SCALE * math.sin(angle_rad)
        
        # Draw flare with varying intensity
        opacity = int(self.intensity * 200)
        flare_color = (255, 200, 100, opacity)
        
        # Draw multiple lines for thickness
        for i in range(3):
            offset = (i - 1) * 2
            perp_x = -math.sin(angle_rad) * offset
            perp_y = math.cos(angle_rad) * offset
            
            start_x = screen_x + perp_x
            start_y = screen_y + perp_y
            finish_x = end_x + perp_x
            finish_y = end_y + perp_y
            
            arcade.draw_line(start_x, start_y, finish_x, finish_y, flare_color, 2)

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
        
        # Collision optimization
        self.collision_check_timer = 0
        self.collision_check_interval = 0.016  # Check collisions ~60fps instead of every frame
    
    def update(self, delta_time, keys_pressed):
        # Handle rotation
        if arcade.key.LEFT in keys_pressed:
            self.angle -= ROTATION_SPEED * delta_time
        if arcade.key.RIGHT in keys_pressed:
            self.angle += ROTATION_SPEED * delta_time
        
        # Convert angle to radians
        angle_rad = math.radians(self.angle)
        
        # Handle thrust
        self.thrusting_forward = arcade.key.UP in keys_pressed
        self.thrusting_backward = arcade.key.DOWN in keys_pressed
        
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
        
        # Apply speed limits
        current_speed = math.sqrt(self.velocity_x**2 + self.velocity_y**2)
        if current_speed > MAX_SPEED:
            scale = MAX_SPEED / current_speed
            self.velocity_x *= scale
            self.velocity_y *= scale
        
        # Update position
        self.x += self.velocity_x * delta_time
        self.y += self.velocity_y * delta_time
        
        # Keep within world bounds
        self.x = max(0, min(self.x, WORLD_WIDTH))
        self.y = max(0, min(self.y, WORLD_HEIGHT))
    
    def check_collision_with_debris(self, debris_field, delta_time):
        """Optimized collision check with debris and apply pushback"""
        # Update collision timer
        self.collision_check_timer += delta_time
        
        # Only check collisions at intervals (not every frame)
        if self.collision_check_timer < self.collision_check_interval:
            return False
        
        self.collision_check_timer = 0  # Reset timer
        
        # Quick distance check to debris field center first
        field_center_x = debris_field.x
        field_center_y = debris_field.y
        field_dx = self.x - field_center_x
        field_dy = self.y - field_center_y
        field_distance = field_dx * field_dx + field_dy * field_dy  # Use squared distance (faster)
        
        # Skip if ship is too far from debris field (rough estimate)
        max_field_radius = 60  # Approximate debris field spread
        if field_distance > (max_field_radius + 20) * (max_field_radius + 20):
            return False
        
        # Check individual debris pieces
        for debris_item in debris_field.debris:
            debris_x, debris_y, debris_size = debris_item[0], debris_item[1], debris_item[2]
            
            # Fast squared distance check first
            dx = self.x - debris_x
            dy = self.y - debris_y
            distance_squared = dx * dx + dy * dy
            
            # Check if collision might occur (avoid sqrt until necessary)
            collision_distance = self.size + debris_size
            collision_distance_squared = collision_distance * collision_distance
            
            if distance_squared < collision_distance_squared:
                # Now calculate actual distance for precise collision
                distance = math.sqrt(distance_squared)
                
                if distance > 0:  # Avoid division by zero
                    # Calculate pushback direction (normalize)
                    pushback_x = dx / distance
                    pushback_y = dy / distance
                    
                    # Apply pushback force
                    pushback_strength = 150
                    self.velocity_x += pushback_x * pushback_strength * delta_time
                    self.velocity_y += pushback_y * pushback_strength * delta_time
                    
                    # Move ship out of collision
                    overlap = collision_distance - distance
                    self.x += pushback_x * overlap
                    self.y += pushback_y * overlap
                    
                    return True  # Collision occurred - exit early
        
        return False  # No collision
    
    def draw(self, camera_x, camera_y):
        # Draw thruster first (behind ship)
        self.draw_thruster(camera_x, camera_y)
        
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
            rotated_points.append((final_x, final_y))
        
        # Draw filled triangle
        arcade.draw_polygon_filled(rotated_points, SHIP_FILL_COLOR)
        
        # Draw triangle outline
        arcade.draw_polygon_outline(rotated_points, SHIP_BORDER_COLOR, BORDER_THICKNESS)
    
    def draw_thruster(self, camera_x, camera_y):
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


class SpaceFlightGame(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, "Little Space - Flight Game")
        arcade.set_background_color(arcade.color.BLACK)
        
        self.player = None
        self.starfield = None
        self.camera = None
        self.keys_pressed = set()
        
        # Space objects
        self.planets = []
        self.space_fog = []
        self.energy_anomalies = []
        self.asteroid_clusters = []
        self.space_stations = []
        self.pulsars = []
        self.warning_beacons = []
        self.space_debris = []
        self.solar_flares = []
        self.labels = []  # Text labels for components
        
        # FPS display
        self.fps_text = arcade.Text("FPS: --", 
                                   WINDOW_WIDTH - 100, 
                                   WINDOW_HEIGHT - 30, 
                                   arcade.color.GREEN, 
                                   16)
        
        # Coordinates display
        self.coords_text = arcade.Text("X: 0 Y: 0", 
                                      WINDOW_WIDTH - 100, 
                                      20, 
                                      arcade.color.WHITE, 
                                      12)
        
        self.frame_delta_time = 0.0
    
    def setup(self):
        # Start player in center of world
        self.player = Player(WORLD_WIDTH // 2, WORLD_HEIGHT // 2)
        self.starfield = StarField(WORLD_WIDTH, WORLD_HEIGHT)
        self.camera = Camera()
        
        # Generate space objects around starting area
        self.generate_space_objects()
    
    def generate_space_objects(self):
        # Create organized showcase layout
        center_x = WORLD_WIDTH // 2
        center_y = WORLD_HEIGHT // 2
        
        # Grid settings
        spacing_x = 150  # Horizontal spacing between objects
        spacing_y = 120  # Vertical spacing between rows
        
        # Row 1: Space Stations (Top row)
        station_types = [
            "command", "fuel", "bar", "mining", "research", 
            "trade", "military", "shipyard", "medical", "casino"
        ]
        
        start_x = center_x - (len(station_types) * spacing_x) // 2
        row_y = center_y + spacing_y * 2
        
        for i, station_type in enumerate(station_types):
            x = start_x + i * spacing_x
            y = row_y
            
            # Consistent sizing
            if station_type in ["command", "military", "shipyard"]:
                size = 25
            elif station_type in ["fuel", "trade", "casino"]:
                size = 22
            else:
                size = 20
            
            station = BaseStation(x, y, size, station_type)
            self.space_stations.append(station)
        
        # Row 2: Planets (Second row)
        planet_data = [
            ("Mars", (205, 92, 92), (139, 69, 69), (180, 60, 60)),
            ("Earth", (70, 130, 180), (25, 25, 112), (100, 200, 100)),
            ("Venus", (255, 228, 181), (205, 133, 63), (200, 180, 120)),
            ("Neptune", (72, 201, 176), (47, 79, 79), (120, 220, 200)),
            ("Jupiter", (222, 184, 135), (139, 90, 43), (180, 140, 100)),
            ("Purple", (147, 112, 219), (75, 0, 130), (180, 140, 200))
        ]
        
        start_x = center_x - (len(planet_data) * spacing_x) // 2
        row_y = center_y + spacing_y
        
        for i, planet_scheme in enumerate(planet_data):
            x = start_x + i * spacing_x
            y = row_y
            size = 30
            
            planet = Planet(x, y, size, planet_scheme)
            self.planets.append(planet)
        
        # Row 3: Energy Phenomena (Third row - center)
        row_y = center_y
        
        # Pulsars
        pulsar_colors = [(255, 255, 255), (255, 200, 255), (200, 255, 255)]
        for i, color in enumerate(pulsar_colors):
            x = center_x - spacing_x * 2 + i * spacing_x
            y = row_y
            pulsar = Pulsar(x, y, 15, color)
            self.pulsars.append(pulsar)
        
        # Energy Anomalies
        energy_colors = [(255, 100, 255), (100, 255, 255), (255, 255, 100)]
        for i, color in enumerate(energy_colors):
            x = center_x + spacing_x * 0.5 + i * spacing_x
            y = row_y
            anomaly = EnergyAnomaly(x, y, 25, color)
            self.energy_anomalies.append(anomaly)
        
        # Row 4: Environmental Effects (Fourth row)
        row_y = center_y - spacing_y
        
        # Space Fog
        fog_colors = [
            (150, 50, 200),  # Purple
            (50, 200, 150),  # Teal  
            (200, 150, 50),  # Gold
            (200, 50, 150),  # Pink
            (50, 100, 200)   # Deep blue
        ]
        
        for i, color in enumerate(fog_colors):
            x = center_x - spacing_x * 2.5 + i * spacing_x
            y = row_y
            fog = SpaceFog(x, y, 80, 60, color, 0.5)
            self.space_fog.append(fog)
        
        # Asteroid Cluster
        cluster = AsteroidCluster(center_x + spacing_x * 2.5, row_y, 10, 40)
        self.asteroid_clusters.append(cluster)
        
        # Row 5: Navigation & Debris (Bottom row)
        row_y = center_y - spacing_y * 2
        
        # Warning Beacons
        for i in range(5):
            x = center_x - spacing_x * 2 + i * spacing_x
            y = row_y
            beacon = WarningBeacon(x, y)
            self.warning_beacons.append(beacon)
        
        # Space Debris
        for i in range(3):
            x = center_x + spacing_x * 1.5 + i * spacing_x * 0.8
            y = row_y
            debris = SpaceDebris(x, y, 8, 30)
            self.space_debris.append(debris)
        
        # Solar Flares (attached to first 3 planets)
        for i, planet in enumerate(self.planets[:3]):
            for flare_num in range(2):
                direction = flare_num * 90 + i * 30  # Organized directions
                length = 60
                flare = SolarFlare(planet.x, planet.y, direction, length)
                self.solar_flares.append(flare)
        
        # Add subtle teal fog patches around the space environment
        # Using teal colors from the user's image with subtle opacity
        teal_colors = [
            (64, 224, 208),   # Bright teal
            (32, 178, 170),   # Medium teal  
            (16, 134, 128),   # Darker teal
            (48, 200, 190),   # Light cyan-teal
            (40, 160, 150)    # Deep teal
        ]
        
        # Large atmospheric fog patches (background layer)
        atmospheric_patches = [
            (center_x - 350, center_y + 180, 120, 80, 0.3),   # Top left
            (center_x + 320, center_y + 120, 100, 70, 0.25),  # Top right  
            (center_x - 250, center_y - 280, 140, 90, 0.35),  # Bottom left
            (center_x + 380, center_y - 180, 110, 75, 0.2),   # Bottom right
            (center_x - 80, center_y + 250, 90, 60, 0.25),    # Above center
            (center_x + 150, center_y - 120, 85, 65, 0.3),    # Between rows
        ]
        
        for i, (x, y, width, height, density) in enumerate(atmospheric_patches):
            color = teal_colors[i % len(teal_colors)]
            fog = SpaceFog(x, y, width, height, color, density)
            self.space_fog.append(fog)
        
        # Create labels for each section
        label_offset_y = 40  # Distance above objects
        
        # Row 1 Labels - Space Stations
        station_names = [
            "Command", "Fuel", "Space Bar", "Mining", "Research",
            "Trade", "Military", "Shipyard", "Medical", "Casino"
        ]
        start_x = center_x - (len(station_types) * spacing_x) // 2
        row_y = center_y + spacing_y * 2
        
        for i, name in enumerate(station_names):
            x = start_x + i * spacing_x
            y = row_y + label_offset_y
            label = arcade.Text(name, x * SCREEN_SCALE, y * SCREEN_SCALE, arcade.color.WHITE, 12, anchor_x="center")
            self.labels.append(label)
        
        # Section header for stations
        header_y = row_y + label_offset_y + 25
        header = arcade.Text("SPACE STATIONS", center_x * SCREEN_SCALE, header_y * SCREEN_SCALE, arcade.color.YELLOW, 16, anchor_x="center")
        self.labels.append(header)
        
        # Row 2 Labels - Planets
        planet_names = ["Mars", "Earth", "Venus", "Neptune", "Jupiter", "Purple"]
        start_x = center_x - (len(planet_data) * spacing_x) // 2
        row_y = center_y + spacing_y
        
        for i, name in enumerate(planet_names):
            x = start_x + i * spacing_x
            y = row_y + label_offset_y
            label = arcade.Text(name, x * SCREEN_SCALE, y * SCREEN_SCALE, arcade.color.WHITE, 12, anchor_x="center")
            self.labels.append(label)
        
        header_y = row_y + label_offset_y + 25
        header = arcade.Text("PLANETS", center_x * SCREEN_SCALE, header_y * SCREEN_SCALE, arcade.color.YELLOW, 16, anchor_x="center")
        self.labels.append(header)
        
        # Row 3 Labels - Energy Phenomena
        row_y = center_y
        
        # Pulsar labels
        pulsar_names = ["White Pulsar", "Pink Pulsar", "Cyan Pulsar"]
        for i, name in enumerate(pulsar_names):
            x = center_x - spacing_x * 2 + i * spacing_x
            y = row_y + label_offset_y
            label = arcade.Text(name, x * SCREEN_SCALE, y * SCREEN_SCALE, arcade.color.WHITE, 12, anchor_x="center")
            self.labels.append(label)
        
        # Anomaly labels
        anomaly_names = ["Magenta Field", "Cyan Field", "Yellow Field"]
        for i, name in enumerate(anomaly_names):
            x = center_x + spacing_x * 0.5 + i * spacing_x
            y = row_y + label_offset_y
            label = arcade.Text(name, x * SCREEN_SCALE, y * SCREEN_SCALE, arcade.color.WHITE, 12, anchor_x="center")
            self.labels.append(label)
        
        header_y = row_y + label_offset_y + 25
        header = arcade.Text("ENERGY PHENOMENA", center_x * SCREEN_SCALE, header_y * SCREEN_SCALE, arcade.color.YELLOW, 16, anchor_x="center")
        self.labels.append(header)
        
        # Row 4 Labels - Environmental Effects
        row_y = center_y - spacing_y
        
        # Fog labels
        fog_names = ["Purple Fog", "Teal Fog", "Gold Fog", "Pink Fog", "Blue Fog"]
        for i, name in enumerate(fog_names):
            x = center_x - spacing_x * 2.5 + i * spacing_x
            y = row_y + label_offset_y
            label = arcade.Text(name, x * SCREEN_SCALE, y * SCREEN_SCALE, arcade.color.WHITE, 12, anchor_x="center")
            self.labels.append(label)
        
        # Asteroid label
        asteroid_label = arcade.Text("Asteroids", (center_x + spacing_x * 2.5) * SCREEN_SCALE, (row_y + label_offset_y) * SCREEN_SCALE, arcade.color.WHITE, 12, anchor_x="center")
        self.labels.append(asteroid_label)
        
        header_y = row_y + label_offset_y + 25
        header = arcade.Text("ENVIRONMENTAL EFFECTS", center_x * SCREEN_SCALE, header_y * SCREEN_SCALE, arcade.color.YELLOW, 16, anchor_x="center")
        self.labels.append(header)
        
        # Row 5 Labels - Navigation & Debris
        row_y = center_y - spacing_y * 2
        
        # Beacon labels
        for i in range(5):
            x = center_x - spacing_x * 2 + i * spacing_x
            y = row_y + label_offset_y
            label = arcade.Text("Beacon", x * SCREEN_SCALE, y * SCREEN_SCALE, arcade.color.WHITE, 12, anchor_x="center")
            self.labels.append(label)
        
        # Debris labels
        debris_names = ["Debris A", "Debris B", "Debris C"]
        for i, name in enumerate(debris_names):
            x = center_x + spacing_x * 1.5 + i * spacing_x * 0.8
            y = row_y + label_offset_y
            label = arcade.Text(name, x * SCREEN_SCALE, y * SCREEN_SCALE, arcade.color.WHITE, 12, anchor_x="center")
            self.labels.append(label)
        
        header_y = row_y + label_offset_y + 25
        header = arcade.Text("NAVIGATION & DEBRIS", center_x * SCREEN_SCALE, header_y * SCREEN_SCALE, arcade.color.YELLOW, 16, anchor_x="center")
        self.labels.append(header)
        
    
    def is_visible(self, obj_x, obj_y, obj_size=50):
        """Check if object is visible on screen (frustum culling)"""
        # Calculate screen boundaries in world coordinates
        left = self.camera.x - obj_size
        right = self.camera.x + SCREEN_WIDTH + obj_size
        bottom = self.camera.y - obj_size
        top = self.camera.y + SCREEN_HEIGHT + obj_size
        
        # Check if object is within visible area
        return (obj_x >= left and obj_x <= right and 
                obj_y >= bottom and obj_y <= top)
    
    def on_draw(self):
        self.clear()
        
        # Always draw starfield (background)
        self.starfield.draw(self.camera.x, self.camera.y)
        
        # Draw space fog (with culling)
        for fog in self.space_fog:
            if self.is_visible(fog.x, fog.y, 100):  # Larger cull size for fog
                fog.draw(self.camera.x, self.camera.y)
        
        # Draw solar flares (with culling)
        for flare in self.solar_flares:
            if self.is_visible(flare.x, flare.y, flare.length):
                flare.draw(self.camera.x, self.camera.y)
        
        # Draw planets (with culling)
        for planet in self.planets:
            if self.is_visible(planet.x, planet.y, planet.size):
                planet.draw(self.camera.x, self.camera.y)
        
        # Draw space debris (with culling)
        for debris in self.space_debris:
            if self.is_visible(debris.x, debris.y, 60):
                debris.draw(self.camera.x, self.camera.y)
        
        # Draw asteroid clusters (with culling)
        for cluster in self.asteroid_clusters:
            if self.is_visible(cluster.x, cluster.y, 60):
                cluster.draw(self.camera.x, self.camera.y)
        
        # Draw space stations (with culling)
        for station in self.space_stations:
            if self.is_visible(station.x, station.y, station.size):
                station.draw(self.camera.x, self.camera.y)
        
        # Draw warning beacons (with culling)
        for beacon in self.warning_beacons:
            if self.is_visible(beacon.x, beacon.y, 20):
                beacon.draw(self.camera.x, self.camera.y)
        
        # Draw pulsars (with culling)
        for pulsar in self.pulsars:
            if self.is_visible(pulsar.x, pulsar.y, pulsar.size * 2):
                pulsar.draw(self.camera.x, self.camera.y)
        
        # Draw energy anomalies (with culling)
        for anomaly in self.energy_anomalies:
            if self.is_visible(anomaly.x, anomaly.y, anomaly.size):
                anomaly.draw(self.camera.x, self.camera.y)
        
        # Always draw player ship
        self.player.draw(self.camera.x, self.camera.y)
        
        # Draw labels only if visible (with culling)
        for label in self.labels:
            label_world_x = label.x / SCREEN_SCALE
            label_world_y = label.y / SCREEN_SCALE
            
            if self.is_visible(label_world_x, label_world_y, 50):
                screen_x = (label_world_x - self.camera.x) * SCREEN_SCALE
                screen_y = (label_world_y - self.camera.y) * SCREEN_SCALE
                
                temp_text = arcade.Text(label.text, screen_x, screen_y, label.color, label.font_size, anchor_x="center")
                temp_text.draw()
        
        # Draw HUD (no camera offset)
        self.fps_text.draw()
        self.coords_text.draw()
    
    def on_update(self, delta_time):
        self.frame_delta_time = delta_time
        
        # Update FPS and coordinates display
        fps_value = f"FPS: {1/delta_time:.1f}" if delta_time > 0 else "FPS: --"
        self.fps_text.text = fps_value
        
        coord_text = f"X: {int(self.player.x)} Y: {int(self.player.y)}"
        self.coords_text.text = coord_text
        
        # Update player
        self.player.update(delta_time, self.keys_pressed)
        
        # Check collisions with debris fields (optimized)
        for debris_field in self.space_debris:
            self.player.check_collision_with_debris(debris_field, delta_time)
        
        # Update camera to follow player
        self.camera.follow_player(self.player.x, self.player.y)
        self.camera.update(delta_time)
        
        # Update animated objects (only if visible to save CPU)
        for anomaly in self.energy_anomalies:
            if self.is_visible(anomaly.x, anomaly.y, anomaly.size):
                anomaly.update(delta_time)
        
        for station in self.space_stations:
            if self.is_visible(station.x, station.y, station.size):
                station.update(delta_time)
        
        for pulsar in self.pulsars:
            if self.is_visible(pulsar.x, pulsar.y, pulsar.size * 2):
                pulsar.update(delta_time)
        
        for beacon in self.warning_beacons:
            if self.is_visible(beacon.x, beacon.y, 20):
                beacon.update(delta_time)
        
        for debris in self.space_debris:
            if self.is_visible(debris.x, debris.y, 60):
                debris.update(delta_time)
        
        for flare in self.solar_flares:
            if self.is_visible(flare.x, flare.y, flare.length):
                flare.update(delta_time)
    
    def on_key_press(self, key, modifiers):
        self.keys_pressed.add(key)
    
    def on_key_release(self, key, modifiers):
        self.keys_pressed.discard(key)

def main():
    game = SpaceFlightGame()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()