import pygame
from grid import grid

pygame.init()

running = True

disp_x = 600
disp_y = 600

screen = pygame.display.set_mode((disp_x, disp_y))

new_grid = grid(screen, disp_x, disp_y)

new_grid.draw_grid()

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  pygame.display.flip()
  

pygame.quit()

