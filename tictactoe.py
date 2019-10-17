#tictactoe
"""
Created by : Anuranjan Kumar pandey
Date : 18/10/2019

"""

def displayBoard(board):
    for row in board:
        print()
        for col in row:
            print(col, end=' ')
    print()


def updateBoard(r, c, sym, board):
    if r < 0 or r >= len(board):
        return False
    elif c < 0 or c>= len(board[r]):
        return False
    elif board[r][c] != '[ ]':
        return False

    board[r][c] = '[' + sym + ']'
    return True


def isFull(board):
    for row in board:
        for col in row:
            if col == '[ ]':
                return False
    return True


def checkWins(board, sym):
    sym = '[' + sym + ']'

    # Row check
    i = 0
    while i < 3:
        if board[i][0] == sym and board[i][1] == sym and board[i][2] == sym:
            return True
        i += 1

    # Col check
    i = 0
    while i < 3:
        if board[0][i] == sym and board[1][i] == sym and board[2][i] == sym:
            return True
        i += 1

    # Diagonal check
    if board[0][0] == sym and board[1][1] == sym and board[2][2] == sym:
        return True

    # Reverse diagonal check
    if board[0][2] == sym and board[1][1] == sym and board[2][0] == sym:
        return True

    return False


def tictactoe():
    board = [['[ ]']*3, ['[ ]']*3, ['[ ]']*3]
    players = []
    symbols = ['X','O']

    players.append(input('Enter name of Player1 : '))
    players.append(input('Enter name of Player2 : '))

    i = 0
    while i < 2:
        print( 'Symbols of ' + players[i] + ' is ' + symbols[i])
        i += 1

    i = 0
    flag = 1

    while not isFull(board):
        displayBoard(board)
        print( players[i] + ' (' + symbols[i] + ') ' + 'plays :')
        r = int(input("Enter row (0 - 2) :"))
        c = int(input("Enter col (0 - 2) :"))

        if updateBoard(r, c, symbols[i], board):
            if checkWins(board, symbols[i]):
                displayBoard(board)
                print(players[i] + ' (' + symbols[i] + ') '+ 'Wins !!!')
                flag = 0
                break
            i = (i +1)%2 # Switch Players
        else:
            print('Invalid Move.')

    if flag == 1:
        displayBoard(board)
        print('Game Draw !!!')


def main():
    tictactoe()


main()
