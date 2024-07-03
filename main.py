print("Welcome to Tic-Tac-Toe")
print("Here is our playing board:")

# Constants
EMPTY_CELL = ' '
BOARD_SIZE = 3

# The play board
play_board = [[EMPTY_CELL for _ in range(BOARD_SIZE)]
              for _ in range(BOARD_SIZE)]

def evaluate_utility(board):
    # Function to evaluate the utility of the current board state
    # Check rows for a win
    for row in board:
        if row.count('X') == 3:  # Human player wins
            return -1
        elif row.count('O') == 3:  # AI player wins
            return 1

    # Check columns for a win
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'X':
                return -1
            elif board[0][col] == 'O':
                return 1

    # Check diagonals for a win
    if (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]):
        if board[1][1] == 'X':
            return -1
        elif board[1][1] == 'O':
            return 1

    # Check for a draw
    if all(cell != ' ' for row in board for cell in row):
        return 0  # It's a draw

    # If none of the above conditions are met, the game is still in progress
    return None

def is_terminal_state(board):
    # Check for a draw or a win
    return evaluate_utility(board) is not None

def minimax_ab(board, alpha, beta, is_maximizer_turn):
    raise NotImplementedError

def find_best_move(board):
    best_val = float('-inf')
    best_move = (-1, -1)

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == EMPTY_CELL:
                board[i][j] = 'O'  # AI makes a move
                move_val = minimax_ab(board, float('-inf'), float('inf'), False)
                board[i][j] = EMPTY_CELL  # Undo the move

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Prints the board
def print_board():
    print("   1  2  3")
    for i in range(BOARD_SIZE):
        print(i + 1, end=" ")
        for j in range(BOARD_SIZE):
            print("[" + play_board[i][j] + "]", end="")  # print elements without new line
        print()  # print empty line after each row
    print('--------------')

def get_player_input(player):
    while True:
        try:
            position = input(f'{player}, Enter play position (i.e. 1,1): ')
            x, y = map(int, position.split(','))
            if x in range(1, BOARD_SIZE + 1) and y in range(1, BOARD_SIZE + 1) and play_board[x-1][y-1] == EMPTY_CELL:
                return x-1, y-1  # Adjust for zero-based indexing
            else:
                print("Invalid input or position is not empty. Please enter row and column numbers between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter row and column numbers between 1 and 3.")

def play(player, row, col):
    if play_board[row][col] == EMPTY_CELL:
        play_board[row][col] = player
        print_board()
        return True
    else:
        print("Position is not empty. Please try again.")
        return False

def main():
    while True:
        # Player X's turn
        while True:
            pos_x, pos_y = get_player_input('X')
            if play('X', pos_x, pos_y):
                break

        if is_terminal_state(play_board):
            break

        # AI (Player O's) turn
        pos_O_x, pos_O_y = find_best_move(play_board)
        play('O', pos_O_x, pos_O_y)

        if is_terminal_state(play_board):
            break

    winner = evaluate_utility(play_board)
    if winner == 0:
        print("The game is a tie!")
    elif winner == 1:
        print("O wins!")
    else:
        print("X wins!")

if __name__ == '__main__':
    main()
