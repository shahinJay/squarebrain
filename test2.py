import pygame
import random as rd

pygame.init()
running = True
size=512
screen = pygame.display.set_mode((size, size))

grid_line_size = 1
grid_color = (255, 255, 255)

x = 0
y = 0

def randPosition():
   return int(64 * rd.randint(0,8))


def spawn(x, y):
  x = randPosition()
  y = randPosition()
  return x, y


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
  draw_grid()
  red = (255,0,0)
  green = (0,255,0)
  blue = (0,0,255)
     
  pygame.draw.rect(screen, red, (384,256,64,64))
  pygame.draw.rect(screen, green, (x,y, 64, 64))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      x, y = handle_input(event, x, y) #HANDLE INPUTS

  pygame.display.flip()
  
       

    

pygame.quit()