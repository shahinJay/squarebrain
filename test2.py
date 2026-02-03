import pygame
import random as rd

pygame.init()
running = True
cell_size = 64
cell_count=8
size=cell_size*cell_count #screen Size
screen = pygame.display.set_mode((size, size))

clock = pygame.time.Clock()
delta = 0.1

def randPosition():
   return int(64 * rd.randrange(8))

a=randPosition()
b=a



moving_d = False
moving_a = False
moving_s = False
moving_w = False

grid_line_size = 1
grid_color = (255, 255, 255)
def draw_grid():
    
    for x in range(size):
      if x%cell_size == 0:
        pygame.draw.line(screen, grid_color, (x, 0), (x, size), grid_line_size)
    
    for y in range(size):
      if y%cell_size == 0:
        pygame.draw.line(screen, grid_color, (0, y), (size, y), grid_line_size)



while running:
  screen.fill((0, 0, 0))
  draw_grid()
  red = (255,0,0)
  green = (0,255,0)
  blue = (0,0,255)

  if moving_d:
    a += 200 * delta
  if moving_a:
    a -= 200 * delta
  if moving_s:
    b += 200 * delta
  if moving_w:
    b -= 200 * delta





  pygame.draw.rect(screen, red, (384,256,64,64))
  pygame.draw.rect(screen, green, (a,b, 64, 64))
  
  pygame.display.flip()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_d:
            moving_d = True
        if event.key == pygame.K_a:
            moving_a = True
        if event.key == pygame.K_s:
            moving_s = True
        if event.key == pygame.K_w:
            moving_w = True

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_d:
            moving_d = False
        if event.key == pygame.K_a:
            moving_a = False
        if event.key == pygame.K_s:
            moving_s = False
        if event.key == pygame.K_w:
            moving_w = False

  delta = clock.tick(60) / 1000
  delta = max(0.001, min(0.1, delta))

pygame.quit()