from cards import Cards


class Player:

  def __init__(self, health):
    self.health = health
    self.cards = Cards()

  def take_damage(self, damage):
    self.health -= damage
    if self.health <= 0:
      print('\nYou have died!')
      print('Computer has won!')

  def draw_cards(self):
    print('Here are your available cards:')
    self.cards.card_details()

  def select_card(self):
    choices = self.cards.draw_cards()
    check = True
    while check:
      choice_str = input(
        f"\nSelect a card to play (enter a number between 1 and {len(choices)}): "
      )
      try:
        choice = int(choice_str)
        if 1 <= choice <= len(choices):
          selected_card = self.cards.select_card(choice)
          print('\n---------------------------')
          print(f'\nYou have chosen {selected_card[0]}')
          check = False
        else:
          print('\nPlease enter a valid number')
      except ValueError:
        print('\nPlease enter a valid number')
    return selected_card
