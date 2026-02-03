import pygame

class grid:
  def __init__(self, screen, disp_x, disp_y):
    self.disp_x = disp_x
    self.disp_y = disp_y
    self.screen = screen

  def draw_grid(self, cell_size = 25, grid_color = (255, 255, 255), grid_line_size = 1):
    for x in range(self.disp_x):
      if x%cell_size == 0:
        
        pygame.draw.line(self.screen, grid_color, (x, 0), (x, self.disp_y), grid_line_size)
    
    for y in range(self.disp_y):
      if y%cell_size == 0:

        pygame.draw.line(self.screen, grid_color, (0, y), (self.disp_x, y), grid_line_size)



    