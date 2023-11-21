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
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

def checkWhichMarkWon(mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False

def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False 
    return True 

def playerMove():
    position = int(input("Enter a position for 'O': "))
    insertLetter(player, position)
    return 

def compMove():
    bestScore = -800
    bestMove = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = computer
            score = minimax(board, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score 
                bestMove = key
    insertLetter(computer, bestMove)
    return 
def heuristic(board):
    # Calculate the heuristic value based on the board state
    # For example, assign scores based on the number of potential winning lines for each player
    heuristic_value = 0

    # Check for potential winning lines for the computer
    for i in range(1, 4):
        if board[i] == board[i + 3] == board[i + 6] == computer or board[i] == board[i + 3] == board[i + 6] == player:
            if board[i] == computer:
                heuristic_value += 10
            else:
                heuristic_value -= 10

    # Check for potential winning lines for the player
    for i in range(1, 4):
        if board[i] == board[i + 3] == board[i + 6] == player or board[i] == board[i + 3] == board[i + 6] == computer:
            if board[i] == player:
                heuristic_value -= 10
            else:
                heuristic_value += 10

    # Check for potential corners for the computer
    if board[1] == computer or board[9] == computer:
        heuristic_value += 5
    if board[3] == computer or board[7] == computer:
        heuristic_value += 4

    # Check for potential corners for the player
    if board[1] == player or board[9] == player:
        heuristic_value -= 5
    if board[3] == player or board[7] == player:
        heuristic_value -= 4

    return heuristic_value

# Modified minimax function to incorporate heuristic evaluation
def minimax(board, isMaximizing):
    if checkWin():
        return heuristic(board)

    if isMaximizing:
        bestScore = -1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = computer
                score = minimax(board, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore
    else:
        bestScore = 1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, True)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore
while not checkWin():
    compMove()
    playerMove()
    exit()