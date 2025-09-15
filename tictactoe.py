

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        
# Let's test it by creating some players
player1 = Player("Peppa", "X")
player2 = Player("George", "O")
print(f"Player 1: {player1.name} uses symbol '{player1.symbol}'")
print(f"Player 2: {player2.name} uses symbol '{player2.symbol}'")

class Board:
    def __init__(self):
        self.grid = [" "] * 9  # Creates 9 empty spaces
        print("New board created!")
        print(f"Grid contents: {self.grid}")
    def display(self):
        print("\n")
        print(" " + self.grid[0] + " | " + self.grid[1] + " | " + self.grid[2])
        print("---+---+---")
        print(" " + self.grid[3] + " | " + self.grid[4] + " | " + self.grid[5])
        print("---+---+---")
        print(" " + self.grid[6] + " | " + self.grid[7] + " | " + self.grid[8])
        print("\n")
    def display_reference(self):
        reference = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        print("Board positions:\n")
        print(" " + reference[0] + " | " + reference[1] + " | " + reference[2])
        print("---+---+---")
        print(" " + reference[3] + " | " + reference[4] + " | " + reference[5])
        print("---+---+---")
        print(" " + reference[6] + " | " + reference[7] + " | " + reference[8])
        print("\n")
    def make_move(self, position, symbol):
        index = position - 1
        if 0 <= index <= 8 and self.grid[index] == " ":
            self.grid[index] = symbol
            return True
        return False
    def check_winner(self, symbol):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        print(f"Checking for winner with symbol '{symbol}'")
        print(f"Win combinations to check: {win_combinations}")
        for combo in win_combinations:
            if (self.grid[combo[0]] == symbol and
                self.grid[combo[1]] == symbol and
                self.grid[combo[2]] == symbol):
                print(f"WINNER! Found winning combination: {combo}")
                return True
        print("No winner found")
        return False

# Test win detection
board = Board()
print("Setting up a winning scenario...")
board.make_move(1, "X")  # Top left
board.make_move(2, "X")  # Top middle  
board.make_move(3, "X")  # Top right - should be a win!

board.display()
is_winner = board.check_winner("X")
<<<<<<< HEAD
print(f"Is X the winner? {is_winner}")
=======
print("Is X the winner? {is_winner}")
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

class Board:
    def __init__(self):
        self.grid = [" "] * 9

    def display(self):
        print("\n")
        print(" " + self.grid[0] + " | " + self.grid[1] + " | " + self.grid[2])
        print("---+---+---")
        print(" " + self.grid[3] + " | " + self.grid[4] + " | " + self.grid[5])
        print("---+---+---")
        print(" " + self.grid[6] + " | " + self.grid[7] + " | " + self.grid[8])
        print("\n")

    def display_reference(self):
        reference = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        print("Board positions:\n")
        print(" " + reference[0] + " | " + reference[1] + " | " + reference[2])
        print("---+---+---")
        print(" " + reference[3] + " | " + reference[4] + " | " + reference[5])
        print("---+---+---")
        print(" " + reference[6] + " | " + reference[7] + " | " + reference[8])
        print("\n")

    def is_full(self):
        return " " not in self.grid

    def make_move(self, position, symbol):
        index = position - 1
        if index < 0 or index > 8:
            print("Invalid position. Choose a number between 1 and 9.")
            return False
        if self.grid[index] != " ":
            print("That spot is already taken. Try again.")
            return False
        self.grid[index] = symbol
        return True

    def check_winner(self, symbol):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for combo in win_combinations:
            if (self.grid[combo[0]] == symbol and
                self.grid[combo[1]] == symbol and
                self.grid[combo[2]] == symbol):
                return True
        return False

class TicTacToe:
    def __init__(self, player1, player2):
        self.board = Board()              # Composition: TicTacToe "has-a" Board
        self.players = [player1, player2] # Stores both players
        self.current_player = player1     # Tracks whose turn it is

    def switch_player(self):
        # Alternate between the two players
        self.current_player = (
            self.players[1] if self.current_player == self.players[0] else self.players[0]
        )
        print(f"Now it's {self.current_player.name}'s turn")

# Test the TicTacToe class setup
player1 = Player("Peppa", "X")
player2 = Player("George", "O")
game = TicTacToe(player1, player2)
def main():
    print("Welcome to Tic-Tac-Toe!\n")

    # Create players
    name1 = input("Enter name for Player 1 (X): ")
    name2 = input("Enter name for Player 2 (O): ")
    player1 = (name1, "X")
    player2 = (name2, "O")

    while True:
        # Set up the game
        game = TicTacToe(player1, player2)
        game.board.display_reference()
        game.board.display()

        while True:
            try:
                move = int(input(f"{game.current_player.name} ({game.current_player.symbol}), enter your move (1-9): "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if not game.board.make_move(move, game.current_player.symbol):
                continue

            game.board.display()

            if game.board.check_winner(game.current_player.symbol):
                print(f"🎉 {game.current_player.name} wins!")
                if isinstance(game.current_player,):
                    game.current_player.add_win()
                break

            if game.board.is_full():
                print("It's a draw!")
                break

            game.switch_player()

        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

# Run the game
if __name__ == "__main__": 
    main()