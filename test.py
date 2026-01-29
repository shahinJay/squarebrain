import pygame
pygame.init()

screen = pygame.display.set_mode((800,500))
running = True

clock = pygame.time.Clock()
delta = 0.1
x=100
y=100
moving_d = False
moving_a = False
moving_s = False
moving_w = False

while running:
  screen.fill((255, 255, 255))
  red = (255,0,0)
  green = (0,255,0)
  blue = (0,0,255)

  if moving_d:
    x += 200 * delta
  if moving_a:
    x -= 200 * delta
  if moving_s:
    y += 200 * delta
  if moving_w:
    y -= 200 * delta

  pygame.draw.circle(screen, green, (x,y), 20)
  pygame.draw.circle(screen, red, (600,400), 20)
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