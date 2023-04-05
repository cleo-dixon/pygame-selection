import pygame
import random
import pandas as pd

#Author: Cleo Dixon

# Initialize Pygame
pygame.init()

# Initialize music
pygame.mixer.init()

pygame.mixer.music.load('assests/audio/background.wav')
pygame.mixer.music.set_volume(0.5)


coin_sound = pygame.mixer.Sound('assests/audio/coin.wav')
dice_sound = pygame.mixer.Sound('assests/audio/dice.wav')
move_sound = pygame.mixer.Sound('assests/audio/movement.wav')
taken_sound = pygame.mixer.Sound('assests/audio/taken.wav')
win_sound = pygame.mixer.Sound('assests/audio/winner.wav')
# Define the size of the board and cells
#left
board1w = 70
board1h = 630
#top
board2w = 840
board2h = 70
#right
board3w = 70
board3h = 630
#bottom
board4w = 840
board4h = 70

windoww = 1350
windowh = 750

scoreboardw = 150
scoreboardh = 450

leaderw = 200
leaderh = 150
cell_size = 70



class names ( ):
    def __init__(self):
          self.name=''

player_1= names ()
player_1.name= input("Enter player 1's name: ") 
player_2= names ()
player_2.name= input("Enter player 2's name: ") 
player_3= names ()
player_3.name= input("Enter player 3's name: ") 

player_name = [player_1.name, player_2.name, player_3.name]
# Define function to display text
screen = pygame.display.set_mode((windoww, windowh))
pygame.display.set_caption("Collections Market Place")
ticon = pygame.image.load('assests/images/Apples-clipart.png')

pygame.display.set_icon(ticon)

# Plays music in an infinite loop
pygame.mixer.music.play (-1) 

simage = pygame.image.load('assests/images/market2.2.jpg')

# Create a new surface with the desired size and the same pixel format as the screen
reimage = pygame.surface.Surface((windoww, windowh), flags=pygame.SRCALPHA, depth=32)
reimage.fill((255,255,255,0))

# Convert the pixel format of the source image to match the pixel format of the destination surface
simage = simage.convert_alpha(reimage)

# Scale the image to the new size and blit it onto the new surface
pygame.transform.scale(simage, (windoww, windowh), reimage)

# Blit the resized image onto the screen surface
screen.blit(reimage, (0, 0))

y = (1 * cell_size) + (cell_size / 2)
x =(5 * cell_size) + (cell_size / 2)

logo = pygame.image.load('assests/images/logo4.png')
logo = pygame.transform.scale(logo, (300,300))
screen.blit(logo, (x, y))

pygame.display.flip()

# Define the colors for the board
background_color = (0, 255, 255)
grid_color = (0, 0, 0)


# Create the board surfaces
cells = []

# Create the board surfaces
board1 = pygame.surface.Surface((board1w, board1h))
board1.fill((46,139,87))
board2 = pygame.surface.Surface((board2w, board2h))
board2.fill((46,139,87))
board3 = pygame.surface.Surface((board3w, board3h))
board3.fill((46,139,87))
board4 = pygame.surface.Surface((board4w, board4h))
board4.fill((46,139,87))

# Draw a grid on each board

for x in range(0, board1w, cell_size):
    for y in range(0, board1h, cell_size):
        rect = pygame.Rect(x, y, cell_size, cell_size)
        pygame.draw.rect(board1, (255, 255, 255), rect, 1)

for x in range(0, board2w, cell_size):
    for y in range(0, board2h, cell_size):
        rect = pygame.Rect(x, y, cell_size, cell_size)
        pygame.draw.rect(board2, (255, 255, 255), rect, 1)

for x in range(0, board3w, cell_size):
    for y in range(0, board3h, cell_size):
        rect = pygame.Rect(x, y, cell_size, cell_size)
        pygame.draw.rect(board3, (255, 255, 255), rect, 1)

for x in range(0, board4w, cell_size):
    for y in range(0, board4h, cell_size):
        rect = pygame.Rect(x, y, cell_size, cell_size)
        pygame.draw.rect(board4, (255, 255, 255), rect, 1)

# Arrange the boards into a rectangle
board_rect = pygame.Rect(50, 50, board1w + board2w + board3w, board1h + board2h + board3h + board4h)
board1_pos = pygame.math.Vector2(0, 0)
board2_pos = pygame.math.Vector2(board1w + 0, 0)
board3_pos = pygame.math.Vector2(board1w + board2w + 0, 0)
board4_pos = ((windoww - board1w) // 10.61, (windowh - board4h) // 1.113)

screen.blit(board1, board_rect.topleft + board1_pos)
screen.blit(board2, board_rect.topleft + board2_pos)
screen.blit(board3, board_rect.topleft + board3_pos)
screen.blit(board4, board4_pos)


font = pygame.font.Font('assests/fonts/aAbstractGroovy.ttf', 30)
text_surface = font.render("GO", True, (255,255,255))
text_rect = text_surface.get_rect(center=(13.7*cell_size + cell_size//2, 8.75*cell_size + cell_size//2))
screen.blit(text_surface, text_rect)

# Icons To Board
iconpositions = {
    1: (12.45*cell_size + cell_size//2, 8.45*cell_size + cell_size//2),
    2: (11.45*cell_size + cell_size//2, 8.45*cell_size + cell_size//2),
    3: (10.45*cell_size + cell_size//2, 8.45*cell_size + cell_size//2),
    4: (9.45*cell_size + cell_size//2, 8.455*cell_size + cell_size//2),
    5: (8.455*cell_size + cell_size//2, 8.455*cell_size + cell_size//2),
    6: (7.45*cell_size + cell_size//2, 8.455*cell_size + cell_size//2),
    7: (6.45*cell_size + cell_size//2, 8.455*cell_size + cell_size//2),
    8: (5.45*cell_size + cell_size//2, 8.455*cell_size + cell_size//2),
    9: (4.45*cell_size + cell_size//2, 8.455*cell_size + cell_size//2),
    10: (3.45*cell_size + cell_size//2, 8.455*cell_size + cell_size//2),
    11: (2.45*cell_size + cell_size//2, 8.455*cell_size + cell_size//2),
    12: (1.45*cell_size + cell_size//2, 8.455*cell_size + cell_size//2),
    13: (0.45*cell_size + cell_size//2, 8.455*cell_size + cell_size//2),
    14: (0.45*cell_size + cell_size//2, 7.455*cell_size + cell_size//2),
    15: (0.45*cell_size + cell_size//2, 6.455*cell_size + cell_size//2),
    16: (0.45*cell_size + cell_size//2, 5.455*cell_size + cell_size//2),
    17: (0.45*cell_size + cell_size//2, 4.455*cell_size + cell_size//2),
    18: (0.45*cell_size + cell_size//2, 3.455*cell_size + cell_size//2),
    19: (0.45*cell_size + cell_size//2, 2.455*cell_size + cell_size//2),
    20: (0.45*cell_size + cell_size//2, 1.455*cell_size + cell_size//2),
    21: (0.45*cell_size + cell_size//2, 0.455*cell_size + cell_size//2),
    22: (1.45*cell_size + cell_size//2, 0.455*cell_size + cell_size//2),
    23: (2.45*cell_size + cell_size//2, 0.455*cell_size + cell_size//2),
    24: (3.45*cell_size + cell_size//2, 0.455*cell_size + cell_size//2),
    25: (4.45*cell_size + cell_size//2, 0.455*cell_size + cell_size//2),
    26: (5.45*cell_size + cell_size//2, 0.455*cell_size + cell_size//2),
    27: (6.45*cell_size + cell_size//2, 0.455*cell_size + cell_size//2),
    28: (7.45*cell_size + cell_size//2, 0.455*cell_size + cell_size//2),
    29: (8.45*cell_size + cell_size//2, 0.455*cell_size + cell_size//2),
    30: (9.45*cell_size + cell_size//2, 0.455*cell_size + cell_size//2),
    31: (10.45*cell_size + cell_size//2, 0.455*cell_size + cell_size//2),
    32: (11.45*cell_size + cell_size//2, 0.455*cell_size + cell_size//2),
    33: (12.45*cell_size + cell_size//2, 0.455*cell_size + cell_size//2),
    34: (13.45*cell_size + cell_size//2, 0.455*cell_size + cell_size//2),
    35: (13.45*cell_size + cell_size//2, 1.455*cell_size + cell_size//2),
    36: (13.45*cell_size + cell_size//2, 2.455*cell_size + cell_size//2),
    37: (13.45*cell_size + cell_size//2, 3.455*cell_size + cell_size//2),
    38: (13.45*cell_size + cell_size//2, 4.455*cell_size + cell_size//2),
    39: (13.45*cell_size + cell_size//2, 5.455*cell_size + cell_size//2),
    40: (13.45*cell_size + cell_size//2, 6.455*cell_size + cell_size//2),
    41: (13.45*cell_size + cell_size//2, 7.455*cell_size + cell_size//2),
}

# Load the icon image
icon1 = pygame.image.load('assests/images/foodstand.png')
icon1 = pygame.transform.scale(icon1, (40, 40))
icon2 = pygame.image.load('assests/images/hot-dog.png')
icon2 = pygame.transform.scale(icon2, (40, 40))
icon3 = pygame.image.load('assests/images/get-money.png')
icon3 = pygame.transform.scale(icon3, (40, 40))
icon4 = pygame.image.load('assests/images/peach.png')
icon4 = pygame.transform.scale(icon4, (40, 40))
icon5 = pygame.image.load('assests/images/pineapple.png')
icon5 = pygame.transform.scale(icon5, (40, 40))
icon6 = pygame.image.load('assests/images/money.png')
icon6 = pygame.transform.scale(icon6, (40, 40))
icon7 = pygame.image.load('assests/images/vegan.png')
icon7 = pygame.transform.scale(icon7, (40, 40))
icon8 = pygame.image.load('assests/images/grapes.png')
icon8 = pygame.transform.scale(icon8, (40, 40))
icon9 = pygame.image.load('assests/images/banana.png')
icon9 = pygame.transform.scale(icon9, (40, 40))
icon10 = pygame.image.load('assests/images/basket.png')
icon10 = pygame.transform.scale(icon10, (40, 40))
icon11 = pygame.image.load('assests/images/avocado.png')
icon11 = pygame.transform.scale(icon11, (40, 40))
icon12 = pygame.image.load('assests/images/fish-market.png')
icon12 = pygame.transform.scale(icon12, (40, 40))
icon13 = pygame.image.load('assests/images/payment-day.png')
icon13 = pygame.transform.scale(icon13, (40, 40))
icon14 = pygame.image.load('assests/images/food-stall.png')
icon14 = pygame.transform.scale(icon14, (40, 40))
icon15 = pygame.image.load('assests/images/strawberry.png')
icon15 = pygame.transform.scale(icon15, (40, 40))
icon16 = pygame.image.load('assests/images/salmon.png')
icon16 = pygame.transform.scale(icon16, (40, 40))
icon17 = pygame.image.load('assests/images/watermelon.png')
icon17 = pygame.transform.scale(icon17, (40, 40))
icon18 = pygame.image.load('assests/images/potato.png')
icon18 = pygame.transform.scale(icon18, (40, 40))
icon19 = pygame.image.load('assests/images/orange.png')
icon19 = pygame.transform.scale(icon19, (40, 40))
icon20 = pygame.image.load('assests/images/meat.png')
icon20 = pygame.transform.scale(icon20, (40, 40))
icon21 = pygame.image.load('assests/images/lemon.png')
icon21 = pygame.transform.scale(icon21, (40, 40))
icon22 = pygame.image.load('assests/images/cherry.png')
icon22 = pygame.transform.scale(icon22, (40, 40))
icon23 = pygame.image.load('assests/images/baguette.png')
icon23 = pygame.transform.scale(icon23, (40, 40))
icon24 = pygame.image.load('assests/images/corn.png')
icon24 = pygame.transform.scale(icon24, (40, 40))
icon25 = pygame.image.load('assests/images/sausage.png')
icon25 = pygame.transform.scale(icon25, (40, 40))
icon26 = pygame.image.load('assests/images/market.png')
icon26 = pygame.transform.scale(icon26, (40, 40))
icon27 = pygame.image.load('assests/images/apple.png')
icon27 = pygame.transform.scale(icon27, (40, 40))
icon28 = pygame.image.load('assests/images/burden.png')
icon28 = pygame.transform.scale(icon28, (50, 50))


# Blit the icon onto the board surface
screen.blit(icon1, iconpositions[1])
screen.blit(icon2, iconpositions[2])
screen.blit(icon3, iconpositions[3])
screen.blit(icon4, iconpositions[4])
screen.blit(icon5, iconpositions[5])
screen.blit(icon6, iconpositions[6])
screen.blit(icon7, iconpositions[7])
screen.blit(icon8, iconpositions[8])
screen.blit(icon9, iconpositions[9])
screen.blit(icon10, iconpositions[10])
screen.blit(icon11, iconpositions[11])
screen.blit(icon12, iconpositions[12])
screen.blit(icon13, iconpositions[13])
screen.blit(icon14, iconpositions[14])
screen.blit(icon15, iconpositions[15])
screen.blit(icon16, iconpositions[16])
screen.blit(icon6, iconpositions[17])
screen.blit(icon18, iconpositions[18])
screen.blit(icon1, iconpositions[19])
screen.blit(icon20, iconpositions[20])
screen.blit(icon21, iconpositions[21])
screen.blit(icon3, iconpositions[22])
screen.blit(icon7, iconpositions[23])
screen.blit(icon24, iconpositions[24])
screen.blit(icon17, iconpositions[25])
screen.blit(icon22, iconpositions[26])
screen.blit(icon5, iconpositions[27])
screen.blit(icon4, iconpositions[28])
screen.blit(icon8, iconpositions[29])
screen.blit(icon27, iconpositions[30])
screen.blit(icon6, iconpositions[31])
screen.blit(icon25, iconpositions[32])
screen.blit(icon26, iconpositions[33])
screen.blit(icon28, iconpositions[34])
screen.blit(icon23, iconpositions[35])
screen.blit(icon17, iconpositions[36])
screen.blit(icon27, iconpositions[37])
screen.blit(icon11, iconpositions[38])
screen.blit(icon3, iconpositions[39])
screen.blit(icon26, iconpositions[40])
screen.blit(icon19, iconpositions[41])

produce_values = {
    1: 3,
    2: 3,
    4: 1,
    5: 1,
    7: 3,
    8: 1,
    9: 1,
    10: 5,
    11: 1,
    12: 3,
    14: 3,
    15: 1,
    16: 1,
    18: 1,
    19: 3,
    20: 1,
    21: 1,
    23: 2,
    24: 1,
    25: 1,
    26: 1,
    27: 1,
    28: 1,
    29: 1,
    30: 1,
    32: 1,
    33: 3,
    35: 1,
    36: 1,
    37: 1,
    38: 1,
    40: 3,
    41: 1
}
positions_values = {
    1: -50,
    2: -70,
    3: -30,
    4: -20,
    5: -15,
    6: 25,
    7: -85,
    8: -25,
    9: -5,
    11: -20,
    12: -55,
    14: -50,
    15: -25,
    16: -40,
    17: 35,
    18: -25,
    19: -50,
    20: -42,
    21: -15,
    22: -20,
    23: -70,
    24: -10,
    25: -5,
    26: -5,
    27: -10,
    28: -17,
    29: -25,
    30: -15,
    31: 20,
    32: -25,
    33: -50,
    34: -150,
    35: -17,
    36: -5,
    37: -15,
    38: -20,
    39: -35,
    40: -50,
    41: -20
}

positions1 = {
    0: (13.7*cell_size + cell_size//2, 8.75*cell_size + cell_size//2),
    1: (12.7*cell_size + cell_size//2, 8.75*cell_size + cell_size//2),
    2: (11.7*cell_size + cell_size//2, 8.75*cell_size + cell_size//2),
    3: (10.7*cell_size + cell_size//2, 8.75*cell_size + cell_size//2),
    4: (9.7*cell_size + cell_size//2, 8.75*cell_size + cell_size//2),
    5: (8.75*cell_size + cell_size//2, 8.75*cell_size + cell_size//2),
    6: (7.7*cell_size + cell_size//2, 8.75*cell_size + cell_size//2),
    7: (6.7*cell_size + cell_size//2, 8.75*cell_size + cell_size//2),
    8: (5.7*cell_size + cell_size//2, 8.75*cell_size + cell_size//2),
    9: (4.7*cell_size + cell_size//2, 8.75*cell_size + cell_size//2),
    10: (3.7*cell_size + cell_size//2, 8.75*cell_size + cell_size//2),
    11: (2.7*cell_size + cell_size//2, 8.75*cell_size + cell_size//2),
    12: (1.7*cell_size + cell_size//2, 8.75*cell_size + cell_size//2),
    13: (0.7*cell_size + cell_size//2, 8.75*cell_size + cell_size//2),
    14: (0.7*cell_size + cell_size//2, 7.75*cell_size + cell_size//2),
    15: (0.7*cell_size + cell_size//2, 6.75*cell_size + cell_size//2),
    16: (0.7*cell_size + cell_size//2, 5.75*cell_size + cell_size//2),
    17: (0.7*cell_size + cell_size//2, 4.75*cell_size + cell_size//2),
    18: (0.7*cell_size + cell_size//2, 3.75*cell_size + cell_size//2),
    19: (0.7*cell_size + cell_size//2, 2.75*cell_size + cell_size//2),
    20: (0.7*cell_size + cell_size//2, 1.75*cell_size + cell_size//2),
    21: (0.7*cell_size + cell_size//2, 0.75*cell_size + cell_size//2),
    22: (1.7*cell_size + cell_size//2, 0.75*cell_size + cell_size//2),
    23: (2.7*cell_size + cell_size//2, 0.75*cell_size + cell_size//2),
    24: (3.7*cell_size + cell_size//2, 0.75*cell_size + cell_size//2),
    25: (4.7*cell_size + cell_size//2, 0.75*cell_size + cell_size//2),
    26: (5.7*cell_size + cell_size//2, 0.75*cell_size + cell_size//2),
    27: (6.7*cell_size + cell_size//2, 0.75*cell_size + cell_size//2),
    28: (7.7*cell_size + cell_size//2, 0.75*cell_size + cell_size//2),
    29: (8.7*cell_size + cell_size//2, 0.75*cell_size + cell_size//2),
    30: (9.7*cell_size + cell_size//2, 0.75*cell_size + cell_size//2),
    31: (10.7*cell_size + cell_size//2, 0.75*cell_size + cell_size//2),
    32: (11.7*cell_size + cell_size//2, 0.75*cell_size + cell_size//2),
    33: (12.7*cell_size + cell_size//2, 0.75*cell_size + cell_size//2),
    34: (13.7*cell_size + cell_size//2, 0.75*cell_size + cell_size//2),
    35: (13.7*cell_size + cell_size//2, 1.75*cell_size + cell_size//2),
    36: (13.7*cell_size + cell_size//2, 2.75*cell_size + cell_size//2),
    37: (13.7*cell_size + cell_size//2, 3.75*cell_size + cell_size//2),
    38: (13.7*cell_size + cell_size//2, 4.75*cell_size + cell_size//2),
    39: (13.7*cell_size + cell_size//2, 5.75*cell_size + cell_size//2),
    40: (13.7*cell_size + cell_size//2, 6.75*cell_size + cell_size//2),
    41: (13.7*cell_size + cell_size//2, 7.75*cell_size + cell_size//2),
}

positions2 = {
    0: (13.3*cell_size + cell_size//2, 8.75*cell_size + cell_size//2),
    1: (12.3*cell_size + cell_size//2, 8.75*cell_size + cell_size//2),
    2: (11.3*cell_size + cell_size//2, 8.75*cell_size + cell_size//2),
    3: (10.3*cell_size + cell_size//2, 8.75*cell_size + cell_size//2),
    4: (9.3*cell_size + cell_size//2, 8.75*cell_size + cell_size//2),
    5: (8.35*cell_size + cell_size//2, 8.75*cell_size + cell_size//2),
    6: (7.3*cell_size + cell_size//2, 8.75*cell_size + cell_size//2),
    7: (6.3*cell_size + cell_size//2, 8.75*cell_size + cell_size//2),
    8: (5.3*cell_size + cell_size//2, 8.75*cell_size + cell_size//2),
    9: (4.3*cell_size + cell_size//2, 8.75*cell_size + cell_size//2),
    10: (3.3*cell_size + cell_size//2, 8.75*cell_size + cell_size//2),
    11: (2.3*cell_size + cell_size//2, 8.75*cell_size + cell_size//2),
    12: (1.3*cell_size + cell_size//2, 8.75*cell_size + cell_size//2),
    13: (0.3*cell_size + cell_size//2, 8.75*cell_size + cell_size//2),
    14: (0.3*cell_size + cell_size//2, 7.75*cell_size + cell_size//2),
    15: (0.3*cell_size + cell_size//2, 6.75*cell_size + cell_size//2),
    16: (0.3*cell_size + cell_size//2, 5.75*cell_size + cell_size//2),
    17: (0.3*cell_size + cell_size//2, 4.75*cell_size + cell_size//2),
    18: (0.3*cell_size + cell_size//2, 3.75*cell_size + cell_size//2),
    19: (0.3*cell_size + cell_size//2, 2.75*cell_size + cell_size//2),
    20: (0.3*cell_size + cell_size//2, 1.75*cell_size + cell_size//2),
    21: (0.3*cell_size + cell_size//2, 0.75*cell_size + cell_size//2),
    22: (1.3*cell_size + cell_size//2, 0.75*cell_size + cell_size//2),
    23: (2.3*cell_size + cell_size//2, 0.75*cell_size + cell_size//2),
    24: (3.3*cell_size + cell_size//2, 0.75*cell_size + cell_size//2),
    25: (4.3*cell_size + cell_size//2, 0.75*cell_size + cell_size//2),
    26: (5.3*cell_size + cell_size//2, 0.75*cell_size + cell_size//2),
    27: (6.3*cell_size + cell_size//2, 0.75*cell_size + cell_size//2),
    28: (7.3*cell_size + cell_size//2, 0.75*cell_size + cell_size//2),
    29: (8.3*cell_size + cell_size//2, 0.75*cell_size + cell_size//2),
    30: (9.3*cell_size + cell_size//2, 0.75*cell_size + cell_size//2),
    31: (10.3*cell_size + cell_size//2, 0.75*cell_size + cell_size//2),
    32: (11.3*cell_size + cell_size//2, 0.75*cell_size + cell_size//2),
    33: (12.3*cell_size + cell_size//2, 0.75*cell_size + cell_size//2),
    34: (13.3*cell_size + cell_size//2, 0.75*cell_size + cell_size//2),
    35: (13.3*cell_size + cell_size//2, 1.75*cell_size + cell_size//2),
    36: (13.3*cell_size + cell_size//2, 2.75*cell_size + cell_size//2),
    37: (13.3*cell_size + cell_size//2, 3.75*cell_size + cell_size//2),
    38: (13.3*cell_size + cell_size//2, 4.75*cell_size + cell_size//2),
    39: (13.3*cell_size + cell_size//2, 5.75*cell_size + cell_size//2),
    40: (13.3*cell_size + cell_size//2, 6.75*cell_size + cell_size//2),
    41: (13.3*cell_size + cell_size//2, 7.75*cell_size + cell_size//2),
}

positions3 = {
    0: (13.5*cell_size + cell_size//2, 8.25*cell_size + cell_size//2),
    1: (12.5*cell_size + cell_size//2, 8.25*cell_size + cell_size//2),
    2: (11.5*cell_size + cell_size//2, 8.25*cell_size + cell_size//2),
    3: (10.5*cell_size + cell_size//2, 8.25*cell_size + cell_size//2),
    4: (9.5*cell_size + cell_size//2, 8.25*cell_size + cell_size//2),
    5: (8.55*cell_size + cell_size//2, 8.25*cell_size + cell_size//2),
    6: (7.5*cell_size + cell_size//2, 8.25*cell_size + cell_size//2),
    7: (6.5*cell_size + cell_size//2, 8.25*cell_size + cell_size//2),
    8: (5.5*cell_size + cell_size//2, 8.25*cell_size + cell_size//2),
    9: (4.5*cell_size + cell_size//2, 8.25*cell_size + cell_size//2),
    10: (3.5*cell_size + cell_size//2, 8.25*cell_size + cell_size//2),
    11: (2.5*cell_size + cell_size//2, 8.25*cell_size + cell_size//2),
    12: (1.5*cell_size + cell_size//2, 8.25*cell_size + cell_size//2),
    13: (0.5*cell_size + cell_size//2, 8.25*cell_size + cell_size//2),
    14: (0.5*cell_size + cell_size//2, 7.25*cell_size + cell_size//2),
    15: (0.5*cell_size + cell_size//2, 6.25*cell_size + cell_size//2),
    16: (0.5*cell_size + cell_size//2, 5.25*cell_size + cell_size//2),
    17: (0.5*cell_size + cell_size//2, 4.25*cell_size + cell_size//2),
    18: (0.5*cell_size + cell_size//2, 3.25*cell_size + cell_size//2),
    19: (0.5*cell_size + cell_size//2, 2.25*cell_size + cell_size//2),
    20: (0.5*cell_size + cell_size//2, 1.25*cell_size + cell_size//2),
    21: (0.5*cell_size + cell_size//2, 0.25*cell_size + cell_size//2),
    22: (1.5*cell_size + cell_size//2, 0.25*cell_size + cell_size//2),
    23: (2.5*cell_size + cell_size//2, 0.25*cell_size + cell_size//2),
    24: (3.5*cell_size + cell_size//2, 0.25*cell_size + cell_size//2),
    25: (4.5*cell_size + cell_size//2, 0.25*cell_size + cell_size//2),
    26: (5.5*cell_size + cell_size//2, 0.25*cell_size + cell_size//2),
    27: (6.5*cell_size + cell_size//2, 0.25*cell_size + cell_size//2),
    28: (7.5*cell_size + cell_size//2, 0.25*cell_size + cell_size//2),
    29: (8.5*cell_size + cell_size//2, 0.25*cell_size + cell_size//2),
    30: (9.5*cell_size + cell_size//2, 0.25*cell_size + cell_size//2),
    31: (10.5*cell_size + cell_size//2, 0.25*cell_size + cell_size//2),
    32: (11.5*cell_size + cell_size//2, 0.25*cell_size + cell_size//2),
    33: (12.5*cell_size + cell_size//2, 0.25*cell_size + cell_size//2),
    34: (13.5*cell_size + cell_size//2, 0.25*cell_size + cell_size//2),
    35: (13.5*cell_size + cell_size//2, 1.25*cell_size + cell_size//2),
    36: (13.5*cell_size + cell_size//2, 2.25*cell_size + cell_size//2),
    37: (13.5*cell_size + cell_size//2, 3.25*cell_size + cell_size//2),
    38: (13.5*cell_size + cell_size//2, 4.25*cell_size + cell_size//2),
    39: (13.5*cell_size + cell_size//2, 5.25*cell_size + cell_size//2),
    40: (13.5*cell_size + cell_size//2, 6.25*cell_size + cell_size//2),
    41: (13.5*cell_size + cell_size//2, 7.25*cell_size + cell_size//2),
}



scoreboard = pygame.surface.Surface((scoreboardw, scoreboardh))
scoreboard.fill( (46,139,87))
#(53, 94, 59)
# Draw a grid on the game board
cell_size = 150
for x in range(0, scoreboardw, cell_size):
    for y in range(0, scoreboardh, cell_size):
        rect = pygame.Rect(x, y, cell_size, cell_size)
        pygame.draw.rect(scoreboard, (255,255,255), rect, 1)

board_position = ((windoww - scoreboardw) // 1.05, (windowh - scoreboardh) // 1.3289)
screen.blit(scoreboard, board_position)

font = pygame.font.Font('assests/fonts/April Easter.ttf', 20)
name_surface = font.render(player_name[0], True, (255,255,255))
name_rect = name_surface.get_rect(center=(7.6*cell_size + cell_size//2, 1.15*cell_size + cell_size//2))
name_surface1 = font.render(player_name[1], True, (255,255,255))
name_rect1 = name_surface1.get_rect(center=(7.6*cell_size + cell_size//2, 2.15*cell_size + cell_size//2))
name_surface2 = font.render(player_name[2], True, (255,255,255))
name_rect2 = name_surface2.get_rect(center=(7.6*cell_size + cell_size//2, 3.15*cell_size + cell_size//2))

balances = [700, 700, 700]
font = pygame.font.Font('assests/fonts/Amaranth-Bold.ttf', 26)
score_surface = font.render("$"+str(balances[0]), True, (255,0,0))
score_rect = score_surface.get_rect(center=(7.6*cell_size + cell_size//2, 1.4*cell_size + cell_size//2))
score_surface1 = font.render("$"+str(balances[1]), True, (0,0,245))
score_rect1 = score_surface1.get_rect(center=(7.6*cell_size + cell_size//2, 2.4*cell_size + cell_size//2))
score_surface2 = font.render("$"+str(balances[2]), True, (245,0,255))
score_rect2 = score_surface2.get_rect(center=(7.6*cell_size + cell_size//2, 3.4*cell_size + cell_size//2))

produce = [0, 0, 0]
score = [0, 0, 0]
font = pygame.font.Font('assests/fonts/April Easter.ttf', 16)
produce_surface = font.render("Produce: "+str(produce[0]), True, (255,255,255))
produce_rect = produce_surface.get_rect(center=(7.6*cell_size + cell_size//2, 1.7*cell_size + cell_size//2))
produce_surface1 = font.render("Produce: "+str(produce[1]), True, (255,255,255))
produce_rect1 = produce_surface1.get_rect(center=(7.6*cell_size + cell_size//2, 2.7*cell_size + cell_size//2))
produce_surface2 = font.render("Produce: "+str(produce[2]), True, (255,255,255))
produce_rect2 = produce_surface2.get_rect(center=(7.6*cell_size + cell_size//2, 3.7*cell_size + cell_size//2))

font = pygame.font.Font('assests/fonts/April Easter.ttf', 20)
ave_surface = font.render("Score", True, (255,255,255))
ave_rect = ave_surface.get_rect(center=(7.5*cell_size + cell_size//2, 0.0*cell_size + cell_size//2))

ave_surface1 = font.render(player_name[0]+": ", True, (255,255,255))
ave_rect1 = ave_surface1.get_rect(center=(7.3*cell_size + cell_size//2, 0.2*cell_size + cell_size//2))
ave_surface11 = font.render(str(score[0]), True, (255,255,255))
ave_rect11 = ave_surface11.get_rect(center=(7.9*cell_size + cell_size//2, 0.2*cell_size + cell_size//2))

ave_surface2 = font.render(player_name[1]+": " , True, (255,255,255))
ave_rect2 = ave_surface2.get_rect(center=(7.3*cell_size + cell_size//2, 0.4*cell_size + cell_size//2))
ave_surface22 = font.render(str(score[1]), True, (255,255,255))
ave_rect22 = ave_surface22.get_rect(center=(7.9*cell_size + cell_size//2, 0.4*cell_size + cell_size//2))

ave_surface3 = font.render(player_name[2]+": ", True, (255,255,255))
ave_rect3 = ave_surface3.get_rect(center=(7.3*cell_size + cell_size//2, 0.6*cell_size + cell_size//2))
ave_surface33 = font.render(str(score[2]), True, (255,255,255))
ave_rect33 = ave_surface33.get_rect(center=(7.9*cell_size + cell_size//2, 0.6*cell_size + cell_size//2))

screen.blit(score_surface, score_rect)
screen.blit(score_surface1, score_rect1)
screen.blit(score_surface2, score_rect2)

screen.blit(produce_surface, produce_rect)
screen.blit(produce_surface1, produce_rect1)
screen.blit(produce_surface2, produce_rect2)

screen.blit(name_surface, name_rect)
screen.blit(name_surface1, name_rect1)
screen.blit(name_surface2, name_rect2)

screen.blit(ave_surface, ave_rect)
screen.blit(ave_surface1, ave_rect1)
screen.blit(ave_surface2, ave_rect2)
screen.blit(ave_surface3, ave_rect3)
screen.blit(ave_surface11, ave_rect11)
screen.blit(ave_surface22, ave_rect22)
screen.blit(ave_surface33, ave_rect33)

player1 = pygame.image.load('assests/images/red.png')
player1 = pygame.transform.scale(player1, (20, 20))

player2 = pygame.image.load('assests/images/blue.png')
player2 = pygame.transform.scale(player2, (20, 20))

player3 = pygame.image.load('assests/images/purple.png')
player3 = pygame.transform.scale(player3, (20, 20))

screen.blit(player1, positions1[0])
screen.blit(player2, positions2[0])
screen.blit(player3, positions3[0])

# Set up the turn order of the players
players = [player1,player2, player3]
player_positions = [0, 0, 0]
current_player = 0
sumpos = 0
total = 0

font = pygame.font.Font('assests/fonts/April Easter.ttf', 40)
win_instruction = font.render(player_name[current_player] + " has Won!", True, (0, 48, 143))
win_rect = win_instruction.get_rect()
win_rect.center = (int(windoww // 2.6), int(windowh - 350))

font = pygame.font.Font('assests/fonts/April Easter.ttf', 26)
turn_instructionl = font.render(player_name[current_player] + " rolled a double. Roll again!", True, (255, 255, 255))
turnrectl = turn_instructionl.get_rect()
turnrectl.center = (int(windoww // 2.7), int(windowh - 170))


# Set up of the font for the text
font = pygame.font.Font('assests/fonts/Amaranth-Regular.ttf', 26)
instruction = font.render("Press Space To Roll The Dice, R to Reset and E to Exit", True, (255, 255, 255))
instruction_rect = instruction.get_rect()
instruction_rect.center = (int(windoww // 2.6), int(windowh - 50))

font = pygame.font.Font('assests/fonts/April Easter.ttf', 26)
turn_instruction = font.render(player_name[0] + "'s turn", True, (255, 255, 255))
turn_rect = turn_instruction.get_rect()
turn_rect.center = (int(windoww // 2.6), int(windowh - 170))

# Scale the instruct image to cover the whole width of the screen
instruct = pygame.image.load('assests/images/instruct.PNG')
instruct = pygame.transform.scale(instruct, (890, 75))


# Blit the new text
screen.blit(instruction, instruction_rect)
screen.blit(turn_instruction, turn_rect)

# Update the display
pygame.display.update()

roll1= 0
roll2 = 0
#positions of dice x and y axes
y1 = (2.5 * cell_size) + (cell_size / 2)
x1 =(3 * cell_size) + (cell_size / 2)
y2 = (2.5 * cell_size) + (cell_size / 2)
x2 =(2.3 * cell_size) + (cell_size / 2)

dice_images = {
    1: 'assests/images/1.png',
    2: 'assests/images/2.png',
    3: 'assests/images/3.png',
    4: 'assests/images/4.png',
    5: 'assests/images/5.png',
    6: 'assests/images/6.png'
}

# index of the current player in the players list
player = 0
num_players = 3
def reset_game():
    global player_positions, balances, produce, current_player, roll1, roll2, sumpos, total, sum, game_over
    screen.blit(scoreboard, board_position)

    player_positions = [0, 0, 0]
    balances = [700, 700, 700]
    font = pygame.font.Font('assests/fonts/Amaranth-Bold.ttf', 26)
    score_surface = font.render("$"+str(balances[0]), True, (255,0,0))
    score_rect = score_surface.get_rect(center=(7.6*cell_size + cell_size//2, 1.4*cell_size + cell_size//2))
    score_surface1 = font.render("$"+str(balances[1]), True, (0,0,245))
    score_rect1 = score_surface1.get_rect(center=(7.6*cell_size + cell_size//2, 2.4*cell_size + cell_size//2))
    score_surface2 = font.render("$"+str(balances[2]), True, (245,0,255))
    score_rect2 = score_surface2.get_rect(center=(7.6*cell_size + cell_size//2, 3.4*cell_size + cell_size//2))
    screen.blit(score_surface, score_rect)
    screen.blit(score_surface1, score_rect1)
    screen.blit(score_surface2, score_rect2)
    produce = [0, 0, 0]
    font = pygame.font.Font('assests/fonts/April Easter.ttf', 16)
    produce_surface = font.render("Produce: "+str(produce[0]), True, (255,255,255))
    produce_rect = produce_surface.get_rect(center=(7.6*cell_size + cell_size//2, 1.7*cell_size + cell_size//2))
    produce_surface1 = font.render("Produce: "+str(produce[1]), True, (255,255,255))
    produce_rect1 = produce_surface1.get_rect(center=(7.6*cell_size + cell_size//2, 2.7*cell_size + cell_size//2))
    produce_surface2 = font.render("Produce: "+str(produce[2]), True, (255,255,255))
    produce_rect2 = produce_surface2.get_rect(center=(7.6*cell_size + cell_size//2, 3.7*cell_size + cell_size//2))
    screen.blit(produce_surface, produce_rect)
    screen.blit(produce_surface1, produce_rect1)
    screen.blit(produce_surface2, produce_rect2)
    current_player = 0
    roll1 = 0
    roll2 = 0
    sumpos = 0
    total = 0

    font = pygame.font.Font('assests/fonts/April Easter.ttf', 26)
    turn_instruction = font.render(player_1.name + "'s turn", True, (255, 255, 255))
    turn_rect = turn_instruction.get_rect()
    turn_rect.center = (int(windoww // 2.6), int(windowh - 170))

    # Clear the area where the turn instruction is displayed
    screen.blit(instruct, (int(windoww // 2.6) - 860 // 2, int(windowh - 204.5), 860, turn_rect.height))
    
    screen.blit(board1, board_rect.topleft + board1_pos)
    screen.blit(board2, board_rect.topleft + board2_pos)
    screen.blit(board3, board_rect.topleft + board3_pos)
    screen.blit(board4, board4_pos)

    screen.blit(text_surface, text_rect)

    # Blit the icon onto the board surface
    screen.blit(icon1, iconpositions[1])
    screen.blit(icon2, iconpositions[2])
    screen.blit(icon3, iconpositions[3])
    screen.blit(icon4, iconpositions[4])
    screen.blit(icon5, iconpositions[5])
    screen.blit(icon6, iconpositions[6])
    screen.blit(icon7, iconpositions[7])
    screen.blit(icon8, iconpositions[8])
    screen.blit(icon9, iconpositions[9])
    screen.blit(icon10, iconpositions[10])
    screen.blit(icon11, iconpositions[11])
    screen.blit(icon12, iconpositions[12])
    screen.blit(icon13, iconpositions[13])
    screen.blit(icon14, iconpositions[14])
    screen.blit(icon15, iconpositions[15])
    screen.blit(icon16, iconpositions[16])
    screen.blit(icon6, iconpositions[17])
    screen.blit(icon18, iconpositions[18])
    screen.blit(icon1, iconpositions[19])
    screen.blit(icon20, iconpositions[20])
    screen.blit(icon21, iconpositions[21])
    screen.blit(icon3, iconpositions[22])
    screen.blit(icon7, iconpositions[23])
    screen.blit(icon24, iconpositions[24])
    screen.blit(icon17, iconpositions[25])
    screen.blit(icon22, iconpositions[26])
    screen.blit(icon5, iconpositions[27])
    screen.blit(icon4, iconpositions[28])
    screen.blit(icon8, iconpositions[29])
    screen.blit(icon27, iconpositions[30])
    screen.blit(icon6, iconpositions[31])
    screen.blit(icon25, iconpositions[32])
    screen.blit(icon26, iconpositions[33])
    screen.blit(icon28, iconpositions[34])
    screen.blit(icon23, iconpositions[35])
    screen.blit(icon17, iconpositions[36])
    screen.blit(icon27, iconpositions[37])
    screen.blit(icon11, iconpositions[38])
    screen.blit(icon3, iconpositions[39])
    screen.blit(icon26, iconpositions[40])
    screen.blit(icon19, iconpositions[41])

    screen.blit(player1, positions1[0])
    screen.blit(player2, positions2[0])
    screen.blit(player3, positions3[0])

    screen.blit(reimage.subsurface(turn_rect), turn_rect)

    screen.blit(instruction, instruction_rect)
    screen.blit(turn_instruction, turn_rect)
    screen.blit(reimage.subsurface(win_rect), win_rect)

    font = pygame.font.Font('assests/fonts/April Easter.ttf', 20)
    name_surface = font.render(player_name[0], True, (255,255,255))
    name_rect = name_surface.get_rect(center=(7.6*cell_size + cell_size//2, 1.15*cell_size + cell_size//2))
    name_surface1 = font.render(player_name[1], True, (255,255,255))
    name_rect1 = name_surface1.get_rect(center=(7.6*cell_size + cell_size//2, 2.15*cell_size + cell_size//2))
    name_surface2 = font.render(player_name[2], True, (255,255,255))
    name_rect2 = name_surface2.get_rect(center=(7.6*cell_size + cell_size//2, 3.15*cell_size + cell_size//2))
    screen.blit(name_surface, name_rect)
    screen.blit(name_surface1, name_rect1)
    screen.blit(name_surface2, name_rect2)

    game_over = False

# Start the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Check if the current player has won
        if (balances[current_player]) >= 0 and produce[current_player] >= 20:
            win_sound.play()
            # Display winner message
            font = pygame.font.Font('assests/fonts/April Easter.ttf', 40)
            win_instruction = font.render(player_name[current_player] + " has Won!", True, (0, 48, 143))
            win_rect = win_instruction.get_rect()
            win_rect.center = (int(windoww // 2.6), int(windowh - 350))

            screen.blit(reimage.subsurface(win_rect), win_rect)
            screen.blit(win_instruction,win_rect)

            # Clear the area where the turn instruction is displayed
            screen.blit(instruct, (int(windoww // 2.6) - 860 // 2, int(windowh - 204.5), 860, turn_rect.height))

            # Remove the player image from the previous position
            screen.blit(board1, board_rect.topleft + board1_pos)
            screen.blit(board2, board_rect.topleft + board2_pos)
            screen.blit(board3, board_rect.topleft + board3_pos)
            screen.blit(board4, board4_pos)
            screen.blit(text_surface, text_rect)
                
                # Blit the icon onto the board surface
            screen.blit(icon1, iconpositions[1])
            screen.blit(icon2, iconpositions[2])
            screen.blit(icon3, iconpositions[3])
            screen.blit(icon4, iconpositions[4])
            screen.blit(icon5, iconpositions[5])
            screen.blit(icon6, iconpositions[6])
            screen.blit(icon7, iconpositions[7])
            screen.blit(icon8, iconpositions[8])
            screen.blit(icon9, iconpositions[9])
            screen.blit(icon10, iconpositions[10])
            screen.blit(icon11, iconpositions[11])
            screen.blit(icon12, iconpositions[12])
            screen.blit(icon13, iconpositions[13])
            screen.blit(icon14, iconpositions[14])
            screen.blit(icon15, iconpositions[15])
            screen.blit(icon16, iconpositions[16])
            screen.blit(icon6, iconpositions[17])
            screen.blit(icon18, iconpositions[18])
            screen.blit(icon1, iconpositions[19])
            screen.blit(icon20, iconpositions[20])
            screen.blit(icon21, iconpositions[21])
            screen.blit(icon3, iconpositions[22])
            screen.blit(icon7, iconpositions[23])
            screen.blit(icon24, iconpositions[24])
            screen.blit(icon17, iconpositions[25])
            screen.blit(icon22, iconpositions[26])
            screen.blit(icon5, iconpositions[27])
            screen.blit(icon4, iconpositions[28])
            screen.blit(icon8, iconpositions[29])
            screen.blit(icon27, iconpositions[30])
            screen.blit(icon6, iconpositions[31])
            screen.blit(icon25, iconpositions[32])
            screen.blit(icon26, iconpositions[33])
            screen.blit(icon28, iconpositions[34])
            screen.blit(icon23, iconpositions[35])
            screen.blit(icon17, iconpositions[36])
            screen.blit(icon27, iconpositions[37])
            screen.blit(icon11, iconpositions[38])
            screen.blit(icon3, iconpositions[39])
            screen.blit(icon26, iconpositions[40])
            screen.blit(icon19, iconpositions[41])

            # Blit the players onto the board
            screen.blit(players[0], positions1[player_positions[0]])
            screen.blit(players[1], positions2[player_positions[1]])
            screen.blit(players[2], positions3[player_positions[2]])

            # Prevent further player actions
            can_press_space = False

    # Keep the window open until the players decide to reset or quit the game
        else:
            # Allow player to press spacebar
            can_press_space = True

        # Handle player actions
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and can_press_space:
            current_player = (player + 1) % len(player_name)
            if balances[current_player] <= 0:
                # Skip player icon for player who has lost
                if current_player == 0:
                    screen.blit(players[1], positions2[player_positions[1]])
                    screen.blit(players[2], positions3[player_positions[2]])
                elif current_player == 1:
                    screen.blit(players[0], positions1[player_positions[0]])
                    screen.blit(players[2], positions3[player_positions[2]])
                else:
                    screen.blit(players[0], positions1[player_positions[0]])
                    screen.blit(players[1], positions2[player_positions[1]])
                
                # Display the loss instruction
                font = pygame.font.Font('assests/fonts/April Easter.ttf', 26)
                loss_instruction = font.render(player_name[current_player] + " has lost!", True, (255, 0, 0))
                loss_rect = loss_instruction.get_rect()
                loss_rect.center = (int(windoww // 2.6), int(windowh - 170))
                screen.blit(reimage.subsurface(loss_rect), loss_rect)
                screen.blit(loss_instruction,loss_rect)

                # Move to the next player
                current_player = (current_player + 1) % len(player_name)
            
            if event.key == pygame.K_SPACE:
                roll1 = random.randint(1,6)
                roll2 = random.randint(1,6) 

                # Load the dice image for roll1
                dice1 = pygame.image.load(dice_images[roll1])
                dice1 = pygame.transform.scale(dice1, (100,100))
                screen.blit(dice1, (x1,y1))

                # Load the dice image for roll2
                dice2 = pygame.image.load(dice_images[roll2])
                dice2 = pygame.transform.scale(dice2, (100,100))
                screen.blit(dice2, (x2,y2))

                dice_sound.play() 

                # Update the player position
                sumpos = roll1 + roll2
                total = (total + sumpos) % 42

                # Display which player's turn it is
                font = pygame.font.Font('assests/fonts/April Easter.ttf', 26)
                turn_instruction = font.render(player_name[current_player] + "'s turn", True, (255, 255, 255))
                turn_rect = turn_instruction.get_rect()
                turn_rect.center = (int(windoww // 2.6), int(windowh - 170))

                # Clear the area where the turn instruction is displayed
                screen.blit(instruct, (int(windoww // 2.6) - 860 // 2, int(windowh - 204.5), 860, turn_rect.height))

                # Blit the new text
                screen.blit(turn_instruction, turn_rect)

                player_positions[current_player] = (player_positions[current_player] + sumpos) % 42

                # Blit the player image onto the board
                screen.blit(player1, positions1[player_positions[0]])
                screen.blit(player2, positions2[player_positions[1]])
                screen.blit(player3, positions3[player_positions[2]])

                # Remove the player image from the previous position
                screen.blit(board1, board_rect.topleft + board1_pos)
                screen.blit(board2, board_rect.topleft + board2_pos)
                screen.blit(board3, board_rect.topleft + board3_pos)
                screen.blit(board4, board4_pos)
                screen.blit(text_surface, text_rect)
                
                # Blit the icon onto the board surface
                screen.blit(icon1, iconpositions[1])
                screen.blit(icon2, iconpositions[2])
                screen.blit(icon3, iconpositions[3])
                screen.blit(icon4, iconpositions[4])
                screen.blit(icon5, iconpositions[5])
                screen.blit(icon6, iconpositions[6])
                screen.blit(icon7, iconpositions[7])
                screen.blit(icon8, iconpositions[8])
                screen.blit(icon9, iconpositions[9])
                screen.blit(icon10, iconpositions[10])
                screen.blit(icon11, iconpositions[11])
                screen.blit(icon12, iconpositions[12])
                screen.blit(icon13, iconpositions[13])
                screen.blit(icon14, iconpositions[14])
                screen.blit(icon15, iconpositions[15])
                screen.blit(icon16, iconpositions[16])
                screen.blit(icon6, iconpositions[17])
                screen.blit(icon18, iconpositions[18])
                screen.blit(icon1, iconpositions[19])
                screen.blit(icon20, iconpositions[20])
                screen.blit(icon21, iconpositions[21])
                screen.blit(icon3, iconpositions[22])
                screen.blit(icon7, iconpositions[23])
                screen.blit(icon24, iconpositions[24])
                screen.blit(icon17, iconpositions[25])
                screen.blit(icon22, iconpositions[26])
                screen.blit(icon5, iconpositions[27])
                screen.blit(icon4, iconpositions[28])
                screen.blit(icon8, iconpositions[29])
                screen.blit(icon27, iconpositions[30])
                screen.blit(icon6, iconpositions[31])
                screen.blit(icon25, iconpositions[32])
                screen.blit(icon26, iconpositions[33])
                screen.blit(icon28, iconpositions[34])
                screen.blit(icon23, iconpositions[35])
                screen.blit(icon17, iconpositions[36])
                screen.blit(icon27, iconpositions[37])
                screen.blit(icon11, iconpositions[38])
                screen.blit(icon3, iconpositions[39])
                screen.blit(icon26, iconpositions[40])
                screen.blit(icon19, iconpositions[41])

                # Blit the players onto the board
                screen.blit(players[0], positions1[player_positions[0]])
                screen.blit(players[1], positions2[player_positions[1]])
                screen.blit(players[2], positions3[player_positions[2]])
                move_sound.play()
                player += 1

                # Update the balance if the player lands on a position with a value
                if player_positions[current_player] in positions_values:
                    position_value = positions_values[player_positions[current_player]]
                    if player_positions[current_player] == 34:
                        balances[current_player] -= 150
                        player_positions[current_player] = 13

                        turn_instructiono = font.render( player_name[current_player] + " Your Tax is overdue! Pay $150 and go back to 13!", True, (255, 255, 255))
                        turnrecto = turn_instructiono.get_rect()
                        turnrecto.center = (int(windoww // 2.7), int(windowh - 170))

                        # Blit the part of the background image corresponding to the text area
                        screen.blit(reimage.subsurface(turnrecto), turnrecto)

                        # Blit the new text
                        screen.blit(turn_instructiono, turnrecto)

                    else:
                        balances[current_player] += position_value

                                                

                # Update the balance of fruits in basket        
                if player_positions[current_player] in produce_values:
                    produce_value = produce_values[player_positions[current_player]]
                    produce[current_player] += produce_value
                    score[current_player] += produce_value
                    
                    if position_value < 0:
                        taken_sound.play()
                    else:
                        coin_sound.play()
                screen.blit(reimage.subsurface(ave_rect11), ave_rect11)
                screen.blit(reimage.subsurface(ave_rect22), ave_rect22)
                screen.blit(reimage.subsurface(ave_rect33), ave_rect33)

                ave_surface11 = font.render(str(score[0]), True, (255,255,255))
                ave_rect11 = ave_surface11.get_rect(center=(7.9*cell_size + cell_size//2, 0.2*cell_size + cell_size//2))
                screen.blit(ave_surface11, ave_rect11)

                ave_rect2 = ave_surface2.get_rect(center=(7.3*cell_size + cell_size//2, 0.4*cell_size + cell_size//2))
                ave_surface22 = font.render(str(score[1]), True, (255,255,255))
                ave_rect22 = ave_surface22.get_rect(center=(7.9*cell_size + cell_size//2, 0.4*cell_size + cell_size//2))
                screen.blit(ave_surface22, ave_rect22)

                ave_rect3 = ave_surface3.get_rect(center=(7.3*cell_size + cell_size//2, 0.6*cell_size + cell_size//2))
                ave_surface33 = font.render(str(score[2]), True, (255,255,255))
                ave_rect33 = ave_surface33.get_rect(center=(7.9*cell_size + cell_size//2, 0.6*cell_size + cell_size//2))
                screen.blit(ave_surface33, ave_rect33)


                if roll1 == roll2:

                    # Blit the part of the background image corresponding to the text area
                    screen.blit(reimage.subsurface(turnrectl), turnrectl)

                    # Blit the new text
                    screen.blit(turn_instructionl, turnrectl)

                    # Load the dice image for roll3
                    sumpos = roll1 + roll2

                    # Load the dice image for roll3
                    screen.blit(dice1, (x1,y1))

                    # Load the dice image for roll4
                    screen.blit(dice2, (x2,y2))

                    # Update the player position
                    total += sumpos
                    player_positions[current_player] = (player_positions[current_player] + sumpos) % 42
                    balances[current_player] += position_value
                else:
                    current_player = (current_player + 1) % len(player_name)
                    
                # Update the scoreboard with the new balances
                screen.blit(scoreboard, board_position)

                font = pygame.font.Font('assests/fonts/April Easter.ttf', 20)
                name_surface = font.render(player_name[0], True, (255,255,255))
                name_rect = name_surface.get_rect(center=(7.6*cell_size + cell_size//2, 1.15*cell_size + cell_size//2))
                name_surface1 = font.render(player_name[1], True, (255,255,255))
                name_rect1 = name_surface1.get_rect(center=(7.6*cell_size + cell_size//2, 2.15*cell_size + cell_size//2))
                name_surface2 = font.render(player_name[2], True, (255,255,255))
                name_rect2 = name_surface2.get_rect(center=(7.6*cell_size + cell_size//2, 3.15*cell_size + cell_size//2))

                screen.blit(name_surface, name_rect)
                screen.blit(name_surface1, name_rect1)
                screen.blit(name_surface2, name_rect2)

                font = pygame.font.Font('assests/fonts/Amaranth-Bold.ttf', 26)                
                score_surface = font.render("$"+str(balances[0]), True, (255,0,0))
                score_rect = score_surface.get_rect(center=(7.6*cell_size + cell_size//2, 1.4*cell_size + cell_size//2))
                score_surface1 = font.render("$"+str(balances[1]), True, (0,0,245))
                score_rect1 = score_surface1.get_rect(center=(7.6*cell_size + cell_size//2, 2.4*cell_size + cell_size//2))
                score_surface2 = font.render("$"+str(balances[2]), True, (245,0,255))
                score_rect2 = score_surface2.get_rect(center=(7.6*cell_size + cell_size//2, 3.4*cell_size + cell_size//2))

                screen.blit(score_surface, score_rect)
                screen.blit(score_surface1, score_rect1)
                screen.blit(score_surface2, score_rect2)

                font = pygame.font.Font('assests/fonts/April Easter.ttf', 16)
                produce_surface = font.render("Produce: "+str(produce[0]), True, (255,255,255))
                produce_rect = produce_surface.get_rect(center=(7.6*cell_size + cell_size//2, 1.7*cell_size + cell_size//2))
                produce_surface1 = font.render("Produce: "+str(produce[1]), True, (255,255,255))
                produce_rect1 = produce_surface1.get_rect(center=(7.6*cell_size + cell_size//2, 2.7*cell_size + cell_size//2))
                produce_surface2 = font.render("Produce: "+str(produce[2]), True, (255,255,255))
                produce_rect2 = produce_surface2.get_rect(center=(7.6*cell_size + cell_size//2, 3.7*cell_size + cell_size//2))

                screen.blit(produce_surface, produce_rect)
                screen.blit(produce_surface1, produce_rect1)
                screen.blit(produce_surface2, produce_rect2)
                win_sound.stop()


        screen.blit(instruction, instruction_rect)
        # Check if the 'r' key is pressed to restart the game
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            reset_game()
            win_sound.stop()
        elif keys[pygame.K_e]:
            exec(open('python/menu.py').read())

            # Stop background music
            pygame.mixer.music.stop()
    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
