"""
"""
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

    def create_board(self):
        """
        Create a board with attributes ranging from small to large.        
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
