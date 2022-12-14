import pygame
from pygame.locals import *
from random import random
import time

class App:
  BLACK = (0, 0, 0)
  WHITE = (255, 255, 255)
  GRAY = (130,130,130)
  SCOREFONT = 0
  
  def __init__(self):
    self._running = False
    self._display_surf = None
    self.score = 0
    self.size = self.weight, self.height = 390, 420
    self.snake = [(6,6), (6,7), (6,8)]
    self.manzana = (0,0)
    self.on_init()
    self.contador = 10
    self.x = 0
    self.current_event = None

  def on_init(self):
    pygame.init()
    App.SCOREFONT = pygame.font.SysFont("dejavusansmono", 25)
    self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
    pygame.display.set_caption("Snake")
    self._display_surf.fill(App.WHITE)
    self._running = True

  def draw_snake(self):
    for e in self.snake:
      pygame.draw.rect(self._display_surf, App.GRAY, pygame.Rect(e[0]*30+1, (e[1]+1)*30+1, 28, 28), 28)

  def reset_snake(self):
    for e in self.snake:
      pygame.draw.rect(self._display_surf, App.WHITE, pygame.Rect(e[0]*30+1, (e[1]+1)*30+1, 28, 28), 28)
    self.snake = [(6,6), (6,7), (6,8)]
    self.current_event = None

  def draw_apple(self):
    if self.manzana != -1:
        pygame.draw.rect(self._display_surf, App.BLACK, pygame.Rect(self.manzana[0]*30+1, (self.manzana[1]+1)*30+1, 28, 28), 28)

  def check_restrictions(self, direction):
    cases = [
      self.snake[0][1] == 0 and direction == "up",
      self.snake[0][1] == 12 and direction == "down",
      self.snake[0][0] == 0 and direction == "left",
      self.snake[0][0] == 12 and direction == "right",
      (self.snake[0][0],self.snake[0][1]-1) in self.snake[2:len(self.snake)-1] and direction == "up",
      (self.snake[0][0],self.snake[0][1]+1) in self.snake[2:len(self.snake)-1] and direction == "down",
      (self.snake[0][0]-1,self.snake[0][1]) in self.snake[2:len(self.snake)-1] and direction == "left",
      (self.snake[0][0]+1,self.snake[0][1]) in self.snake[2:len(self.snake)-1] and direction == "right",
    ]
    if True in cases:
      death_message = "You bitted yourself!" if True in cases[4:] else "You hit the wall!"
      self.draw_game_over_screen(death_message)
      self.draw_try_again_screen(self.score)
      self.score = 0
      self.draw_grid(self.score)
      self.contador = 10
      if self.manzana != -1:
        pygame.draw.rect(self._display_surf, App.WHITE, pygame.Rect(self.manzana[0]*30+1, (self.manzana[1]+1)*30+1, 28, 28), 28)
      self.reset_snake()
      self.pixel_random()
      return True
    else:
      return False

  def case_up(self):
    if self.check_restrictions("up"):
      pass
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
        self.x = int(random()*10)+1
      if self.contador == self.x:
        self.pixel_random()

  def case_down(self):
    if self.check_restrictions("down"):
      pass
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
        self.x = int(random()*10)+1
      if self.contador == self.x:
        self.pixel_random()
  
  def case_left(self):
    if self.check_restrictions("left"):
      pass
    elif self.snake[0][0]-1 != self.snake[1][0]:
      self.contador += 1
      self.snake.insert(0,(self.snake[0][0]-1,self.snake[0][1]))
      if self.snake[0] != self.manzana:
        e = self.snake.pop()
        pygame.draw.rect(self._display_surf, App.WHITE, pygame.Rect(e[0]*30+1, (e[1]+1)*30+1, 28, 28), 28)
      else:
        self.contador = 0
        self.manzana = -1
        self.score += 10
        self.draw_grid(self.score)
        self.x = int(random()*10)+1
      if self.contador == self.x:
        self.pixel_random()
  
  def case_right(self):
    if self.check_restrictions("right"):
      pass
    elif self.snake[0][0]+1 != self.snake[1][0]:
      self.contador += 1
      self.snake.insert(0,(self.snake[0][0]+1,self.snake[0][1]))
      if self.snake[0] != self.manzana:
        e = self.snake.pop()
        pygame.draw.rect(self._display_surf, App.WHITE, pygame.Rect(e[0]*30+1, (e[1]+1)*30+1, 28, 28), 28)
      else:
        self.contador = 0
        self.manzana = -1
        self.score += 10
        self.draw_grid(self.score)
        self.x = int(random()*10)+1
      if self.contador == self.x:
        self.pixel_random()

  def on_event(self):
    #print(pygame.key.get_pressed()[pygame.K_RIGHT])
    """if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        self.case_up()
      elif event.key == pygame.K_DOWN:
        self.case_down()
      elif event.key == pygame.K_LEFT:
        self.case_left()
      elif event.key == pygame.K_RIGHT:
        self.case_right()
    elif event.type == pygame.QUIT:
      self._running = False"""
    #print(event)
    if self.current_event == None:
      pass
    elif self.current_event.type == pygame.QUIT:
      self._running = False
    elif self.current_event.type == pygame.KEYDOWN or self.current_event.type == pygame.KEYUP:
      if self.current_event.key == pygame.K_UP:
        self.case_up()
      elif self.current_event.key == pygame.K_DOWN:
        self.case_down()
      elif self.current_event.key == pygame.K_LEFT:
        self.case_left()
      elif self.current_event.key == pygame.K_RIGHT:
        self.case_right()
  
  def pixel_random(self):
    randomx = int(random()*(169-len(self.snake)))
    contador = -1
    while randomx != contador:
      if (contador%13, contador//13) in self.snake or (randomx == 0 and (0,0) in self.snake):
        randomx += 1
      contador += 1
    contador -= 1
    if contador == -1:
      contador = 0
    self.manzana = (contador%13, contador//13)

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
        
  def draw_start_screen(self):        
    self.menu_screen_prototype("Start game", 35, "PRESS ENTER", 25, 20)
    
  def draw_game_over_screen(self, death_message):
    self.menu_screen_prototype("GAME OVER!", 40, death_message, 25, 25, bg_rgb=(255, 55, 55))
  
  def draw_try_again_screen(self, score):
    self.menu_screen_prototype(f"Final score: {score}", 35, "Press ENTER to try again", 25, 20, bg_rgb=(100, 255, 100))
  
  def menu_screen_prototype(self, text1 = 'Title', text1_size = 30, text2 = 'Subtitle', text2_size = 30, space_between_text = 10, typography = 'dejavusansmono', bg_rgb = (255, 255, 255)):
    self._display_surf.fill(bg_rgb)
    # Set 1st text object
    text1_font = pygame.font.SysFont(typography, text1_size, bold=True)
    start_text = text1_font.render(text1, True, (0, 0, 0))
    textRect = start_text.get_rect()
    textRect.center = (self.size[0] / 2), ( (self.size[1] / 2) - space_between_text )
    # Set 2nd text object
    text2_font = pygame.font.SysFont(typography, text2_size, bold=True)
    start_text_instruction = text2_font.render(text2, True, (0, 0, 0))
    textInstructionRect = start_text_instruction.get_rect()
    textInstructionRect.center = (self.size[0] / 2), ( (self.size[1] / 2) + space_between_text )
    # Displays 2 text lines
    self._display_surf.blit(start_text, textRect)
    self._display_surf.blit(start_text_instruction, textInstructionRect)
    pygame.display.update()
    
    self._display_surf.fill(App.WHITE)
    
    # Waits for the indicated input
    intro = True
    while intro:
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RETURN:
            intro = False
        elif event.type == pygame.QUIT:
          pygame.quit()
          quit()

  def on_execute(self):
    self.pixel_random()
    self.draw_start_screen()
    self.draw_grid(0)
    while self._running:
      events = pygame.event.get()
      if len(events) != 0:
        event = events[-1]
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP or event.type == pygame.QUIT:
          if self.current_event == None:
            self.current_event = events[-1]
          else:
            opposite_keys = (
              event.key == pygame.K_UP and self.current_event.key == pygame.K_DOWN,
              event.key == pygame.K_DOWN and self.current_event.key == pygame.K_UP,
              event.key == pygame.K_LEFT and self.current_event.key == pygame.K_RIGHT,
              event.key == pygame.K_RIGHT and self.current_event.key == pygame.K_LEFT
            )
            print(opposite_keys)
            if not True in opposite_keys:
              self.current_event = events[-1]

      self.on_event()
      
      self.draw_snake()
      self.draw_apple()
      pygame.display.update()
      time.sleep(1)

    self.on_cleanup()

if __name__ == "__main__":
  app = App()
  app.on_execute()