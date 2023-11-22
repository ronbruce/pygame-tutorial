# Import and initialize pygame
import pygame
pygame.init()
from random import randint
import random

# Get the clock
clock = pygame.time.Clock()

# Configure the screen
screen = pygame.display.set_mode([500, 500])

# This class extends pygame.sprite.Sprite
class GameObject(pygame.sprite.Sprite):
    # Defines four parameters: x, y, width, and height.
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y
    # This method render() is responsible for drawing GameObject's on the surface screen.
    # Screen is the parameter. 
    def render(self, screen):
        screen.blit(self.surf, (self.x, self.y))

class Apple(GameObject):
    def __init__(self):
        super(Apple, self).__init__(0, 0, 'apple.png')
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1  # Fix typo here
        self.reset()

    def move(self):
        self.y += self.dy
        # Check y position of the apple
        if self.y > 500:
            self.reset()

    def reset(self):
        # I created 'lane_positions' with the three x-values: [93, 218, 343]
        lane_positions = [93, 218, 343]
        # When resetting the position of the apple('reset' method), I use
        # 'choice(lane_positions)' to randomly select one of the three values above.
        # This allows my apples to fall randomly in one of the three lanes.
        self.x = random.choice(lane_positions)
        self.y = 64 # Move apple of the top of the screen

class Strawberry(GameObject):
    def __init__(self):
        super(Strawberry, self).__init__(0, 0, 'strawberry.png')
        self.dx = 1 # Set a fixed speed 
        self.y = randint(0, 500) # Start at a random y position
    
    def move(self):
        self.x += self.dx
        if self.x > 500:
            self.x = 0
            self.y = randint(0, 500) # Move to a new random y position when reaching the right edge.

# Create an instance of the Apple class before the game loop
apples = [Apple() for _ in range(3)]

# Instances of the Strawberry class
strawberries = [Strawberry() for _ in range(3)]

# Player represents the character in the game. 
# It inherits from the 'GameObject' class.
class Player(GameObject):
    def __init__(self):
        # 'Player' class ha all the attributes and methods of 'GameObject' class.
        super(Player, self).__init__(0, 0, 'player.png')
        # dx and dy represents the target position the player is moving in.
        self.dx = 0
        self.dy = 0
        # sets the players position to the center of the screen.
        self.reset()
        # Methods used to set the target positions of the corresponding keys.
    
    # Define a fixed movement distance
    movement_distance = 125
    
    def left(self):
        self.dx = max(self.dx - 10, 0)  # Decrease dx, but ensure it's not less than 0

    def right(self):
        self.dx = min(self.dx + 10, 500 - self.surf.get_width())  # Increase dx, but ensure it's not greater than (500 - player_width)

    def up(self):
        self.dy = max(self.dy - 10, 0)  # Decrease dy, but ensure it's not less than 0

    def down(self):
        self.dy = min(self.dy + 10, 500 - self.surf.get_height())  # Increase dy, but ensure it's not greater than (500 - player_height)

        
        
        # move is responsible for updating the player's position.
        # Instead of directly setting the position, it uses an easing function to gradually approach the target position.
        # '(x - dx) * 0.25' is used to calculate the distance to move('distanceToMove')
        # the object from its current position ('x') toward a target position ('dx).
        # The '0.25' represents factor (25%) of the distance to be covered in each frame.
        # The result of 'distanceToMove' is substracted from the current position('x'),
        # moving the object closer to a target.
    def move(self):
        # Update player position using the easing function
        self.x -= (self.x - self.dx) * 0.25
        self.y -= (self.y - self.dy) * 0.25

        # Ensure the player stays within the screen boundaries
        self.x = max(0, min(self.x, 500 - self.surf.get_width()))
        self.y = max(0, min(self.y, 500 - self.surf.get_height()))


    # 'reset' method sets the player's position to the center of the screen, ensuring it stays within screen boundaries.
    def reset(self):
        # Getting the image loaded in GameObject with 'self.surf'
        # Using the get_width() and get_height() to get width and height.
        self.x = (500 - self.surf.get_width()) // 2
        self.y = (500 - self.surf.get_height()) // 2

player = Player()

# Create the game loop
running = True 
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Check for event type KEYBOARD
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()
            elif event.key == pygame.K_UP:
                player.up()
            elif event.key == pygame.K_DOWN:
                player.down()
      
    # Draw background
    screen.fill((255, 255, 255))

    # Instead of dealing with a single apple and strawberry in the game loop,
    # I use a loop to iterate over all my apples and strawberries.
    # For each iteration, I move the object and render it on to my screen. 

    # move and render each apples
    for apple in apples:
        apple.move()
        apple.render(screen)

    # Move and render each strawberry
    for strawberry in strawberries:
        strawberry.move()
        strawberry.render(screen)

    player.move()
    player.render(screen)

    
    
    # Update the window
    pygame.display.flip()

    # Tick the clock
    clock.tick(60)

pygame.quit()
