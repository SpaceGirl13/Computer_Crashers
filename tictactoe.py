class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
player1 = Player("Peppa", "X")
player2 = Player("George", "O")
print(f"Player 1: {player1.name} uses symbol '{player1.symbol}'")
print(f"Player 2: {player2.name} uses symbol '{player2.symbol}'")
class Board:
    def __init__(self):
        self.grid = [" "] * 9 
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
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
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
board = Board()
print("Setting up a winning scenario...")
board.make_move(1, "X") 
board.make_move(2, "X") 
board.make_move(3, "X") 

board.display()
is_winner = board.check_winner("X")
print(f"Is X the winner? {is_winner}")

