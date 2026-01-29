import pygame

pygame.init()

running = True

disp_x = 600
disp_y = 600



screen = pygame.display.set_mode((disp_x, disp_y))


grid_line_size = 1
grid_color = (255, 255, 255)
grid_size = 25

def draw_grid():
  
  for x in range(disp_x):
    if x%grid_size == 0:
      pygame.draw.line(screen, grid_color, (x, 0), (x, disp_y), grid_line_size)
  
  for y in range(disp_y):
    if y%grid_size == 0:
      pygame.draw.line(screen, grid_color, (0, y), (disp_x, y), grid_line_size)



draw_grid()


while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  pygame.display.flip()
  

pygame.quit()

