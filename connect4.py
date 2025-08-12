import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A","B","C","D","E","F","G"]
gameBoard = [["" for _ in range(7)] for _ in range(6)]
rows = 6
cols = 7

def printGameBoard():
    print("\n     A    B    C    D    E    F    G  ", end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x+1, " |", end="")  # Row number 1-based
        for y in range(cols):
            if gameBoard[x][y] == "🔵":
                print(" 🔵 ", end=" |")
            elif gameBoard[x][y] == "🔴":
                print(" 🔴 ", end=" |")
            else:
                print("    ", end=" |")
    print("\n   +----+----+----+----+----+----+----+")

def modifyTurn(col, turn):
    # col is 0-based index of column
    for row in reversed(range(rows)):  # Bottom to top
        if gameBoard[row][col] == "":
            gameBoard[row][col] = turn
            return True
    return False  # Column full

def checkWin(turn):
    # Horizontal check
    for r in range(rows):
        for c in range(cols - 3):
            if all(gameBoard[r][c+i] == turn for i in range(4)):
                return True
    # Vertical check
    for c in range(cols):
        for r in range(rows - 3):
            if all(gameBoard[r+i][c] == turn for i in range(4)):
                return True
    # Diagonal /
    for r in range(3, rows):
        for c in range(cols - 3):
            if all(gameBoard[r - i][c + i] == turn for i in range(4)):
                return True
    # Diagonal \
    for r in range(rows - 3):
        for c in range(cols - 3):
            if all(gameBoard[r + i][c + i] == turn for i in range(4)):
                return True
    return False

turnCounter = 0
players = ["🔵", "🔴"]

while True:
    printGameBoard()
    currentPlayer = players[turnCounter % 2]
    print(f"\nPlayer {currentPlayer}, choose a column (A-G): ", end="")
    choice = input().upper()

    if choice not in possibleLetters:
        print("Invalid column. Try again.")
        continue

    colIndex = possibleLetters.index(choice)
    if not modifyTurn(colIndex, currentPlayer):
        print("Column full! Try another column.")
        continue

    if checkWin(currentPlayer):
        printGameBoard()
        print(f"\nPlayer {currentPlayer} wins! Congratulations!")
        break

    turnCounter += 1

    if turnCounter == rows * cols:
        printGameBoard()
        print("\nIt's a draw!")
        break