from cards import Cards
import random

class Computer:

  def __init__(self, health):
    self.health = health
    
  def take_damage(self, damage):
    self.health -= damage
    if self.health <= 0:
      print('Computer has died!')
      print('Player has won!')
      exit()
  
  def draw_cards(self):
    self.draw = Cards()
    self.draw.draw_cards()

  def select_card(self):
    selection = random.choice(self.draw.draw_cards)
    print('Computer has chosen ' + selection[0])
    return selection