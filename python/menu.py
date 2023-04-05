import pygame

# Initialize Pygame
pygame.init()

# Set the screen dimensions
windoww = 640
windowh = 480
screen = pygame.display.set_mode((windoww, windowh))
pygame.display.set_caption("Menu")

# Set the font and font size
font = pygame.font.Font(None, 36)

# Set the game options
game_options = [
    {'name': 'Collections Market Place', 'game': 'python/market.py'},
    {'name': 'Super Space Strikers', 'game': 'python/Super Space Strickers.py'},
    {'name': 'Dice Fighters', 'game': 'python/dice fighter.py'}
]

# Set the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set the starting option
selected_option = 0

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_option = (selected_option - 1) % len(game_options)
            elif event.key == pygame.K_DOWN:
                selected_option = (selected_option + 1) % len(game_options)
            elif event.key == pygame.K_RETURN:
                start = game_options[selected_option]['game']
                exec(open(start).read())

    # Draw the background
    screen.fill(WHITE)

        # Draw the options
    for i, option in enumerate(game_options):
        text = font.render(option['name'], True, BLACK if i != selected_option else RED)
        rect = text.get_rect(center=(windoww/2, windowh/2 + i * 40))
        screen.blit(text, rect)

    # Update the screen
    pygame.display.update()
# Quit Pygame
pygame.quit()