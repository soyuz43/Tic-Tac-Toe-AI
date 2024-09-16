# tictactoe.py

import random

# Create the game board (3x3)
board = [' ' for _ in range(9)]  # A list of 9 empty spaces

# Display the board
def print_board():
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Check if the game has been won
def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_conditions)

# Check if the game is a draw
def check_draw():
    return ' ' not in board

# Make a move
def make_move(position, player):
    if board[position] == ' ':
        board[position] = player
        return True
    return False

# Reset the board
def reset_board():
    global board
    board = [' ' for _ in range(9)]

# Minimax algorithm to determine the best move
def minimax(player):
    opponent = 'O' if player == 'X' else 'X'
    
    # Base case: check for terminal states (win, lose, or draw)
    if check_win('O'):
        return {'position': None, 'score': 1 * (len([i for i in board if i == ' ']) + 1)}
    elif check_win('X'):
        return {'position': None, 'score': -1 * (len([i for i in board if i == ' ']) + 1)}
    elif check_draw():
        return {'position': None, 'score': 0}
    
    moves = []
    
    # Loop through all empty spots
    for i in range(9):
        if board[i] == ' ':
            # Try the move
            board[i] = player
            move = {}
            move['position'] = i
            
            # Recursively call minimax for the other player
            if player == 'O':
                result = minimax('X')
                move['score'] = result['score']
            else:
                result = minimax('O')
                move['score'] = result['score']
            
            # Undo the move
            board[i] = ' '
            
            # Add move to list of possible moves
            moves.append(move)
    
    # Pick the best move
    if player == 'O':  # AI is 'O', wants to maximize
        best_score = -float('inf')
        best_move = None
        for move in moves:
            if move['score'] > best_score:
                best_score = move['score']
                best_move = move
        return best_move
    else:  # Opponent is 'X', wants to minimize
        best_score = float('inf')
        best_move = None
        for move in moves:
            if move['score'] < best_score:
                best_score = move['score']
                best_move = move
        return best_move

def play_game():
    reset_board()
    print("Welcome to Tic-Tac-Toe!")
    print_board()
    
    while True:
        # Human move
        position = int(input("Enter your move (1-9): ")) - 1
        if not make_move(position, 'X'):
            print("Invalid move. Try again.")
            continue
        
        print_board()
        
        # Check for human win
        if check_win('X'):
            print("Congratulations! You win!")
            break
        if check_draw():
            print("It's a draw!")
            break
        
        # AI move
        print("AI is making its move...")
        ai_move = minimax('O')
        make_move(ai_move['position'], 'O')
        print_board()
        
        # Check for AI win
        if check_win('O'):
            print("The AI wins!")
            break
        if check_draw():
            print("It's a draw!")
            break

# Play the game
if __name__ == "__main__":
    play_game()
