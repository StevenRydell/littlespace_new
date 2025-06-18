"""
Little Space - Flight Prototype Variables

All physics and gameplay variables for the spaceship flight mechanics.
Modify these values to tweak the feel of the spaceship controls.
"""

# === SPACESHIP PHYSICS ===

# Movement
ACCELERATION = 240          # How quickly ship speeds up when thrusting (increased for high speeds)
FRICTION = 0.995           # How quickly ship slows down (0.0 = instant stop, 1.0 = no friction)
MAX_SPEED = 50         # Maximum velocity the ship can reach
MAX_REVERSE_SPEED = 50    # Maximum reverse velocity the ship can reach

# Rotation  
ROTATION_SPEED = 180       # Degrees per second when turning left/right

# === SPACESHIP APPEARANCE ===

# Size
SHIP_SIZE = 5              # Base size of triangle spaceship
BORDER_THICKNESS = 1       # Thickness of white outline

# Colors (RGBA format: Red, Green, Blue, Alpha)
SHIP_FILL_COLOR = (255, 255, 255, 128)    # Semi-transparent white fill
SHIP_BORDER_COLOR = (255, 255, 255, 255)  # Solid white border

# === THRUSTER/ENGINE FLAME ===

# Thruster appearance
THRUSTER_LENGTH = 5            # How long the engine flame extends behind ship (decreased height)
THRUSTER_WIDTH = 4             # Width of flame at the base (near ship) (increased width)
THRUSTER_COLOR = (255, 100, 50, 180)  # Orange-red flame color

# Thruster behavior  
SHOW_REVERSE_THRUSTER = True   # Show smaller flame when thrusting backward
REVERSE_THRUSTER_LENGTH = 4    # Length of reverse thruster flame

# === PLANETS ===

# Planet appearance
PLANET_COUNT = 5                   # Number of planets to generate
MIN_PLANET_SIZE = 15              # Minimum planet radius
MAX_PLANET_SIZE = 40              # Maximum planet radius

# Planet colors (name, RGB color, outline color)
PLANET_COLORS = [
    ("Mars", (205, 92, 92), (139, 69, 69)),        # Reddish
    ("Earth", (70, 130, 180), (25, 25, 112)),      # Blue
    ("Venus", (255, 228, 181), (205, 133, 63)),    # Sandy/yellow
    ("Neptune", (72, 201, 176), (47, 79, 79)),     # Teal/cyan
    ("Jupiter", (222, 184, 135), (139, 90, 43)),   # Tan/brown
]

# === WORLD PHYSICS ===

# No additional world physics variables yet
# Future: gravity, air resistance, etc.

# === NOTES FOR TWEAKING ===

# Make ship more responsive:
#   - Increase ACCELERATION
#   - Increase MAX_SPEED and MAX_REVERSE_SPEED
#   - Decrease FRICTION (closer to 0.9)
#   - Increase ROTATION_SPEED

# Make ship more floaty/realistic:  
#   - Decrease ACCELERATION
#   - Decrease MAX_SPEED and MAX_REVERSE_SPEED
#   - Increase FRICTION (closer to 0.99)
#   - Decrease ROTATION_SPEED

# Make ship bigger/smaller:
#   - Adjust SHIP_SIZE
#   - Adjust BORDER_THICKNESS if neede