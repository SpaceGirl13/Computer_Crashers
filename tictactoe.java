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



