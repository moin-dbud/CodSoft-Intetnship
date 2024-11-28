def print_board(board):
    """
    Prints the Tic-Tac-Toe board.
    """
    for row in board:
        print("|".join(row))
    print()


def is_moves_left(board):
    """
    Checks if there are any moves left on the board.
    """
    for row in board:
        if " " in row:
            return True
    return False


def check_winner(board, player):
    """
    Checks if the given player has won the game.
    """
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def minimax(board, depth, is_maximizing, alpha=-float('inf'), beta=float('inf')):
    """
    Implements the Minimax algorithm with Alpha-Beta Pruning.
    """
    if check_winner(board, "O"):  # AI's symbol
        return 10 - depth
    if check_winner(board, "X"):  # Human's symbol
        return depth - 10
    if not is_moves_left(board):  # Draw
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval


def find_best_move(board):
    """
    Finds the best move for the AI using the Minimax algorithm.
    """
    best_val = -float('inf')
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_val = minimax(board, 0, False)
                board[i][j] = " "
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
    return best_move


def player_move(board):
    """
    Allows the human player to make a move.
    """
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            x, y = divmod(move, 3)
            if board[x][y] == " ":
                board[x][y] = "X"
                break
            else:
                print("Square already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid move. Enter a number between 1 and 9.")


def play_game():
    """
    The main function to play the Tic-Tac-Toe game.
    """
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are 'X'.")
    print("The board positions are as follows:")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")
    print_board(board)

    while True:
        # Player move
        player_move(board)
        print_board(board)
        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break
        if not is_moves_left(board):
            print("It's a draw!")
            break

        # AI move
        print("AI is making its move...")
        x, y = find_best_move(board)
        board[x][y] = "O"
        print_board(board)
        if check_winner(board, "O"):
            print("AI wins! Better luck next time.")
            break
        if not is_moves_left(board):
            print("It's a draw!")
            break


# Run the game
if __name__ == "__main__":
    play_game()
