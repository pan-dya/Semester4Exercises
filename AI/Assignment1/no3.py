import math

class TicTacToe():
    def __init__(self, state=None):
        if state is None:
            self.state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        else:
            self.state = state

    def make_move(self, row, col, val):
        if self.state[row][col] == 0:
            self.state[row][col] = val
            return True
        else:
            return False

    def expand_node(self, val):
        children = []
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    new_state = [row[:] for row in self.state]
                    new_state[i][j] = val
                    children.append(new_state)
        return children

    def is_winner(self, val):
        for i in range(3):
            if all(self.state[i][j] == val for j in range(3)) or all(self.state[j][i] == val for j in range(3)):
                return True
        if all(self.state[i][i] == val for i in range(3)) or all(self.state[i][2 - i] == val for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(self.state[i][j] != 0 for i in range(3) for j in range(3))

    def is_game_over(self):
        return self.is_winner(1) or self.is_winner(-1) or self.is_draw()

def minimax(node, depth, maximizing_player):
    if node.is_game_over() or depth == 0:
        if node.is_winner(-1):
            return -10
        elif node.is_winner(1):
            return 10
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for child in node.expand_node(1):
            eval = minimax(TicTacToe(child), depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for child in node.expand_node(-1):
            eval = minimax(TicTacToe(child), depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(node):
    best_eval = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if node.state[i][j] == 0:
                node.state[i][j] = 1
                eval = minimax(TicTacToe(node.state), 2, False)  # You can adjust the depth for a stronger/weaker AI
                node.state[i][j] = 0
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

def print_board(board):
    for row in board:
        print(" ".join(["X" if cell == 1 else "O" if cell == -1 else "." for cell in row]))

def main():
    game = TicTacToe()
    while not game.is_game_over():
        print_board(game.state)
        player_row = int(input("Enter the row (0, 1, 2): "))
        player_col = int(input("Enter the column (0, 1, 2): "))
        
        if game.make_move(player_row, player_col, -1):
            if game.is_game_over():
                break
            print("Player's move:")
            print_board(game.state)
            
            computer_move = best_move(game)
            game.make_move(computer_move[0], computer_move[1], 1)
            print("Computer's move:")
            print_board(game.state)
    
    print("Game over!")
    if game.is_winner(-1):
        print("Player wins!")
    elif game.is_winner(1):
        print("Computer wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
