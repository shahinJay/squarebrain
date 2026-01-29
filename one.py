import pygame

pygame.init()

event = pygame.event.get()

running = True

pygame.display.set_mode((300,400))

while running:
    for event in pygame.event.get():
        
        if event == pygame.quit():
            
            running = False



pygame.quit()