import pygame
import random
import sys
import time

WIDTH = 1200
HEIGHT = 1000
FPS = 60

# game constants
player_vel = 20
player_width = 150
player_health = 20
asteroid_width = 100
asteroid_kill_count = 0
scrolling_speed = 5
asteroids = []  # starts out empty and asteroid objects are appended to the list
big_asteroids = []
big_asteroid_health = 5
laser_width = 50
laser_height = 80
laser_vel = 20
enemy_laser_width = 10
enemy_laser_height = 70
laser_delay = 10
aliens = []
lasers = []
laser_count = 0
alien_width = 200
alien_health = 5
alien_vel = 4
boss_width = 700
boss_height = 250
bosses = []
boss_vel = 3
boss_health = 50
boss_spawned = False
boss_death_count = 0

count = 0
alien_frame_count = 0

# defining colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# loading sprites
background = pygame.transform.scale(pygame.image.load('assests/images/space_background.gif'),
                                    (WIDTH, HEIGHT))  # loads and scales image to window size
player = pygame.transform.scale(pygame.image.load('assests/images/spaceship.png'), (player_width, player_width))
asteroid = pygame.transform.scale(pygame.image.load('assests/images/asteroid.png'), (asteroid_width, asteroid_width))
big_asteroid = pygame.transform.scale(pygame.image.load('assests/images/asteroid.png'), (asteroid_width * 2, asteroid_width * 2))
laser = pygame.transform.scale(pygame.image.load('assests/images/bullet.png'), (laser_width, laser_height))

alien_1 = pygame.transform.scale(pygame.image.load('assests/images/alien.png'), (alien_width, alien_width))
alien_2 = pygame.transform.scale(pygame.image.load('assests/images/alien_2.png'), (alien_width, alien_width))
alien_sprites = [alien_1, alien_2]

boss_image = pygame.transform.scale(pygame.image.load('assests/images/alien_boss.png'), (boss_width, boss_height))

# initialize pygame and create window
pygame.mixer.pre_init(44100, -16, 1, 512)  # prevents sound delay
pygame.init()
my_font = pygame.font.SysFont("assests/fonts/Space Crusaders Italic.ttf", 64)  # this needs to be after pygame.init()
game_over_font = pygame.font.SysFont("assests/fonts/Space Crusaders Italic.ttf", 120, bold=True)  # game over font
win_font = pygame.font.SysFont('cambrian', 120, bold=True)
# pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Space Strikers")
icon = pygame.image.load('assests/images/galaxy.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()


class Background1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = background
        self.rect = self.image.get_rect()  # figures out rectangle based on image
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        if self.rect.y > HEIGHT:
            self.rect.y = -HEIGHT
        else:
            self.rect.y += scrolling_speed


class Background2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = background
        self.rect = self.image.get_rect()  # figures out rectangle based on image
        self.rect.center = (WIDTH / 2, -HEIGHT / 2)

    def update(self):
        if self.rect.y > HEIGHT:
            self.rect.y = -HEIGHT
        else:
            self.rect.y += scrolling_speed


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player
        self.rect = self.image.get_rect()  # figures out rectangle based on image
        self.rect.center = (WIDTH / 2, HEIGHT / 1.1)

    def update(self):
        global player_health, count, laser_delay, counts
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.x < WIDTH - player_width:
            self.rect.x += player_vel
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= player_vel

        # try:
        #    if keys[pygame.K_UP] and self.rect.x > 0:
        #        self.rect.x -= player_vel
        # except:
        #   print("Up is not a direction u can go. Only Left or Right")

        count += 1  # adds a delay to the lasers (for holding down the button)
        if keys[pygame.K_SPACE] and count % laser_delay == 0:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('assests/audio/laser_sound.wav'))
            all_sprites.add(Laser())  # space bar adds a laser sprite every time it is pressed

        # when an asteroid hits the player
        for asteroid in asteroids:
            if pygame.sprite.collide_rect(self, asteroid):
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('assests/audio/space_ship_hit.wav'))
                asteroids.remove(asteroid)
                all_sprites.remove(asteroid)
                player_health -= 1

        for asteroid in big_asteroids:
            if pygame.sprite.collide_rect(self, asteroid):
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('assests/audio/space_ship_hit.wav'))
                big_asteroids.remove(asteroid)
                all_sprites.remove(asteroid)
                player_health -= 1
        for laser in lasers:
            if pygame.sprite.collide_rect(self, laser):
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('assests/audio/space_ship_hit.wav'))
                lasers.remove(laser)
                all_sprites.remove(laser)
                player_health -= 1


class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = asteroid
        self.rect = self.image.get_rect()  # figures out rectangle hitbox based on image
        self.rect.center = (random.randrange(0, WIDTH - asteroid_width), 0)
        self.asteroid_vel = [random.randrange(-1, 2), random.randrange(2, 12)]

    def update(self):  # asteroid movement (asteroids disappear when the hit the edge of the screen)
        self.rect.y += self.asteroid_vel[1]
        self.rect.x += self.asteroid_vel[0]
        if self.rect.y > HEIGHT:
            asteroids.remove(self)
            all_sprites.remove(self)


class BigAsteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = big_asteroid
        self.rect = self.image.get_rect()  # figures out rectangle hitbox based on image
        self.rect.center = (random.randrange(0, WIDTH - asteroid_width), 0)
        self.asteroid_vel = [random.randrange(-1, 2), random.randrange(2, 12)]
        self.big_asteroid_health = big_asteroid_health

    def update(self):  # asteroid movement (asteroids disappear when the hit the edge of the screen)
        self.rect.y += self.asteroid_vel[1]
        self.rect.x += self.asteroid_vel[0]
        if self.rect.y > HEIGHT:
            big_asteroids.remove(self)
            all_sprites.remove(self)


class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = boss_image
        self.rect = self.image.get_rect()  # figures out rectangle hitbox based on image
        self.rect.center = (WIDTH / 2, -boss_height / 2)
        self.boss_health = boss_health

    def update(self):
        global boss_vel
        if self.rect.y < HEIGHT / 20:
            self.rect.y += boss_vel
        else:
            self.rect.x += boss_vel
            if self.rect.x + boss_width > WIDTH:
                boss_vel *= -1
            elif self.rect.x < 0:
                boss_vel *= -1


# adds an asteroid at a random location to all_sprites and appends it to the list asteroids if the asteroid list is less than 10
def add_asteroid():
    if random.random() < 0.1 and len(asteroids) < 8:
        asteroids.append(Asteroid())
        for asteroid in asteroids:
            all_sprites.add(asteroid)


def add_big_asteroid():
    if random.random() < 0.05 and len(big_asteroids) < 3:
        big_asteroids.append(BigAsteroid())
        for asteroid in big_asteroids:
            all_sprites.add(asteroid)


def add_alien():
    if random.random() < 0.01 and len(aliens) < 1:
        aliens.append(Alien())
        for alien in aliens:
            all_sprites.add(alien)


def add_boss():
    global boss_spawned
    if len(bosses) < 1 and random.random() < 0.005:
        bosses.append(Boss())
        boss_spawned = True
        for boss in bosses:
            all_sprites.add(boss)


def add_laser():
    global laser_count
    laser_count += 1
    if len(lasers) < 10 and laser_count + 1 >= 60:
        laser_count = 0
        lasers.append(EnemyLaser())
        for laser in lasers:
            all_sprites.add(laser)


def draw_text():
    health = str(player_health)
    killed = str(asteroid_kill_count)
    health_label = my_font.render('Health: ' + health, 1, WHITE)
    screen.blit(health_label, (0, 0))
    killed_label = my_font.render('Points: ' + killed, 1, WHITE)
    screen.blit(killed_label, (0, HEIGHT / 18))


class Laser(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = laser
        self.rect = self.image.get_rect()  # figures out rectangle hitbox based on image
        self.rect.center = player.rect.center

    def update(self):
        global asteroid_kill_count
        self.rect.y -= laser_vel

        # if a laser collides with an asteroid, the asteroid and laser disappear
        for asteroid in asteroids:
            if pygame.sprite.collide_rect(self, asteroid):
                pygame.mixer.Channel(2).play(pygame.mixer.Sound('assests/audio/asteroid_explosion.wav'))
                asteroids.remove(asteroid)
                all_sprites.remove(asteroid)
                all_sprites.remove(self)  # removes laser after it hits the asteroid
                asteroid_kill_count += 1

        for asteroid in big_asteroids:  # big asteroids take more than one hit
            if pygame.sprite.collide_rect(self, asteroid):
                asteroid.big_asteroid_health -= 1
                all_sprites.remove(self)  # removes laser after it hits the asteroid
                if asteroid.big_asteroid_health < 1:
                    pygame.mixer.Channel(2).play(pygame.mixer.Sound('assests/audio/asteroid_explosion.wav'))
                    big_asteroids.remove(asteroid)
                    all_sprites.remove(asteroid)
                    asteroid_kill_count += 3
                else:
                    pygame.mixer.Channel(4).play(pygame.mixer.Sound('assests/audio/big_asteroid_hit.wav'))

        for alien in aliens:  # aliens take more than one hit
            if pygame.sprite.collide_rect(self, alien):
                alien.alien_health -= 1
                all_sprites.remove(self)  # removes laser after it hits the alien
                if alien.alien_health < 1:
                    pygame.mixer.Channel(5).play(pygame.mixer.Sound('assests/audio/alien_killed.wav'))
                    aliens.remove(alien)
                    all_sprites.remove(alien)
                    asteroid_kill_count += 10
                else:
                    pygame.mixer.Channel(5).play(pygame.mixer.Sound('assests/audio/alien_hit.wav'))

        for boss in bosses:  # aliens take more than one hit
            if pygame.sprite.collide_rect(self, boss):
                boss.boss_health -= 1
                all_sprites.remove(self)  # removes laser after it hits the alien
                if boss.boss_health < 1:
                    pygame.mixer.Channel(6).play(pygame.mixer.Sound('assests/audio/boss_death.wav'))
                    bosses.remove(boss)
                    all_sprites.remove(boss)
                    asteroid_kill_count += 1000
                else:
                    pygame.mixer.Channel(6).play(pygame.mixer.Sound('assests/audio/boss_hit.wav'))

        if self.rect.y < 0:
            all_sprites.remove(self)


class EnemyLaser(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # required
        self.image = pygame.Surface((enemy_laser_width, enemy_laser_height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()  # figures out rectangle based on image
        if len(aliens) > 0:
            self.rect.center = aliens[0].rect.center

    def update(self):
        self.rect.y += laser_vel

        if self.rect.y > HEIGHT:
            lasers.remove(self)
            all_sprites.remove(self)


class Alien(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = alien_sprites[0]
        self.rect = self.image.get_rect()  # figures out rectangle hitbox based on image
        if random.random() < 0.5:
            self.rect.center = (0, HEIGHT / 4)
            self.alien_vel = alien_vel
        else:
            self.rect.center = (WIDTH, HEIGHT / 4)
            self.alien_vel = alien_vel * -1
        self.alien_health = alien_health

    def update(self):  # asteroid movement (asteroids disappear when the hit the edge of the screen)
        global alien_frame_count
        self.rect.x += self.alien_vel
        if self.rect.x > WIDTH or self.rect.x < -alien_width:
            aliens.remove(self)
            all_sprites.remove(self)

        # makes alien image animated
        alien_frame_count += 1
        if alien_frame_count + 1 >= 60:
            alien_frame_count = 0
        self.image = alien_sprites[alien_frame_count // 30]


title_font = pygame.font.SysFont("Times New Roman", 100, bold=True)


def title_screen():
    intro = True
    while intro:
        screen.fill(WHITE)
        text1 = 'Welcome to Space Strikers'
        text2 = "Press Enter to Start!"
        label1 = title_font.render(text1, 1, BLACK)
        label2 = title_font.render(text2, 1, BLACK)
        screen.blit(label1, (WIDTH / 25, HEIGHT / 3))
        screen.blit(label2, (WIDTH / 6, HEIGHT / 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            intro = False
        if keys[pygame.K_e]:
            exec(open('python/menu.py').read())

        pygame.display.update()


title_screen()


def win():
    global boss_death_count
    keys = pygame.key.get_pressed()

    boss_death_count += 1
    if boss_death_count + 1 >= 150:
        boss_death_count = 0

        win = True
        pygame.mixer.music.stop()
        pygame.mixer.Channel(7).play(pygame.mixer.Sound('assests/audio/Mega Man X (SNES) - Stage Clear Theme .mp3'))
        while win:
            if keys[pygame.K_e]:
                exec(open('python/menu.py').read())
            screen.fill(WHITE)
            label = win_font.render('YOU WON! ;)', 1, BLACK)
            score_label = win_font.render('Your Score: ' + str(asteroid_kill_count), 1, BLACK)
            screen.blit(label, (WIDTH / 2.9, HEIGHT / 4))
            screen.blit(score_label, (WIDTH / 4, HEIGHT / 2.5))
            screen.blit(pygame.transform.scale(pygame.image.load('assests/images/spaceship.png'), (300, 300)),
                        (WIDTH / 2 - 150, HEIGHT / 2))
            

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


def game_over():
    global player_health, boss_health, asteroid_kill_count, song
    keys = pygame.key.get_pressed()
    game_over = True
    pygame.mixer.music.stop()
    pygame.mixer.Channel(3).play(pygame.mixer.Sound('assests/audio/game_over.wav'))
    while game_over:
        screen.fill(WHITE)
        label = game_over_font.render('GAME OVER :(', 1, BLACK)
        screen.blit(label, (WIDTH / 3.7, HEIGHT / 4))
        score_label = game_over_font.render('Your Score: ' + str(asteroid_kill_count), 1, BLACK)
        screen.blit(score_label, (WIDTH / 4, HEIGHT / 3))
        screen.blit(pygame.transform.scale(pygame.image.load('assests/images/alien_boss.png'), (600, 300)),
                    (WIDTH / 2 - 300, HEIGHT / 2))
        restart_label = game_over_font.render('Press R to restart', 1, BLACK)
        screen.blit(restart_label, (WIDTH / 5, HEIGHT / 2.5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            game_over = False
            song = pygame.mixer.music.load('assests/audio/tomp3.cc - StarTropics Music  Cave.mp3')
            pygame.mixer.music.play(-1)
            player_health = 20
            asteroid_kill_count = 0
            boss_health = 50
        if keys[pygame.K_e]:
            exec(open('python/menu.py').read())

        pygame.display.update()


# play music for pygame:

song = pygame.mixer.music.load('assests/audio/tomp3.cc - StarTropics Music  Cave.mp3')
pygame.mixer.music.play(-1)

all_sprites = pygame.sprite.Group()
all_sprites.add(Background1())
all_sprites.add(Background2())
player = Player()
all_sprites.add(player)


# Game Loop
def main():
    global bosses, game_state
    running = True
    while running:
        # keeps loop running at the right speed
        clock.tick(FPS)
        # process input (events)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:  # this is for if you want to spam the space bar
                if event.key == pygame.K_SPACE:
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound('assests/audio/laser_sound.wav'))
                    all_sprites.add(Laser())
                if event.key == pygame.K_e:
                    exec(open('python/menu.py').read())

            keys = pygame.key.get_pressed()
        # Update
        all_sprites.update()
        add_asteroid()

        if asteroid_kill_count > 5:  # 49
            add_big_asteroid()

        if asteroid_kill_count > 20:  # 99
            add_alien()
            if len(aliens) > 0:
                add_laser()

        if asteroid_kill_count > 30 and not boss_spawned:  # 179
            add_boss()
            if len(bosses) > 0:
                pass  # add lasers here if you want the boss to shoot lasers

        if boss_spawned and len(bosses) < 1:
            win()

        if player_health < 1:
            game_over()

        # Draw / render
        all_sprites.draw(screen)
        draw_text()
        pygame.display.update()


    pygame.quit()


main()
