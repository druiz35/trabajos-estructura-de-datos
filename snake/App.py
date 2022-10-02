import pygame
from pygame.locals import *
from random import random
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
  GRAY = (130,130,130)
  SCOREFONT = 0
  def __init__(self):
    self._running = False
    self._display_surf = None
    self.size = self.weight, self.height = 390, 420
    self.snake = [(6,6), (6,7), (6,8)]
    self.manzana = (0,0)
    self.score = 0
    self.contador = 10
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
        if self.snake[0][1] == 0 or (self.snake[0][0],self.snake[0][1]-1) in self.snake[2:len(self.snake)-1]:
          self.score = 0
          self.draw_grid(self.score)
          self.contador = 10
          if self.manzana != -1:
            pygame.draw.rect(self._display_surf, App.WHITE, pygame.Rect(self.manzana[0]*30+1, (self.manzana[1]+1)*30+1, 28, 28), 28)
          self.pixel_random()
          for e in self.snake:
            pygame.draw.rect(self._display_surf, App.WHITE, pygame.Rect(e[0]*30+1, (e[1]+1)*30+1, 28, 28), 28)
          self.snake = [(6,6), (6,7), (6,8)]
        elif self.snake[0][1]-1 != self.snake[1][1] and self.snake[0][1] != 0:
          self.contador += 1
          self.snake.insert(0,(self.snake[0][0],self.snake[0][1]-1))
          if self.snake[0] != self.manzana:
            e = self.snake.pop()
            pygame.draw.rect(self._display_surf, App.WHITE, pygame.Rect(e[0]*30+1, (e[1]+1)*30+1, 28, 28), 28)
          else:
            self.contador = 0
            self.manzana = -1
            self.score += 10
            self.draw_grid(self.score)
          if self.contador == 10:
            self.pixel_random()
      elif event.key == pygame.K_DOWN:
        if self.snake[0][1] == 12 or (self.snake[0][0],self.snake[0][1]+1) in self.snake[2:len(self.snake)-1]:
          self.score = 0
          self.draw_grid(self.score)
          self.contador = 10
          if self.manzana != -1:
            pygame.draw.rect(self._display_surf, App.WHITE, pygame.Rect(self.manzana[0]*30+1, (self.manzana[1]+1)*30+1, 28, 28), 28)
          self.pixel_random()
          for e in self.snake:
            pygame.draw.rect(self._display_surf, App.WHITE, pygame.Rect(e[0]*30+1, (e[1]+1)*30+1, 28, 28), 28)
          self.snake = [(6,6), (6,7), (6,8)]
        elif self.snake[0][1]+1 != self.snake[1][1]:
          self.contador += 1
          self.snake.insert(0,(self.snake[0][0],self.snake[0][1]+1))
          if self.snake[0] != self.manzana:
            e = self.snake.pop()
            pygame.draw.rect(self._display_surf, App.WHITE, pygame.Rect(e[0]*30+1, (e[1]+1)*30+1, 28, 28), 28)
          else:
            self.contador = 0
            self.manzana = -1
            self.score += 10
            self.draw_grid(self.score)
          if self.contador == 10:
            self.pixel_random()
      elif event.key == pygame.K_LEFT:
        if self.snake[0][0] == 0 or (self.snake[0][0]-1,self.snake[0][1]) in self.snake[2:len(self.snake)-1]:
          self.score = 0
          self.draw_grid(self.score)
          self.contador = 10
          if self.manzana != -1:
            pygame.draw.rect(self._display_surf, App.WHITE, pygame.Rect(self.manzana[0]*30+1, (self.manzana[1]+1)*30+1, 28, 28), 28)
          self.pixel_random()
          for e in self.snake:
            pygame.draw.rect(self._display_surf, App.WHITE, pygame.Rect(e[0]*30+1, (e[1]+1)*30+1, 28, 28), 28)
          self.snake = [(6,6), (6,7), (6,8)]
        elif self.snake[0][0]-1 != self.snake[1][0]:
          self.contador += 1
          self.snake.insert(0,(self.snake[0][0]-1,self.snake[0][1]))
          if self.contador == 10:
            self.pixel_random()
          if self.snake[0] != self.manzana:
            e = self.snake.pop()
            pygame.draw.rect(self._display_surf, App.WHITE, pygame.Rect(e[0]*30+1, (e[1]+1)*30+1, 28, 28), 28)
          else:
            self.contador = 0
            self.manzana = -1
            self.score += 10
            self.draw_grid(self.score)
          if self.contador == 10:
            self.pixel_random()
      elif event.key == pygame.K_RIGHT:
        if self.snake[0][0] == 12 or (self.snake[0][0]+1,self.snake[0][1]) in self.snake[2:len(self.snake)-1]:
          self.score = 0
          self.draw_grid(self.score)
          self.contador = 10
          if self.manzana != -1:
            pygame.draw.rect(self._display_surf, App.WHITE, pygame.Rect(self.manzana[0]*30+1, (self.manzana[1]+1)*30+1, 28, 28), 28)
          self.pixel_random()
          for e in self.snake:
            pygame.draw.rect(self._display_surf, App.WHITE, pygame.Rect(e[0]*30+1, (e[1]+1)*30+1, 28, 28), 28)
          self.snake = [(6,6), (6,7), (6,8)]
        
        elif self.snake[0][0]+1 != self.snake[1][0]:
          self.contador += 1
          if self.contador == 10:
            self.pixel_random()
          self.snake.insert(0,(self.snake[0][0]+1,self.snake[0][1]))
          if self.snake[0] != self.manzana:
            e = self.snake.pop()
            pygame.draw.rect(self._display_surf, App.WHITE, pygame.Rect(e[0]*30+1, (e[1]+1)*30+1, 28, 28), 28)
          else:
            self.contador = 0
            self.manzana = -1
            self.score += 10
            self.draw_grid(self.score)
          if self.contador == 10:
            self.pixel_random()
    elif event.type == pygame.QUIT:
      self._running = False
  def pixel_random(self):
    randomx = int(random()*(169-len(self.snake)))
    contador = -1
    w = 0
    while randomx != contador:
      if (contador%13, contador//13) in self.snake:
        randomx += 1
        w += 1
      contador += 1
    contador -= 1
    if contador == -1:
      contador = 0
    self.manzana = (contador%13, contador//13)
  def on_loop(self):
    pass
  
  def on_render(self):
    pass

  def on_cleanup(self):
    pygame.quit()

  def draw_grid(self, scores):
    pygame.draw.rect(self._display_surf, App.WHITE, pygame.Rect(0, 0, 390, 420), 28)
    scores = App.SCOREFONT.render("Score: " + str(scores), True, App.BLACK)
    self._display_surf.blit(scores, [0, 0])
    blockSize = 30
    for x in range(0, blockSize*13, blockSize):
      for y in range(blockSize, blockSize*14, blockSize):
        rect = pygame.Rect(x, y, blockSize, blockSize)
        pygame.draw.rect(self._display_surf, App.BLACK, rect, 1)

  def on_execute(self):
    if self.on_init() == False:
      self._running = False
    self.pixel_random()
    self.draw_grid(0)
    while self._running:
      for event in pygame.event.get():
        self.on_event(event)
      for e in self.snake:
        pygame.draw.rect(self._display_surf, App.GRAY, pygame.Rect(e[0]*30+1, (e[1]+1)*30+1, 28, 28), 28)
      if self.manzana != -1:
        pygame.draw.rect(self._display_surf, App.BLACK, pygame.Rect(self.manzana[0]*30+1, (self.manzana[1]+1)*30+1, 28, 28), 28)
      self.on_loop()
      self.on_render()
      pygame.display.update()
    self.on_cleanup()

if __name__ == "__main__":
  app = App()
  app.on_execute()