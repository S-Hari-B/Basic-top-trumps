from battle import Battle
from cards import Cards

class Menu:

  def menu_options(self):
    select = True
    while select:
      print('---------------------------')
      print('Welcome to Basic Top Trumps!')
      print('---------------------------\n')
      print('---------------------------')
      print('Main Menu!')
      print('---------------------------\n')
      print('1. New game')
      print('2. Load Game')
      print('3. View Full Card List')
      print('4. Exit Game')
      choice = int(input('\nPlease select an option: '))
      print('')
      if choice == 1:
        self.battle_menu()
        select = False
      elif choice == 2:
        print('Not implemented yet')
      elif choice == 3:
        cards = Cards()
        cards.view_full_card_list()
        print('')
      elif choice == 4:
        select = False
        exit(0)
      else:
        print('Please enter a valid option\n')

  def battle_menu(self):
    print('---------------------------')
    print('Battle Menu!')
    print('---------------------------\n')
    option = True
    while option:
      print('1. Start Battle!')
      print('2. View Player Stats')
      print('3. View Player Cards')
      print('4. Return to Main Menu')
      print('5. Exit Game')
      choice = int(input('\nPlease select an option: '))
      if choice == 1:
        battle = Battle()
        battle.battle()
        option = False
      if choice == 2:
        print('Still to add')
      if choice == 3:
        print('Still to add')
      if choice == 4:
        print('Returning to menu')
        self.menu_options
        option = False
      if choice == 5:
        print('Exiting Game')
        exit(0)
        option = False
      else:
        print('Please enter a valid option\n')
