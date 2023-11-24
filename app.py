# Import and initialize pygame
import pygame
pygame.init()
from random import randint
import random

#TODO Make Player move one space into lane of strawberries and apples.


# Get the clock
clock = pygame.time.Clock()

# Configure the screen
screen = pygame.display.set_mode([500, 500])

lanes = [93, 218, 343]

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
        self.pos_x = 1
        self.pos_y = 1
        # sets the players position to the center of the screen.
        self.reset()
        # Methods used to set the target positions of the corresponding keys.
    
    # Define a fixed movement distance
    movement_distance = 125
    
    def left(self):
        if self.pos_x > 0:
            self.pos_x -= 1
            self.update_dx_dy()
        

    def right(self):
        if self.pos_x < len(lanes) -1:
            self.pos_x += 1
            self.update_dx_dy()

    def up(self):
        if self.pos_y > 0:
            self.pos_y -= 1
            self.update_dx_dy()
        

    def down(self):
        if self.pos_y < len(lanes) -1:
            self.pos_y += 1
            self.update_dx_dy()

        
        
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
        self.x = lanes[self.pos_x]
        self.y = lanes[self.pos_y]
        self.dx = self.x
        self.dy = self.y

    # Player chamge lanes but stick to available lanes
    def update_dx_dy(self):
        self.dx = lanes[self.pos_x]
        self.dy = lanes[self.pos_y]

player = Player()

# Make a group
all_sprites = pygame.sprite.Group()

# Add sprites to group
all_sprites.add(player)
all_sprites.add(apples)
all_sprites.add(strawberries)

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

    # move and render each apples
    for entity in all_sprites:
        entity.move()
        entity.render(screen)

    
    # Update the window
    pygame.display.flip()

    # Tick the clock
    clock.tick(60)

pygame.quit()
