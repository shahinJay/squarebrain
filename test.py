import pygame

pygame.init()
running = True
screen = pygame.display.set_mode((600, 600))

clock = pygame.time.Clock()
delta = 0.1
a=101
b=101
moving_d = False
moving_a = False
moving_s = False
moving_w = False

grid_line_size = 1
grid_color = (255, 255, 255)
grid_size = 25
def draw_grid():
    
    for x in range(600):
      if x%grid_size == 0:
        pygame.draw.line(screen, grid_color, (x, 0), (x, 600), grid_line_size)
    
    for y in range(600):
      if y%grid_size == 0:
        pygame.draw.line(screen, grid_color, (0, y), (600, y), grid_line_size)



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


  
  pygame.draw.rect(screen, red, (301,301,24,24))
  pygame.draw.rect(screen, green, (a,b,24,24))
  
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