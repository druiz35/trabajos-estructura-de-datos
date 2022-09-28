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
  BLACK = (0, 0, 0)
  WHITE = (255, 255, 255)
  SCOREFONT = 0
  def __init__(self):
    self._running = False
    self._display_surf = None
    self.size = self.weight, self.height = 390, 420
  def on_init(self):
    pygame.init()
    App.SCOREFONT = pygame.font.SysFont("dejavusansmono", 25)
    self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
    pygame.display.set_caption("Snake")
    self._display_surf.fill(App.WHITE)
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

  def draw_grid(self, score):
    score = App.SCOREFONT.render("Score: " + str(score), True, App.BLACK)
    self._display_surf.blit(score, [0, 0])
    blockSize = 30
    for x in range(0, blockSize*13, blockSize):
      for y in range(blockSize, blockSize*14, blockSize):
        rect = pygame.Rect(x, y, blockSize, blockSize)
        pygame.draw.rect(self._display_surf, App.BLACK, rect, 1)

  def on_execute(self):
    if self.on_init() == False:
      self._running = False
    
    while self._running:
      self.draw_grid(0)
      for event in pygame.event.get():
        self.on_event(event)
      self.on_loop()
      self.on_render()
      pygame.display.update()
    self.on_cleanup()

if __name__ == "__main__":
  app = App()
  app.on_execute()