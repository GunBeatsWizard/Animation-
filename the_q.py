
#imports
import pygame
import math
import random
print("q brings the thing up on the screen")
print("w makes it move from right to left")
print("e screws with the background")
print("r makes it bounce")
print(" t y u and i all do things that i dont remember, enjoy")
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
LIGHT_BLUE = (230, 255, 255)
rainbow = [(255, 0, 0), (255, 125 , 0), (255, 255, 0), (0, 255, 0), (0, 153, 255), (0, 0, 255), (77, 0, 77)]

#Game loop
done = False
harvey_music = pygame.mixer.Sound("yeet.ogg")

##
the_q = False
wavy = False
bouncy = False
stars_color = False
screen_bounds_decision = False
##
ticks = 0
rainbow_index = 0

##
def display_message(x, y, text, size, color):
    my_font = pygame.font.Font(None, size)
    text_surface = my_font.render(text, True, color)
    screen.blit(text_surface, [x, y])

def draw_stars(C):
    stars = []
    for i in range(230):
        x = random.randrange(0, 1900)
        y = random.randrange(0, 1000)
        
        q = random.randrange(9, 15)
        s =  [x, y, q, q]
        stars.append(s)

    for s in stars:
        pygame.draw.ellipse(screen, C, s)

##
message_output = 'harvey you suck'
right_screen_bound = 1350
##
harvey_x = 700
harvey_y = 50 * math.sin(.02 * int(harvey_x) + 50) + 200
b_x = True
b_y = True
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                the_q =  not the_q
                harvey_music.play()
            if event.key == pygame.K_w:
                wavy = not wavy
                bouncy = False
            if event.key == pygame.K_r:
                bouncy = not bouncy
                wavy = False
                harvey_x = 1000
            if event.key == pygame.K_e:
                stars_color = not stars_color
            if event.key == pygame.K_t:
                message_output = 'harvey you suck'
                screen_bounds_decision = False
                right_screen_bound = 1350
            if event.key == pygame.K_y:
                message_output = 'look at all those chickens'
                screen_bounds_decision = False
                right_screen_bound = 1050
            if event.key == pygame.K_u:
                message_output = 'Have you ever had a dream? That you, um, you had, your, you, you could, youâ’ll do, you, you wants, you, you could do so, you , you’ll do, you could, you, you want, you want them, to do you so much, you could do anything?'
                screen_bounds_decision = True
            if event.key == pygame.K_i:
                message_output = 'i smell like beef'
                screen_bounds_decision = False
                right_screen_bound = 1385
    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 
     
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    '''  background  '''

    '''ticks'''
    ticks += 1 

    ''' drawing code '''
    #Color changing
    Q = rainbow[rainbow_index]

    if ticks % 4 == 0:
        rainbow_index += 1
        if rainbow_index > 6:
            rainbow_index = 0
        if ticks % 130 == 0:
            harvey_music.play()
            
    #stars code
    if stars_color:    
        E = Q
        R = Q
    elif not stars_color:
        E = WHITE
        R = LIGHT_BLUE
    draw_stars(E)
    draw_stars(R)

    #Q
    if screen_bounds_decision:
        screen_bounds = -8000
        bouncy = False
    else:
        screen_bounds = -500
    if not the_q:
        pygame.mixer.pause()
    
    if the_q:
        if wavy:
            harvey_x -= 4
            if harvey_x <= screen_bounds:
                harvey_x = 2000
            harvey_y = 50 * math.sin(.02 * int(harvey_x) + 50) + 200
        display_message(harvey_x, harvey_y, message_output, 100, Q)

        if bouncy:
            if b_x:
                harvey_x += 4
            else:
                harvey_x -= 4
            if harvey_x > right_screen_bound or harvey_x < 0:
                b_x = not b_x

            if b_y:
                harvey_y += 4
            else:
                harvey_y -= 4
            if harvey_y > 950 or harvey_y < 0:
                b_y = not b_y
    

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
