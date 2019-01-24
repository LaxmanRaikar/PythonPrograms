
from utilities import utility


def tic_tac_toe():
  end = False
  while not end:
    utility.draw()
    end = utility.check_board()

    print("Player 1 choose where to place a cross")
    utility.p1()
    print()
    utility.draw()
    end = utility.check_board()
    if end == True :
        break

    print("Player 2 choose where to place a nought")
    utility.p2()
    print()

tic_tac_toe()