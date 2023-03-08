from cards import Cards

class Player:

  def __init__(self, health):
    self.health = health

  def take_damage(self, damage):
    self.health -= damage
    if self.health <= 0:
      print('\nYou have died!')
      print('Computer has won!')
  
  def draw_cards(self):
    self.draw = Cards()
    self.draw.draw_cards()
    print('Here are your available cards:')
    self.draw.card_details()

  def select_card(self):
    choices = self.draw.draw_cards
    check = True
    while check:
      choice_str = input(f"\nSelect a card to play (enter a number between 1 and {len(choices)}): ")
      try:
        choice = int(choice_str) - 1  
        if 0 <= choice < len(choices):
          self.draw.select_card(choice)
          selected_card = choices[choice]
          print(f'\nYou have chosen {selected_card[0]}')
          check = False
        else:
          print('\nPlease enter a valid number')
      except ValueError:
        print('\nPlease enter a valid number')
    return selected_card