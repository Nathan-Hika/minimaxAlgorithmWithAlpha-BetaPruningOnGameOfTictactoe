board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}
player = 'O'
computer = 'X'

def printBoard(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("\n")

def spaceIsFree(position):
    if board[position] == ' ':
        return True
    return False

def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if checkDraw():
            print("Draw!")
            exit()
        if checkWin():
            if letter == 'X':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()
        return
    else:
        print("Invalid position")
        position = int(input("Please enter a new position: "))
        insertLetter(letter, position)
        return

def checkWin():
    if (board[1] == board[2] == board[3] != ' ' or
        board[4] == board[5] == board[6] != ' ' or
        board[7] == board[8] == board[9] != ' ' or
        board[1] == board[4] == board[7] != ' ' or
        board[2] == board[5] == board[8] != ' ' or
        board[3] == board[6] == board[9] != ' ' or
        board[1] == board[5] == board[9] != ' ' or
        board[7] == board[5] == board[3] != ' '):
        return True
    return False

def checkDraw():
    for key in board:
        if board[key] == ' ':
            return False
    return True

def playerMove():
    position = int(input("Enter a position for 'O': "))
    insertLetter(player, position)
    return

def compMove():
    bestScore = float('-inf')
    bestMove = None
    for key in board:
        if board[key] == ' ':
            board[key] = computer
            score = minimax(board, False, float('-inf'), float('inf'))
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key
    insertLetter(computer, bestMove)
    return

def minimax(board, isMaximizing, alpha, beta):
    scores = {'X': 1, 'O': -1, 'draw': 0}

    if checkWin():
        if isMaximizing:
            return scores[computer]
        else:
            return scores[player]

    if checkDraw():
        return scores['draw']

    if isMaximizing:
        maxScore = float('-inf')
        for key in board:
            if board[key] == ' ':
                board[key] = computer
                score = minimax(board, False, alpha, beta)
                board[key] = ' '
                maxScore = max(maxScore, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return maxScore

    else:
        minScore = float('inf')
        for key in board:
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, True, alpha, beta)
                board[key] = ' '
                minScore = min(minScore, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return minScore

while True:
    playerMove()
    compMove()