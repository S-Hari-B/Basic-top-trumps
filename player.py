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
    choices = []
    for card in self.draw.draw_cards:
        choices.append(card[0])
    check = True
    while check:
        choice_str = input("\nSelect a card to play from the following choices: ")
        choice = choice_str
        if choice in choices:
            self.draw.select_card(choices.index(choice))
            print(f'\nYou have chosen {choice_str}')
            selected_card = self.draw.draw_cards[choices.index(choice)]
            check = False
        else:
            print('\nPlease enter a valid card')
    return selected_card