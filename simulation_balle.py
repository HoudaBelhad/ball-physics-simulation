import pygame
import sys

pygame.init()

# window setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulation Physique Balle")

clock = pygame.time.Clock()  # pour contrôler les FPS
 # ball position (x, y) and speed (vX, vY)
x = 50.0
y = 50.0

vX = 5.0
vY = 0.0

G = 0.4        # the ball fall down with this gravity by 0.4 pixels per frame
REBOND = 0.75  # when the ball touches the ground it bounces back with 75% of its speed (loses some energy)
DIAMETRE = 30
RAYON = DIAMETRE // 2

# colors
WHITE = (255, 255, 255)
BLUE = (41, 128, 185)

# core simulation loop
running = True
while running:
    clock.tick(60)  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # when the ball falls down by increasing its vertical speed (vY) due to gravity (G)
    vY += G

    # it moves the ball by adding its speed to its position (x and y)
    x += vX
    y += vY

    # ground collision 
    if y + DIAMETRE > HEIGHT:
        y = HEIGHT - DIAMETRE
        vY = -vY * REBOND
        vX *= 0.98  

    # wall collision
    if x < 0:
        x = 0
        vX = -vX * REBOND
    elif x + DIAMETRE > WIDTH:
        x = WIDTH - DIAMETRE
        vX = -vX * REBOND

    # draw everything
    screen.fill(WHITE)
    pygame.draw.circle(
        screen,
        BLUE,
        (int(x + RAYON), int(y + RAYON)),
        RAYON
    )

    pygame.display.flip()
pygame.quit()
sys.exit()
