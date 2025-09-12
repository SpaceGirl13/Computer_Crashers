class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        
# Let's test it by creating some players
player1 = Player("Peppa", "X")
player2 = Player("George", "O")

print(f"Player 1: {player1.name} uses symbol '{player1.symbol}'")
print(f"Player 2: {player2.name} uses symbol '{player2.symbol}'")