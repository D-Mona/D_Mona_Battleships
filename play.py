"""
OS module is used for clearing the terminal.
"""
from battleships import Battleships, wipe_terminal


class Play:
    """
    Play's a game between two Battleship objects.
    Player vs Computer.    
    """

    def __init__(self):
        # Battleship object representing the human player.
        self.player = Battleships()
        # Battleship object representing the computer.
        self.computer = Battleships()
        # Game message - Updated throughout(Player turns, game status etc.)
        self.game_message = 'Fire your missile !'
        self.begin_game()

    def begin_game(self):
        """
        Welcome the user and provide options to see the rules or setup the game.
        Forces inputs of R or S.
        """
        wipe_terminal()
        print('Welcome to this simple command line Battleships game...\n')
        print('')
        user_input = input('Enter S for Setup / Enter R for Rules\n')
        user_input = user_input.upper()
        if user_input in ('R', 'S'):
            if user_input == 'R':
                self.rules()
            else:
                self.game_setup()
        else:
            self.begin_game()

    def rules(self):
        """
        Displays the rules of the game.
        Periodically waits for a user to press Enter before continuing to the next -
        section of the rules.
        User can read the rules again, or to begin a game.
        """
        wipe_terminal()
        print('General Rules:')
        print('')
        print('You will place a given amount of your fleets ships upon a grid.\n'
              '\n'
              'After which, both you and the computer will guess the coordinates\n'
              "of each other's ship locations in order to destroy them.\n"
              '\n'
              "The first player to destroy all of the enemy's ships is declared the winner.\n")
        print('')
        input('Press Enter to learn about the game board.')
        wipe_terminal()
        print('You will have a choice of 3 game sizes.')
        print('Small, Medium or Large.\n')
        print('A Medium sized game board is below:')
        print('')
        print('  A B C D E F G H')
        print('1 ^ W W W W O W W')
        print('2 * W W O W W W W')
        print('3 W W O ^ W W * W')
        print('4 W W W W W W ^ O')
        print('')
        print('---> W <--- These are the waves and they are empty positions.\n'
              '\n''---> ^ <--- When placed upon the waves your ships are marked like this.''\n'
              '\n''---> * <--- Hits to ships are marked like this.\n'
              '\n''---> O <--- Misses are marked like this.\n'
              )
        print('')
        input('Press Enter to learn how to place your ships.')
        wipe_terminal()
        print('Ship placements and firing attempts on the opposition work in the same way. \n'
              'Automatic ship placements and firing attempts are always available.\n'
              )
        print(
            'If entering manually, a letter followed by a number is a required coordinate.\n'
            'Letters are not case sensitive.\n')
        print('Examples of C4 and F2 placements are below:')
        print('')
        print('  A B C D E F G H')
        print('1 W W W W W W W W')
        print('2 W W W W W ^ W W')
        print('3 W W W W W W W W')
        print('4 W W ^ W W W W W')
        print('')
        print(
            'Upon placing all of your ships the game will begin and you will fire first.\n')
        print('')
        input_str = input(
            'Enter S for game setup / Press Enter for another recap of the rules\n'
        )
        user_input = input_str.upper()
        if user_input == 'S':
            self.game_setup()
        else:
            self.rules()

    def game_setup(self):
        """
        Setup of the computer and player Battleships.
        Once the board size is set the computer can auto build a board.
        """
        Battleships.set_board_size()
        self.player.create_board()
        self.computer.create_board()
        self.computer.auto_ship_placements()
        self.player.choose_ship_placement()
        self.play_game()

    def game_display(self):
        """
        Displays the two game boards and their respective ships remaining.
        Displays the game message.
        """
        wipe_terminal()
        self.player.guess_board_display()
        print('')
        print(f'Enemy Ships: {self.computer.ships}')
        print('')
        self.player.player_board_display()
        print('')
        print(f'Friendly Ships: {self.player.ships}')
        print('')
        print(self.game_message)
        print('')

    def choose_fire_mode(self):
        """"
        A choice of automatic or manual fire modes.
        Forces inputs of A or M.
        """
        self.game_display()
        user_input = input(
            'Enter A to auto fire / Enter M to input your coordinates')
        user_input = user_input.upper()
        if user_input in ('A', 'M'):
            if user_input == 'A':
                self.auto_fire()
            elif user_input == 'M':
                self.manual_fire()
        else:
            self.choose_fire_mode()

    def manual_fire(self):
        """
        Fire on a position at the given coordinates.
        Raises a key error where an invalid key has been used as the coordinate.
        Will not allow to fire on a position already fired upon.
        """
        self.game_message = 'Take aim !'
        while True:
            try:
                while True:
                    self.game_display()
                    key = input('Enter the coordinates for your missile !')
                    key = key.upper()
                    if key not in self.computer.player_board:
                        raise KeyError
                    break
                if self.player.guess_board.get(key) in ('O', '*'):
                    self.game_message = f'You already fired at position {
                        key}, silly !'
                    self.game_display()
                    input('Press Enter to try again !\n')
                    self.game_message = 'Take aim !'
                    self.manual_fire()
                elif self.computer.player_board.get(key) == '^':
                    self.game_message = 'Firing your missile...'
                    self.game_display()
                    sleep(3)
                    self.player.guess_board.update({key: '*'})
                    self.computer.ships -= 1
                    self.game_message = f'You fired at coordinates {
                        key} and HIT !'
                    self.game_display()
                elif self.computer.player_board.get(key) == 'W':
                    self.game_message = 'Firing your missile...'
                    self.game_display()
                    sleep(3)
                    self.player.guess_board.update({key: 'O'})
                    self.game_message = f'You fired at coordinates {
                        key} and missed !'
                    self.game_display()
            except KeyError:
                self.game_message = f"The coordinates '{
                    key}' you entered are invalid !"
                self.game_display()
                print('Letter followed by number - And must be a valid coordinate on the board.\n'
                      '\n'
                      'Example: A1, A2 etc. - And not fired upon previously.\n'
                      )
                input('Press Enter to try again.')
                self.manual_fire()
            break

    def game_setup(self):
        """
        """

