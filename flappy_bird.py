# INITIALIZE PYGAME
# # Import the pygame module
import pygame,sys, random
# Initialize module
pygame.init()
pygame.display.set_caption("Flappy Bird by Harvey")

# DISPLAY SURFACE
# (has width and height)
SCREEN_WIDTH = 576
SCREEN_HEIGHT = 1024
screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

#functions
def draw_floor():
    screen_surface.blit(floor, (floor_x_pos,850))
    screen_surface.blit(floor, (floor_x_pos + 576,850))
    pass


def create_pipe():
    random_pipe_position = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (700, random_pipe_position))
    top_pipe = pipe_surface.get_rect(midbottom = (700, random_pipe_position-250))
    return bottom_pipe, top_pipe


def move_pipes(pipe_list):
    for pipe in pipe_list:
        pipe.centerx -= 5
        pass
    return pipe_list

def draw_pipes(pipe_list):
    for pipe in pipe_list:
        
        if pipe.bottom >= 900:
            screen_surface.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen_surface.blit(flip_pipe, pipe)
def check_collision(pipe_list):
    for pipe in pipe_list:
        if bird_rect.colliderect(pipe):
            print("game over")
            return False
    if bird_rect.top <= -50 or bird_rect.top >=850:
        print("game over")
        return False
    return True

def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird,-bird_movement*5, 1)
    return new_bird

def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center = (120, bird_rect.centery))
    return new_bird, new_bird_rect
#variables
gravity = 0.15
bird_movement = 0
game_active = True

bg_surface = pygame.image.load("./assests/sprites/background-day.png")
bg_surface = pygame.transform.scale2x(bg_surface)


#floor
floor = pygame.image.load("./assests/sprites/base.png")
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0
#bird
'''bird_surface = pygame.image.load("./assests/sprites/redbird-midflap.png")
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (200,200))'''
bird_down_flap = pygame.transform.scale2x(pygame.image.load("./assests/sprites/redbird-downflap.png").convert_alpha())

bird_mid_flap = pygame.transform.scale2x(pygame.image.load("./assests/sprites/redbird-midflap.png").convert_alpha())

bird_up_flap = pygame.transform.scale2x(pygame.image.load("./assests/sprites/redbird-upflap.png").convert_alpha())

bird_frames = [bird_down_flap,bird_mid_flap,bird_up_flap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center = (120,200))

BIRDFLAP = pygame.USEREVENT+1
pygame.time.set_timer(BIRDFLAP,200)



#pipe

pipe_surface = pygame.image.load("./assests/sprites/pipe-green.png")
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
pipe_height = [300,500,700]
SPAWN_PIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWN_PIPE, 1500)
# GAME LOOP
# (has methods to draw)
# (checks for user input)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
            pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active == True:
                bird_movement = 0
                bird_movement -= 5      
                pass
            pass

            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True

                pipe_list.clear()
                bird_rect.center = (120,200)
                bird_movement = 0   

        if event.type == BIRDFLAP:
            if bird_index <2:
                bird_index += 1
            else:
                bird_index = 0

            bird_surface, bird_rect = bird_animation()
        
        
                
        if event.type == SPAWN_PIPE:
            pipe_list.extend(create_pipe())
            print(pipe_list)
        pass
    #screen
    screen_surface.blit(bg_surface, (0, 0))
    if game_active:
        #bird
        bird_movement += gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += bird_movement
        screen_surface.blit(rotated_bird,bird_rect)
        game_active = check_collision(pipe_list)
        #pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
    
    #floor
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -576:
        floor_x_pos = 0

    

    pygame.display.update()
    clock.tick(120)



# QUIT PYGAME
