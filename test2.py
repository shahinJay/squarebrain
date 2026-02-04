import pygame
import random as rd
from grid import grid

pygame.init()
running = True
cell_size = 64
cell_count=8
size = cell_size*cell_count #screen Size
screen = pygame.display.set_mode((size, size))

grid_line_size = 1
grid_color = (255, 255, 255)

playground = grid(screen = screen, disp_x=size, disp_y=size)

x = 4
y = 2

gx = 5
gy = 5

goal_pos = (gx, gy)

def randPosition():
  return rd.randrange(8)

def spawn(x, y):
  if (x == gx and y == gy):
    spawn(x, y)
  else:
    x = randPosition()
    y = randPosition()
  return x , y

def nextPosition(move, currentX, currentY):
  if move == "right":
    currentX += 1
  elif move == "left":
    currentX -= 1
  elif move == "up":
    currentY += 1
  elif move == "down":
    currentY -= 1
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


def states(x, y, gx, gy):
  green_cell = (x,y)
  red_cell = (gx,gy)
  print(red_cell)

  cell_list=list()
  state_list=list()
  for i in range(8):
    for j in range(8):
      cell = (i,j)
      cell_list.append(cell)

      if cell == green_cell or cell == red_cell:
        state_list.append((1))
        print(1)
      else:
        state_list.append((0))

  return dict(zip(cell_list, state_list))

print(states(x , y, gx, gy))
#main function of loop
while running:
  screen.fill((0, 0, 0))
  playground.draw_grid(cell_size=cell_size)
  red = (255,0,0)
  green = (0,255,0)
  blue = (0,0,255)

  pygame.draw.rect(screen, red, (gx * cell_size, gy*cell_size, cell_size, cell_size))
  pygame.draw.rect(screen, green, (x * cell_size, y * cell_size, cell_size, cell_size))


  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      x, y = handle_input(event, x, y) #HANDLE INPUTS
      print(states(x , y, gx, gy))

  
  pygame.display.flip()
  

pygame.quit()