import pygame

pygame.init()

clock = pygame.time.Clock()

running = True

window_size = (600,600)

screen = pygame.display.set_mode((window_size))


x = 250 
y = 250 
size = 60 
speed = 200

delta_time = 0.1

while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  keys = pygame.key.get_pressed()

  if keys[pygame.K_LEFT]:
    x -= speed * delta_time
  if keys[pygame.K_RIGHT]:
    x += speed * delta_time
  if keys[pygame.K_UP]:
    y -= speed * delta_time
  if keys[pygame.K_DOWN]:
    y += speed * delta_time

  screen.fill((0,0,0))
  pygame.draw.rect(screen, (255,255,255), (x, y, size, size))  
    
  delta_time = clock.tick(60)/1000
  pygame.display.flip()

pygame.quit()

