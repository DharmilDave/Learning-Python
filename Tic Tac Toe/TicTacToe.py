board = [' ' for x in range(10)]


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


def printBoard(board):
    print('       |   |')
    print('      ' + board[1] + '| ' + board[2] + ' | ' + board[3])
    print('       |   |')
    print('-------------------')
    print('       |   |')
    print('      ' + board[4] + '| ' + board[5] + ' | ' + board[6])
    print('       |   |')
    print('-------------------')
    print('       |   |')
    print('      ' + board[7] + '| ' + board[8] + ' | ' + board[9])
    print('       |   |')


def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le)


def playerMove():
    run = True
    while run:
        move = input("Select a position between (1-9) to put 'X' ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter("X", move)
                else:
                    print("Space is already occupied!")
            else:
                print("Out of range number!")
        except:
            print("Please provide a number!")


def compMove():
    possibleMoves = [x for x, letter in enumerate(
        board) if letter == " " and x != 0]
    move = 0

    for let in ["O", "X"]:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornerOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornerOpen.append(i)

    if len(cornerOpen) > 0:
        move = selectRandom(cornerOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move


def selectRandom(li):
    import random
    r = random.randrange(0, len(li))
    return li[r]


def isBoardFull(board):
    if board.count(" ") > 1:
        return False
    else:
        return True


def main():
    print("Welcome to Tic Tac Toe Game :)")
    print("I'll be playing as 'O' and You are 'X'")
    printBoard(board)

    while not (isBoardFull(board)):
        if not (isWinner(board, 'O')):
            playerMove()
            printBoard(board)

        else:
            print("oops!! I won..")
            break

        if not (isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print("Game is Tie")
                break
            else:
                insertLetter("O", move)
                print("I've Put 'O' at position: ", move)
                printBoard(board)

        else:
            print("Great You won..")
            break


i = 0
while True:
    if i == 0:
        main()
        i += 1
    ans = input("Would you like to play again? (Y/N)")
    if ans.lower() == "y" or ans.lower() == "yes":
        board = [' ' for x in range(10)]
        main()
    else:
        break
