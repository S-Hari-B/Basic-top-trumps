from battle import Battle
from cards import Cards

class Menu:
    def menu_options(self):
      select = True
      while select:
        print('Welcome to Basic Top Trumps!\n')
        print('1. New game')
        print('2. Load Game')
        print('3. View Full Card List')
        print('4. Exit Game')
        choice = int(input('\nPlease select an option: '))
        print('')
        if choice == 1:
          battle = Battle()
          battle.battle()
          select = False
        elif choice == 2:
          print('Not implemented yet')
          select = False
        elif choice == 3:
          cards = Cards()
          cards.view_full_card_list()
          select = False
        elif choice == 4:
          select = False
          exit(0)
        else:
          print('Please enter a valid option')