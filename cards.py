import random
import csv


class Cards:

  def __init__(self):
    self.cards = []
    self.generate_cards()

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
    return self.cards[int(choice) - 1]
