# Imports
import pygame
import math
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (1900, 1000)
TITLE = "My Awesome Picture"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125 , 0)
FLAG_BLUE = (1, 18, 165)
rainbow = [(255, 0, 0), (255, 125 , 0), (255, 255, 0), (0, 255, 0), (0, 153, 255), (0, 0, 255), (77, 0, 77)]

#Game loop
done = False
harvey_music = pygame.mixer.Sound("yeet.ogg")

##
the_q = False
moving = False

##
ticks = 0
rainbow_index = 0

##

def draw_spikeybois(y):
    for x in range(5, 1900, 30):
        pygame.draw.polygon(screen, BLACK, [ [x+5, y], [x+10, y+5], [x+10, y+40],
                                             [x, y+40], [x, y+5]])
    pygame.draw.rect(screen, BLACK, [0, y+10, 1900, 7])
    pygame.draw.rect(screen, BLACK, [0, y+25, 1900, 7])


def draw_inverted_spikeybois(y):
    for x in range(5, 1900, 30):
        pygame.draw.polygon(screen, BLACK, [ [x, y], [x+10, y], [x+10, y+35],
                                             [x+5, y+40], [x, y+35]])
    pygame.draw.rect(screen, BLACK, [0, y+10, 1900, 7])
    pygame.draw.rect(screen, BLACK, [0, y+25, 1900, 7])

def display_message(x, y, text, size, color):
    my_font = pygame.font.Font(None, size)
    text_surface = my_font.render(text, True, color)
    screen.blit(text_surface, [x, y])


harvey_x = 700
harvey_y = 200
    
while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                the_q =  not the_q
                harvey_music.play()
            if event.key == pygame.K_w:
                moving = not moving


    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 
     
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    '''  background  '''
    screen.fill(RED)
    '''spikies'''
    draw_spikeybois(360)
    draw_inverted_spikeybois(600)
    ''' flag ''' 
    pygame.draw.rect(screen, WHITE, [0, 400, 1920, 200])
    pygame.draw.rect(screen, WHITE, [400, 0, 200, 1920])
    pygame.draw.rect(screen, FLAG_BLUE, [450, 0, 100, 1920])
    pygame.draw.rect(screen, FLAG_BLUE, [0, 450, 1920, 100])


    ''' q '''
    if not the_q:
        pygame.mixer.pause()
        
    if the_q == True:
        if moving == True:
            harvey_x += 4
            if harvey_x == 1900:
                harvey_x = -600
            harvey_y = 50 * math.sin(.02 * int(harvey_x) + 50) + 200
        Q = rainbow[rainbow_index]

        ticks += 1
        if ticks % 7 == 0:
            rainbow_index += 1

            if rainbow_index > 6:
                rainbow_index = 0
        if ticks % 130 == 0:
            harvey_music.play()


        display_message(harvey_x, harvey_y, 'harvey you suck', 100, Q)
                

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
