import os
from enum import Enum
from random import randrange


class GameState(Enum):
  RUNNING = 0
  WIN = 1
  DRAW = 2

class Player(Enum):
  COMPUTER = 0
  PLAYER = 1


# Represents the computer player
class Computer:
  # Returns the index of the computer's selected move
  def play(self, board):
    choice = randrange(9)

    while not self.space_available(choice, board):
      choice = randrange(9)
    
    return choice
  
  # Checks if a given board slot is unoccupied
  def space_available(self, slot_index, board):
    if slot_index <= 8 and slot_index >= 0 and board[slot_index] == " ":
      return True
    else:
      return False


# Represents the game board; manages turns, board state, and winner status
class Game:
  def __init__(self):
    self.game_state = GameState.RUNNING
    self.player = Player.COMPUTER # Player starts the game
    self.board = [
      " ", " ", " ",
      " ", " ", " ",
      " ", " ", " "
    ]
    self.computer = Computer()
  
  # Starts the game loop
  def start(self):
    while self.game_state == GameState.RUNNING:
      self.update()

  # Checks if either player has ended the game.
  # If not, play alternates to the next player
  def update(self):
    self.game_state = self.check_winner(self.board)
    self.paint_board()

    if self.game_state == GameState.WIN:
      if self.player == Player.PLAYER:
        print("Congratulations, you won!")
      elif self.player == Player.COMPUTER:
        print("You lost, better luck next time!")
    elif self.game_state == GameState.DRAW:
        print("Tie Game!")
    else:
      if self.player == Player.PLAYER:
        self.player = Player.COMPUTER
      else:
        self.player = Player.PLAYER
      self.run_turn()
  
  # Handles turns for both the player and computer
  def run_turn(self):
    # Players turn
    if self.player == Player.PLAYER:
      choice = int(input("Enter a position between [1-9]: ")) - 1 # Subtract 1 for 0-based indexing

      # Keep having the player input moves until one is valid
      while not self.space_available(choice):
        choice = int(input("Space not available, place enter again [1-9]: ")) - 1
      
      self.board[choice] = "X"
    
    elif self.player == Player.COMPUTER:
      choice = self.computer.play(self.board)

      if self.space_available(choice):
        self.board[choice] = "O"

  # Prints the Tic-Tac-Toe board
  def paint_board(self):
    os.system('clear')
    print(" %c | %c | %c " % (self.board[0], self.board[1], self.board[2]))
    print("___|___|___")
    print(" %c | %c | %c " % (self.board[3], self.board[4], self.board[5]))
    print("___|___|___")
    print(" %c | %c | %c " % (self.board[6], self.board[7], self.board[8]))
    print("   |   |   ")
  
  # Checks if a given board slot is unoccupied
  def space_available(self, slot_index):
    if slot_index <= 8 and slot_index >= 0 and self.board[slot_index] == " ":
      return True
    else:
      return False
  
  # Returns whether the game has been ended
  def check_winner(self, board):
    # Horizontal Win Conditions    
    if (
      board[0] == board[1] and 
      board[1] == board[2] and 
      board[0] != ' '
    ):    
      return GameState.WIN
    elif (
      board[3] == board[4] and
      board[4] == board[5] and
      board[3] != ' '
    ):    
        return GameState.WIN
    elif (
      board[6] == board[7] and
      board[7] == board[8] and
      board[6] != ' '
    ):    
      return GameState.WIN
    
    # Vertical Win Conditions 
    elif (
      board[0] == board[3] and
      board[3] == board[6] and
      board[0] != ' '
    ):    
      return GameState.WIN
    elif (
      board[1] == board[4] and
      board[4] == board[7] and
      board[1] != ' '
    ):    
      return GameState.WIN
    elif (
      board[2] == board[5] and
      board[5] == board[8] and
      board[2] != ' '
    ):    
      return GameState.WIN
    
    # Diagonal Win Conditions    
    elif (
      board[1] == board[4] and
      board[4] == board[8] and
      board[4] != ' '
    ):    
      return GameState.WIN
    elif (
      board[2] == board[4] and
      board[4] == board[6] and
      board[4] != ' '
    ):    
      return GameState.WIN
    
    # Draw Conditions    
    elif (
      board[0] != ' ' and
      board[1] != ' ' and
      board[2] != ' ' and
      board[3] != ' ' and
      board[4] != ' ' and
      board[5] != ' ' and
      board[6] != ' ' and
      board[7] != ' ' and
      board[8] != ' '
    ):
      return GameState.DRAW
    
    else:            
       return GameState.RUNNING


if __name__ == "__main__":
  game = Game()
  game.start()
