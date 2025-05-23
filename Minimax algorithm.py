PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = '.'

def printBoard(board):
    for row in board:
        print(" ".join(row))
    print()

def isMovesLeft(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return True
    return False

def evaluate(b):
    for row in range(3):
        if b[row][0] == b[row][1] and b[row][1] == b[row][2]:
            if b[row][0] == PLAYER_X:
                return 10
            elif b[row][0] == PLAYER_O:
                return -10

    for col in range(3):
        if b[0][col] == b[1][col] and b[1][col] == b[2][col]:
            if b[0][col] == PLAYER_X:
                return 10
            elif b[0][col] == PLAYER_O:
                return -10

    if b[0][0] == b[1][1] and b[1][1] == b[2][2]:
        if b[0][0] == PLAYER_X:
            return 10
        elif b[0][0] == PLAYER_O:
            return -10

    if b[0][2] == b[1][1] and b[1][1] == b[2][0]:
        if b[0][2] == PLAYER_X:
            return 10
        elif b[0][2] == PLAYER_O:
            return -10

    return 0

def minimax(board, depth, isMax):
    score = evaluate(board)

    if score == 10:
        return score - depth
    
    if score == -10:
        return score + depth

    if not isMovesLeft(board):
        return 0

    if isMax:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    best = max(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = EMPTY
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    best = min(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = EMPTY
        return best

def findBestMove(board):
    bestVal = -1000
    bestMove = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                moveVal = minimax(board, 0, False)
                board[i][j] = EMPTY
                if moveVal >= bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal
    return bestMove

if __name__ == "__main__":
    board = [
        [PLAYER_X, PLAYER_O, PLAYER_X],
        [PLAYER_O, PLAYER_X, EMPTY],
        [EMPTY, PLAYER_O, PLAYER_X]
    ]

    print("Current Board:")
    printBoard(board)

    move = findBestMove(board)
    print(f"Best Move: {move}")

    if move != (-1, -1):
        board[move[0]][move[1]] = PLAYER_X
        print("\nBoard after best move:")
        printBoard(board)
    else:
        print("No moves left or game over.")
