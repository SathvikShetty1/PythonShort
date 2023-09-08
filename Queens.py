def is_safe(board, row, col, n):
    # Check the column on top
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    def solve(row):
        if row == n:
            for row in board:
                print(" ".join(["Q" if cell == 1 else "." for cell in row]))
            print()
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                solve(row + 1)
                board[row][col] = 0

    solve(0)
    
n = int(input("Enter the no of queens "))
solve(n)
"""
Enter no of Queens: 4
. . Q . 
Q . . . 
. . . Q 
. Q . . 

. Q . . 
. . . Q 
Q . . . 
. . Q . 
"""
