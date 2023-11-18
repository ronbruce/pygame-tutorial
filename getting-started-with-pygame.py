import pygame
pygame.init()

# Setting the dimension of the screen.
screen = pygame.display.set_mode([800, 800])
# Loop will run until game is False
running = True 

# Game loop
while running:
    # Check for game events: If click and close windows, then the game will end (loop closes).
    for event in pygame.event.get(): # Checking to see if the game has QUIT.
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen as white.
    screen.fill((255, 255, 255)) # Numbers are assigned to a Tuple.

    # Dark gray color for RGB tuple.
    dark_gray = (50, 50, 50)

    # Calculate circle spacing
    spacing = 300

    # color = [(255, 255, 0), (250, 141, 7), (25, 184, 22), (0, 255, 255), (255, 0, 0)] # List
    # position = [(250, 250), (400, 100), (100, 400), (400, 400), (100, 100)]  # List: First number is x and second number is y.
    # for color, position in zip(color, position):
    #     pygame.draw.circle(screen, color, position, 75)

    # Draw circles color for circles.
    # Nested loops are used to iterate over rows and columns.
    # x is determined by multiplying the col (column) by the spacing and adding an offset (100) for centering.
    # y is determined by multiplying the row by the spacing and adding an offset (100) for centering.
    for row in range(3):
        for col in range(3):
            x = col * spacing + 100 # Calculate x position based on column.
            y = row * spacing + 100 # Calculate y position based on row.
    # pygame.draw.circle() is used to draw a circle at the calculated (x, y) position with a radius of 75 pixels and the dark gray color.
            pygame.draw.circle(screen, dark_gray, (x, y), 75)
    # Draws a circle filled with the color, at the position, with a radius of 75 pixels.
    # pygame.draw.circle(screen, color, position, 75)
    # Update the display
    pygame.display.flip()

pygame.quit()

# Resources:
# Color picker for generating various RGB values
#  https://www.google.com/search?client=safari&rls=en&q=rgb+color+picker&ie=UTF-8&oe=UTF-8