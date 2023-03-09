import random
import csv


class Cards:

  def __init__(self):
    self.cards = []
    self.selected_cards = []
    self.generate_cards()

  def __len__(self):
    return len(self.cards)

  def generate_cards(self):
    with open('cards.csv') as card_list:
      self.cards = random.sample(list(csv.reader(card_list, delimiter=':')), 5)

  def draw_cards(self):
    return self.cards

  def card_details(self):
    option = 1
    for cards in self.cards:
      print(f"\n{option}. {cards[0]}, Damage: {cards[1]}")
      option += 1

  def select_card(self, choice):
    selected_card = self.cards[int(choice) - 1]
    self.selected_cards.append(selected_card)
    self.cards.remove(selected_card)
    return selected_card

  def view_full_card_list(self):
    print("Full Card List:")
    print('---------------------------')
    with open('cards.csv') as card_list:
      option = 1
      for card in csv.reader(card_list, delimiter=':'):
        print(f"{option}. {card[0]}, Damage: {card[1]}")
        option += 1

  def reset_selected_cards(self):
    self.cards.extend(self.selected_cards)
    self.selected_cards = []
