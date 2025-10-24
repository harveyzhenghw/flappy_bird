# INITIALIZE PYGAME
# # Import the pygame module
import pygame,sys
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
    new_pipe = pipe_surface.get_rect(midtop = (300, 512))
    return new_pipe
#variables
gravity = 0.1
bird_movement = 0

def move_pipes(pipe_list):
    for pipe in pipe_list:
        pipe.centerx -= 5
        pass
    return pipe_list

def draw_pipes(pipe_list):
    for pipe in pipe_list:
        screen_surface.blit(pipe_surface, pipe)
        pass

bg_surface = pygame.image.load("./assests/sprites/background-day.png")
bg_surface = pygame.transform.scale2x(bg_surface)


#floor
floor = pygame.image.load("./assests/sprites/base.png")
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0
#bird
bird_surface = pygame.image.load("./assests/sprites/redbird-midflap.png")
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (200,200))
#pipe
pipe_surface = pygame.image.load("./assests/sprites/pipe-green.png")
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
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
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 5
                pass
            pass
        if event.type == SPAWN_PIPE:
            pipe_list.append(create_pipe())
            print(pipe_list)
        pass
    #screen
    screen_surface.blit(bg_surface, (0, 0))
    #bird
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen_surface.blit(bird_surface,bird_rect)

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
