from board import Board
def acceptBoardSize():
    minBoardSize = 3
    boardSize = None
    while boardSize is None:
        boardSize = int(input("Enter board size (>=3): "))
        if boardSize < minBoardSize:
            boardSize = None

    return boardSize

if __name__ == "__main__":
    # Create board
    boardSize = acceptBoardSize()
    board = Board(boardSize)

    player = 1
    while True:
        board.display()

        winner = board.winner()
        if winner is not None:
            print("Player {} won.".format(winner))
            break

        tie = board.tie()
        if tie is True:
            print("Match Tied")
            break
        
        # Take input from player
        while True:
            position = input("Choose next position. [Player {}]: ".format(player))
            if board.update(position, player):
                player += 1
                if player > 2:
                    player = 1
                break



    