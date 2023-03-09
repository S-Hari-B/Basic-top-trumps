from player import Player
from computer import Computer
import random

class Battle:
  def __init__(self):
    self.player = Player(30, 0) 
    self.gold = self.player.gold

  def battle(self):
    gold_dropped = random.randint(1, 10)
    computer = Computer(1, gold_dropped)
    
    while self.player.health > 0 and computer.health > 0:
      print('\n---------------------------')
      print(f"Player health: {self.player.health}")
      print(f"Player gold: {self.player.gold}")
      print(f"Computer health: {computer.health}")
      print('---------------------------\n')
      
      self.player.draw_cards()
      player_card = self.player.select_card()
      if not player_card:
        continue     
      computer.draw_cards()
      computer_card = computer.select_card()

      print('\n---------------------------')
      print(f"You played {player_card[0]} with damage {player_card[1]}")
      print(f"Computer played {computer_card[0]} with damage {computer_card[1]}")
      print('---------------------------\n')
      player_damage = int(player_card[1])
      computer_damage = int(computer_card[1])
      damage_diff = abs(player_damage - computer_damage)
      if int(player_damage) > int(computer_damage):
        print('Player wins round!\n')
        self.player.add_gold(computer.gold)
        print(f"Player gold: {self.player.gold}")
        computer.take_damage(damage_diff)
      elif computer_damage > player_damage:
        print('Computer wins round!\n')
        self.player.take_damage(damage_diff)
      else:
        print('Draw! Neither takes damage!\n')
    print('\n---------------------------')
    choice = input("Do you want to play again? (y/n) ")

    if choice.lower() == "y":
      print('\n')
      self.battle()  
    else:
      self.gold = self.player.gold 
      exit(0)
