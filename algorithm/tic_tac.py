"""
this program is used  to play tic tac toe game with the computer
author:Laxman Raikar
since:8 JAN,2019
"""
from utilities import utility


def tic_tac_toe():

  end = False
  while not end:
    utility.draw()          # calls the method
    end = utility.check_board()   # calls the method

    print("Player 1 choose where to place a cross")
    utility.p1()                  # calls the method
    print()                     # prints the empty line
    utility.draw()              # calls the method
    end = utility.check_board()    # calls the method
    if end == True:
        break

    print("Player 2 choose where to place a nought")
    utility.p2()                        # calls the method
    print()

if __name__ == "__main__":
  tic_tac_toe()