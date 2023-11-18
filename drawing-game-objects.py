# Import and initialize pygame
import pygame
pygame.init()
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

apple = GameObject(120, 300, 'apple.png')
strawberry = GameObject(240, 300, 'strawberry.png')
apple2 = GameObject(360, 300, 'apple.png')
strawberry2 = GameObject(120, 200, 'strawberry.png')
apple3 = GameObject(240, 200, 'apple.png')
strawberry3 = GameObject(360, 200, 'strawberry.png')
apple4 = GameObject(120, 100, 'apple.png')
strawberry4 = GameObject(240, 100, 'strawberry.png')
apple5 = apple5 = GameObject(360, 100, 'apple.png')

# Creat the game loop
running = True 
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
  # Draw a circle
  screen.fill((255, 255, 255))
  # Render image to screen
  apple.render(screen)
  strawberry.render(screen)
  apple2.render(screen)
  strawberry2.render(screen)
  apple3.render(screen)
  strawberry3.render(screen)
  apple4.render(screen)
  strawberry4.render(screen)
  apple5.render(screen)

  # Update the window
  pygame.display.flip()