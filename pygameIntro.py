import pygame
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((300, 250, 50, 50))

run = True
while run:

    screen.fill((0,0,0)) #fills screen with color black to prevent the red block from leaving a trail on the screen when moved
    pygame.draw.rect(screen, (255, 0, 0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a]:    #check if key pressed is "a"
        player.move_ip(-1, 0)     #move in place -1 right, 0 vertical
    elif key[pygame.K_d]:
        player.move_ip(1, 0)
    elif key[pygame.K_w]:
        player.move_ip(0, -1)
    elif key[pygame.K_s]:
        player.move_ip(0, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()