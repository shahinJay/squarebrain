import pygame

pygame.init()

running = True


pygame.display.set_mode((300,300))


while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  

pygame.quit()

