import random
import csv

class Cards:
  def draw_cards(self):
    with open('cards.csv') as card_list:
      self.draw_cards = random.sample(list(csv.reader(card_list, delimiter=':')) , 5)

  def card_details(self):
    option = 1
    for cards in self.draw_cards:
      print(f"\n{option}. {cards[0]}, Damage: {cards[1]}")
      option += 1

  def select_card(self, choice):
    return self.draw_cards[int(choice)- 1]
    