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
