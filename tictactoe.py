#tictactoe


def displayBoard(board):
    for row in board:
        print()
        for col in row:
            print(col, end=' ')
    print()


def updateBoard(r, c, sym, board):
    if r < 0 and r >= len(board):
        return False
    elif c < 0 and c >= len(board[r]):
        return False
    elif board[r][c] != '[ ]':
        return False

    board[r][c] = '[' + sym + ']'
    return True


def tictactoe():
    board = [['[ ]']*3, ['[ ]']*3, ['[ ]']*3]
    displayBoard(board)
    updateBoard(1, 1, 'X', board)
    displayBoard(board)


def main():
    tictactoe()


main()
