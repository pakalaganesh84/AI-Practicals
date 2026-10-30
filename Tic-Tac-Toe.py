board = [" "] * 9

def display():
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()

def winner(player):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True

    return False

def minimax(is_max, alpha, beta):

    if winner("O"):
        return 1

    if winner("X"):
        return -1

    if " " not in board:
        return 0

    if is_max:
        best = -100

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False, alpha, beta)
                board[i] = " "

                best = max(best, score)
                alpha = max(alpha, best)

                if beta <= alpha:
                    break

        return best

    else:
        best = 100

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True, alpha, beta)
                board[i] = " "

                best = min(best, score)
                beta = min(beta, best)

                if beta <= alpha:
                    break

        return best

def ai_move():
    best_score = -100
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False, -100, 100)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    if move != -1:
        board[move] = "O"

print("TIC TAC TOE")
print("You are X and Computer is O")

while True:
    display()

    pos = int(input("Enter position (1-9): ")) - 1

    if pos < 0 or pos > 8 or board[pos] != " ":
        print("Invalid position! Try again.")
        continue

    board[pos] = "X"

    if winner("X"):
        display()
        print("You Win!")
        break

    if " " not in board:
        display()
        print("Game Draw!")
        break

    ai_move()
    print("Computer played.")

    if winner("O"):
        display()
        print("Computer Wins!")
        break

    if " " not in board:
        display()
        print("Game Draw!")
        break
