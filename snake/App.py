import pygame
from pygame.locals import *
"""
pygame.init()
dis = pygame.display.set_mode((400,300))
pygame.display.update()
pygame.display.set_caption("Snake")
game_over = False
while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over=True
pygame.quit()
quit()
"""
class App:
  def __init__(self):
    self._running = False
    self._display_surf = None
    self.size = self.weight, self.height = 640, 400
  
  def on_init(self):
    pygame.init()
    self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
    pygame.display.set_caption("Snake")
    self._running = True
  
  def on_event(self, event):
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        print("UP")
      elif event.key == pygame.K_DOWN:
        print("DOWN")
      elif event.key == pygame.K_LEFT:
        print("LEFT")
      elif event.key == pygame.K_RIGHT:
        print("RIGHT")
    elif event.type == pygame.QUIT:
      self._running = False
    
  def on_loop(self):
    pass
  
  def on_render(self):
    pass

  def on_cleanup(self):
    pygame.quit()

  def on_execute(self):
    if self.on_init() == False:
      self._running = False
    
    while self._running:
      for event in pygame.event.get():
        self.on_event(event)
      self.on_loop()
      self.on_render()
    self.on_cleanup()

if __name__ == "__main__":
  app = App()
  app.on_execute()