import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 600))
done = False
is_blue = True
x = 30
y = 30

speed = 40

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True                
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= speed
        if pressed[pygame.K_DOWN]: y += speed
        if pressed[pygame.K_LEFT]: x -= speed
        if pressed[pygame.K_RIGHT]: x += speed     

        if x < 0: x = 0
        if y < 0: y = 0
        if x > 1140: x = 1140        
        if y > 540: y = 540

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x, y, 60, 60))
        
        pygame.display.flip()
        clock.tick(60)