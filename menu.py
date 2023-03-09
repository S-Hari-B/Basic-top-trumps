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
      print('---------------------------')
      print('1. New game')
      print('2. Load Game')
      print('3. View Full Card List')
      print('4. Exit Game')
      print('---------------------------')
      try:
        choice1 = int(input('\nPlease select an option: '))
        print('')
        if choice1 == 1:
          self.battle_menu()
          select = False
        elif choice1 == 2:
          print('Not implemented yet')
        elif choice1 == 3:
          cards = Cards()
          cards.view_full_card_list()
          print('')
        elif choice1 == 4:
          select = False
          exit(0)
      except ValueError:
          print('\nPlease enter a valid option\n')
          continue

  def battle_menu(self):
    print('---------------------------')
    print('Battle Menu!')
    print('---------------------------\n')
    option = True
    while option:
        print('---------------------------')
        print('1. Start Battle!')
        print('2. View Player Stats')
        print('3. View Player Cards')
        print('4. Return to Main Menu')
        print('5. Exit Game')
        print('---------------------------')
        try:
          choice2 = int(input('\nPlease select an option: '))
          if choice2 == 1:
              battle = Battle()
              battle.battle()
              option = False
          elif choice2 == 2:
              print('\nStill to add')
          elif choice2 == 3:
              print('\nStill to add')
          elif choice2 == 4:
              print('Returning to menu')
              self.menu_options()
              option = False
          elif choice2 == 5:
              print('Exiting Game')
              exit(0)
              option = False
          else:
              print('Invalid input. Please enter a valid option.')
        except ValueError:
            print('\nPlease enter a valid option\n')
            continue