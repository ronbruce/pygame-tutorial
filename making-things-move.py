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

# Create the game loop
running = True 
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
      
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

    
    
    # Update the window
    pygame.display.flip()

    # Tick the clock
    clock.tick(60)

pygame.quit()


