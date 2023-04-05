import pygame
import sys

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

jump_sound = pygame.mixer.Sound("jump_sound.wav")
hit_sound = pygame.mixer.Sound("hit_sound.wav")

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
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

            else:
                # Update the player position and display the turn instruction
                roll1 = random.randint(1,6)
                roll2 = random.randint(1,6) 

                sumpos = roll1 + roll2
                total = (total + sumpos) % 42

                font = pygame.font.Font('assests/fonts/April Easter.ttf', 26)
                turn_instruction = font.render(player_name[current_player] + "'s turn", True, (255, 255, 255))
                turn_rect = turn_instruction.get_rect()
                turn_rect.center = (int(windoww // 2.6), int(windowh - 170))

                # Clear the area where the turn instruction is displayed
                screen.blit(instruct, (int(windoww // 2.6) - 860 // 2, int(windowh - 204.5), 860, turn_rect.height))

                # Blit the new text
                screen.blit(turn_instruction, turn_rect)

                player_positions[current_player] = (player_positions[current_player] + sumpos) % 42

                # Blit the player image onto the board and remove the previous one
                screen.blit(player1, positions1[player_positions[0]])
                screen.blit(player2, positions2[player_positions[1]])
                screen.blit(player3, positions3[player_positions[2]])

                screen.blit(board1, board_rect.topleft + board1_pos)
                screen.blit(board2, board_rect.topleft + board2_pos)
                screen.blit(board3, board_rect.topleft + board3_pos)
                screen.blit(board4, board4_pos)
                screen.blit(text_surface, text_rect)

                # Roll the dice and display the dice images
                dice1 = pygame.image.load(dice_images[roll1])
                dice1 = pygame.transform.scale(dice1, (100,100))
                screen.blit(dice1, (x1,y1))

                dice2 = pygame.image.load(dice
    pygame.mixer.music.stop()
    pygame.quit()
    sys.exit()
