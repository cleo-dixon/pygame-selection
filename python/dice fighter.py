import pygame
import random 


pygame.init() 

# load and play music (Background music the rest are called throughout the game)

try: #exception handling if pygame mixer does not Initialize
    pygame.mixer.init()
except pygame.error as error:
    print("An error occurred while initializing Pygame mixer:",error)

background_sound=pygame.mixer.music.load('assests/audio/background music.wav')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
#(other game sounds that are called throughout the game )
dice_roll_music=pygame.mixer.Sound('assests/audio/Rolling Dice - Sound Effect (HD).mp3')
winner_music=pygame.mixer.Sound('assests/audio/You Win (Street Fighter) - Sound Effect.mp3')
game_start_music=pygame.mixer.Sound('assests/audio/Round 1, FIGHT!! - Sound Effect.mp3')


#screen size 
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Define the player class
class Player:
    def __init__(self, x, y):
        self.name= '' 
        self.rectangle = pygame.Rect((x, y, 50, 50))
        self.health = 100
        self.alive=True
    # Draw the player rectangle and health bar on the screen
    def show(self, surface):
       
        pygame.draw.rect(surface, (255, 255, 255), self.rectangle)
        pygame.draw.rect(surface, (255, 0, 0), (self.rectangle.x, self.rectangle.y - 10, self.health * 0.8 ,10))
        
        screen.blit(background_img.subsurface(self.rectangle),self.rectangle)
     # Draw the player name above the player
        text_surface = font.render(self.name, True, (0, 255, 205))
        surface.blit (text_surface, (self.rectangle.x + 5, self.rectangle.y - 40))
        
     # Reduce player health by the damage amount  
    def damage(self, damage):
        self.health -= damage
        if self.health<=0:
            self.alive=False 
            
                                   
# functions for dice roll and animation 
def dice():
    return random.randint(1, 6)

def dice_roll_dis (dice_roll):
    diceimage=dice_images[dice_roll-1]
    screen.blit(diceimage,(10,20))
    

#dice images list 
dice_images=[
    pygame.image.load('assests/images/1.png'),
    pygame.image.load('assests/images/2.png'),
    pygame.image.load('assests/images/3.png'),
    pygame.image.load('assests/images/4.png'),
    pygame.image.load('assests/images/5.png'),
    pygame.image.load('assests/images/6.png'),   
]


# prompt the user to enter their names 
player1 = Player(200, 320)
player1.name = input('Enter Player 1 name: ')
player2 = Player(390, 320)
player2.name = input('Enter Player 2 name: ')



#  Pygame window and game name
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Dice Fighter')

# game logo
logo = pygame.image.load('assests/images/001-fight.png')
pygame.display.set_icon(logo)

# Load the background image and create the background surface
background_img = pygame.image.load('assests/images/background.jpg')
updated_bg = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

# function to display the background image
def display_bg():
    screen.blit(updated_bg, (0, 0))

# Create  font objects
font = pygame.font.Font('assests/fonts/California Paradise.otf', 25)
font2=pygame.font.Font('assests/fonts/game over Italic.ttf',20)
#load animation image sheets
idle_sheet = pygame.image.load ('assests/images/Idle.png').convert_alpha ()
idle_sheet2=pygame.image.load('assests/images/Idle2.png').convert_alpha ()
attack_sheet = pygame.image.load('assests/images/Attack.png').convert_alpha()
attack_sheet2 = pygame.image.load('assests/images/Attack2.png').convert_alpha()
#player 1 idle animation 
num_frames = 8
num_frames2 = 8
frame_width = idle_sheet.get_width() // num_frames
frame_height = idle_sheet.get_height()
#player 2 idle animation
frame_width2 = idle_sheet2.get_width() // num_frames2
frame_height2 = idle_sheet2.get_height()
# Player 1 attack animation
num_attack_frames = 5
attack_frame_width = attack_sheet.get_width() // num_attack_frames
attack_frame_height = attack_sheet.get_height()
# Player 2 attack animation
num_attack_frames2 = 8
attack_frame_width2 = attack_sheet2.get_width() // num_attack_frames2
attack_frame_height2 = attack_sheet2.get_height()

# Create a list to hold the individual frames
idle_frames = []
idle_frames2 = []
attack_frames = []
attack_frames2 = []

#  Extract player images from the frames from the sprite sheet
for i in range(num_frames):
    frame = pygame.Surface((frame_width, frame_height), pygame.SRCALPHA)
    frame.blit(idle_sheet, (0, 0), (i * frame_width, 0, frame_width, frame_height))
    scaled_frame1 = pygame.transform.scale(frame, (frame_width * 4, frame_height * 4))
    idle_frames.append(scaled_frame1)
    
for i in range(num_frames2):
    frame2 = pygame.Surface((frame_width2, frame_height2), pygame.SRCALPHA)
    frame2.blit(idle_sheet2, (0, 0), (i * frame_width2, 0, frame_width2, frame_height2))
    scaled_frame2 = pygame.transform.scale(frame2, (frame_width2 * 4, frame_height2 * 4))
    idle_frames2.append(scaled_frame2)

for i in range(num_attack_frames):
    frame = pygame.Surface((attack_frame_width, attack_frame_height), pygame.SRCALPHA)
    frame.blit(attack_sheet, (0, 0), (i * attack_frame_width, 0, attack_frame_width, attack_frame_height))
    scaled_frame3 = pygame.transform.scale(frame, (attack_frame_width * 4, attack_frame_height * 4))
    attack_frames.append(scaled_frame3)

for i in range(num_attack_frames2):
    frame2 = pygame.Surface((attack_frame_width2, attack_frame_height2), pygame.SRCALPHA)
    frame2.blit(attack_sheet2, (0, 0), (i * attack_frame_width2, 0, attack_frame_width2, attack_frame_height2))
    scaled_frame4 = pygame.transform.scale(frame2, (attack_frame_width2 * 4, attack_frame_height2 * 4))
    attack_frames2.append(scaled_frame4)


# Set the current frame and frame counter
current_frame = 0
frame_counter = 0
current_attack_frame = 0
attack_frame_counter = 0
dice_rect = pygame.Rect(10, 20, 100, 100)  # Create a rectangle for the dice surface
dice_roll = 0  # Initialize dice_roll to 0
dice_surface = dice_images[dice_roll - 1]

# indicate if an attack is in progress
attacking = False

clock = pygame.time.Clock() # add the clock function to time certain actions 
animation_speed = 10
turn = 1
dice_roll = 0
winner=None
winner_data=[]
# Game loop 
running = True
while running:
    display_bg()
    player1.show(screen)
    player2.show(screen)
    
    frame_counter += 1

    # Update the current frame if it's time to do so
    if frame_counter >= animation_speed:
        current_frame = (current_frame + 1) % num_frames
        frame_counter = 0

    # Draw the current frame on the screen
    screen.blit(idle_frames[current_frame], (-50,125 ))
    screen.blit(pygame.transform.flip(idle_frames2[current_frame], True, False), (110, 125))
    
    
    if not attacking and frame_counter >= animation_speed:
        current_frame = (current_frame + 1) % num_frames
        frame_counter = 0

    # Draw the current frame on the screen
    if attacking:
        if turn == 1:
            screen.blit(attack_frames[current_attack_frame], (-50,125 ))
            screen.blit(pygame.transform.flip(idle_frames2[current_frame], True, False), (110, 125))
        else:
            screen.blit(idle_frames[current_frame], (-50,125 ))
            screen.blit(pygame.transform.flip(attack_frames2[current_attack_frame], True, False), (110, 125))
        
        # Update the current frame of the attack animation if it's time to do so
        if attack_frame_counter >= animation_speed:
            current_attack_frame += 1
            if turn == 1 and current_attack_frame >= num_attack_frames:
                attacking = False
                current_attack_frame = 0
            elif turn == 2 and current_attack_frame >= num_attack_frames2:
                attacking = False
                current_attack_frame = 0
            attack_frame_counter = 0
        else:
            attack_frame_counter += 1
    else:
        screen.blit(idle_frames[current_frame], (-50,125 ))
        screen.blit(pygame.transform.flip(idle_frames2[current_frame], True,False), (110,125))

    # Display player names
    text_surface = font.render(f"{player1.name} vs {player2.name}", True, (255, 0, 50))
    screen.blit(text_surface, (SCREEN_WIDTH // 2 - 60, 20))
    # if statement to determine whose turn it is 
    if turn == 1:
         current_player = player1.name
    else:
        current_player = player2.name
    text_surface = font.render(current_player+"'s turn", True, (255, 0, 50)) # render player names on screen
    screen.blit(text_surface, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50))

    screen.blit(dice_surface, dice_rect) #display dice animation on screen 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            #dice roll and damage code 
            if event.key == pygame.K_SPACE: #press space bar to roll dice  
                if player1.alive and player2.alive:
                    dice_roll = dice()
                    #music for dice roll
                    
                    dice_roll_music.play () 
                      
                    dice_surface = dice_images[dice_roll - 1]
                    attacking = True
                    if turn == 1:
                        player2.damage(dice_roll*10)
                        turn = 2
                    else:
                        player1.damage(dice_roll*10)
                        turn = 1
                else:
                    if player1.alive:
                        winner = player1.name
                        winner_data.append((player1.name, player1.health))
                        
                    else:
                        winner = player2.name
                        winner_data.append((player2.name, player2.health))
                        
                    winner_music.play () #winner of the game sound 
                    text_surface = font2.render('Congratulations '  +  winner  +  ' you are the victor', True, (0, 0, 0))
                    screen.blit(text_surface, (SCREEN_WIDTH // 2 - 220, SCREEN_HEIGHT // 2-150))
                    pygame.display.update()
                    pygame.time.wait(2000)

                    text_surface = font2.render('Press R to restart or Q to quit', True, (0, 0, 0))
                    screen.blit(text_surface, (SCREEN_WIDTH // 2 - 220, SCREEN_HEIGHT // 2 - 100))
                    pygame.display.update()
                    #reseting the game code 
                    waiting = True
                    while waiting:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running = False
                                waiting = False
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_r:
                                    # Restart the game
                                    player1.health = 100
                                    player2.health = 100
                                    player1.alive = True
                                    player2.alive = True
                                    turn = 1
                                    dice_roll = 0
                                    winner = None
                                    winner_data = []
                                    waiting = False
                                elif event.key == pygame.K_q:
                                    # Quit the game
                                    running = False
                                    waiting = False
            elif event.key == pygame.K_r:
                # Restart the game
                player1.health = 100
                player2.health = 100
                player1.alive = True
                player2.alive = True
                turn = 1
                dice_roll = 0
                winner = None
                winner_data = []
            elif event.key == pygame.K_q:
                # Quit the game
                running = False
            elif event.key == pygame.K_e:
                exec(open('python/menu.py').read())
    clock.tick(80) #sets frame rate to 80 frames per second 
    
 
    pygame.display.update() #keep refresing screen to see changes 

pygame.quit() #stop pygame from running 


















































                