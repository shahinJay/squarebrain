import pygame
import random as rd

pygame.init()
running = True
cell_size = 64
cell_count=8
size=cell_size*cell_count #screen Size
screen = pygame.display.set_mode((size, size))


def randPosition():
   return int(64 * rd.randrange(8))

x=randPosition()
y=randPosition()


grid_line_size = 1
grid_color = (255, 255, 255)

def draw_grid():
    
    for x in range(size):
      if x%cell_size == 0:
        pygame.draw.line(screen, grid_color, (x, 0), (x, size), grid_line_size)
    
    for y in range(size):
      if y%cell_size == 0:
        pygame.draw.line(screen, grid_color, (0, y), (size, y), grid_line_size)

def nextPosition(move, currentX, currentY):
  if move == "right":
    currentX += cell_size
  elif move == "left":
    currentX -= cell_size
  elif move == "up":
    currentY += cell_size
  elif move == "down":
    currentY -= cell_size
  return currentX, currentY

#main function of loop
while running:
  screen.fill((0, 0, 0))
  draw_grid()
  red = (255,0,0)
  green = (0,255,0)
  blue = (0,0,255)
     
  pygame.draw.rect(screen, red, (384,256,64,64))
  pygame.draw.rect(screen, green, (x,y, 64, 64))
  
  pygame.display.flip()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

    move = "None"
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_d:
          move = "right"
      if event.key == pygame.K_a:
          move = "left"
      if event.key == pygame.K_s:
          move = "up"
      if event.key == pygame.K_w:
          move = "down"
      x , y = nextPosition(move, x , y)

pygame.quit()