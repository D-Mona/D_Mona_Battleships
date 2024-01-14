"""
Random module is used for generating random coordinates.
"""
import random
import os


def wipe_terminal():
    """
    Wipes all text in the terminal.
    Works for Windows, Mac and Linux. 
    Saw this variant on stackoverflow.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


class Battleships:
    """
    A class containing the logic for a basic command line Battleships game.

    """
    # Board size - Determined by the player on start up.
    board_size = ''

    def __init__(self):
        # Used for building a board [Rows, Columns].
        self.dimensions = ()
        # The player ships remaining.
        self.ships = 2
        # An overlay that sits on top of the game board displaying letters for cooordinates.
        self.letter_overlay = ''
        # A players board containing their ships, as well as opponent guesses and outcomes.
        self.player_board = {}
        # An opponent's board containing their guesses and outcomes.
        self.guess_board = {}

    @classmethod
    def set_board_size(cls):
        """
        Class method for setting the game size.
        The computer will auto-build a board to the correct size.
        Forces inputs of S, M or L.
        """
        wipe_terminal()
        user_input = input(
            'Enter S, M or L - Select Small, Medium or Large game mode.\n')
        user_input = user_input.upper()
        if user_input in ('S', 'M', 'L'):
            cls.board_size = user_input
            wipe_terminal()
        else:
            wipe_terminal()
            cls.set_board_size()

    def create_board(self):
        """
        A board with attributes ranging from small to large.        
        """
        size = self.board_size
        if size == 'S':
            self.dimensions = (2, 4)
            self.ships = 2
            self.letter_overlay = '  A B C D'
            self.player_board = self.populate_board()
            self.guess_board = self.populate_board()
        elif size == 'M':
            self.dimensions = (4, 8)
            self.ships = 4
            self.letter_overlay = '  A B C D E F G H'
            self.player_board = self.populate_board()
            self.guess_board = self.populate_board()
        elif size == 'L':
            self.dimensions = (5, 10)
            self.ships = 5
            self.letter_overlay = '  A B C D E F G H I J'
            self.player_board = self.populate_board()
            self.guess_board = self.populate_board()

    def populate_board(self):
        """
        Populates a board appropriately for the required size of the game.
        Creates key-value pairs, used for accessing coordinates during a game.
        Populates all values with W  - Representing the waves/empty positions.
        """
        board = {}
        numbers = ('1', '2', '3', '4', '5')
        # letters2 = string.ascii_uppercase
        letters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')
        # Will populate the given amount of rows and columns stored in dimensions.
        # Dimensions was set by game size.
        for number in range(self.dimensions[0]):
            for letter in range(self.dimensions[1]):
                board.update({f'{letters[letter]}{numbers[number]}': 'W'})
        return board

    def player_board_display(self):
        """        
        Displays a players board and their ship locations.    
        Also displayed will be the opponents hits and missed.            
        The board is stripped of all unwanted characters for display.
        """
        player_board = self.player_board
        display_board = []
        for item in player_board:
            display_board.append(player_board.get(item))
        print(self.letter_overlay)
        for num in range(self.dimensions[0]):
            rows = []
            rows.append(num + 1)
            for num in range(self.dimensions[1]):
                rows.append(display_board.pop(0))
            print(str(rows).strip('[').strip(']').replace(
                ',', '').replace("'", ''))
            rows.clear()

    def guess_board_display(self):
        """
        The guess board for an opponent.
        This board will contain all of a players's hits and misses.
        The board is stripped of all unwanted characters for display.
        """
        guess_board = self.guess_board
        display_board = []
        for item in guess_board:
            display_board.append(guess_board.get(item))
        print(self.letter_overlay)
        for num in range(self.dimensions[0]):
            rows = []
            rows.append(num + 1)
            for num in range(self.dimensions[1]):
                rows.append(display_board.pop(0))
            print(str(rows).strip('[').strip(']').replace(
                ',', '').replace("'", ''))
            rows.clear()

    def auto_ship_placements(self):
        """
        Sets random placements for all of a players ships.
        Will only place a ship where there is not one already placed.
        """
        player_board = self.player_board
        keys = []
        counter = 0
        while counter < self.ships:
            for item in player_board:
                keys.append(item)
            key = random.choice(keys)
            if self.player_board.get(key) != '^':
                counter += 1
                self.player_board.update({key: '^'})

    def invalid_coordinates(self, key):
        """
        Displays some help to the user when invalid coordinates are entered.
        """
        print(f"The coordinates '{key}' you entered are invalid !\n"
              'Please check your board for valid coordinates..\n'
              '\n'
              'Example below: All the coordinates from A1 to D2 are valid.\n')
        print('  A B C D\n'
              '1 W W W W\n'
              '2 W W W W\n')
        print('Coordinates must have the form of letter then number, as above.\n'
              'Letters are not case sensitive.')
        print('')

    def manual_ship_placement(self):
        """
        Manually place a player's ships to their desired coordinates.
        Raises a key error where an invalid key has been used as the coordinate.        
        Places the required number of ships for a game size.        
        """
        ship_number = 1
        counter = 0
        while counter < self.ships:
            try:
                wipe_terminal()
                self.player_board_display()
                print('')
                print(f'Enemy Ships: {self.ships}')
                print('')
                input_str = input(
                    f'Enter the coordinates for ship number {ship_number}.\n')
                key = input_str.upper()
                if key not in self.player_board:
                    raise KeyError
                if self.player_board.get(key) == '^':
                    wipe_terminal()
                    print(f'A ship is already at position {key}, silly ! \n')
                    input('Press Enter to try again.')
                else:
                    self.player_board.update({key: '^'})
                    ship_number += 1
                    counter += 1
            except KeyError:
                wipe_terminal()
                self.invalid_coordinates(key)
                input('Press Enter to try again.')
        wipe_terminal()
        print(self.player_board_display)

    def choose_ship_placement(self):
        """
        Choose auto or manual ship placements.
        Only accepts A or M or is recalled.
        """
        user_input = input(
            'Enter A for automatic ship placements / Enter M for manual ship placements\n'
        )
        user_input = user_input.upper()
        if user_input in ('A', 'M'):
            if user_input == 'A':
                self.auto_ship_placements()
            elif user_input == 'M':
                self.manual_ship_placement()
        else:
            wipe_terminal()
            self.choose_ship_placement()

