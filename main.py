import pygame
import random as rd
from grid import grid

pygame.init()
running = True
cell_size = 64
cell_count=8
size=cell_size*cell_count #screen Size
screen = pygame.display.set_mode((size, size))

grid_line_size = 1
grid_color = (255, 255, 255)

playground = grid(screen = screen, disp_x=size, disp_y=size)

x = 0
y = 0

gx = 5
gy = 5

goal_pos = (gx * cell_size, gy *cell_size)

def randPosition():
   return int(cell_size * rd.randrange(8))

def spawn(x, y):
  while(x != goal_pos[0] and y!= goal_pos[1]):
    x = randPosition()
    y = randPosition()
  return x, y

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

def handle_input(event, x, y):
  
  move = "None"
  
  if event.key == pygame.K_d:
      move = "right"
  if event.key == pygame.K_a:
      move = "left"
  if event.key == pygame.K_s:
      move = "up"
  if event.key == pygame.K_w:
      move = "down"
  
  x , y = nextPosition(move, x , y)
  return x, y

x, y = spawn(x, y)
   
#main function of loop
while running:
  screen.fill((0, 0, 0))
  playground.draw_grid(cell_size=cell_size)
  red = (255,0,0)
  green = (0,255,0)
  blue = (0,0,255)
     
  pygame.draw.rect(screen, red, (goal_pos[0], goal_pos[1], cell_size, cell_size))
  pygame.draw.rect(screen, green, (x, y, cell_size, cell_size))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      x, y = handle_input(event, x, y) #HANDLE INPUTS

  pygame.display.flip()
  

pygame.quit()