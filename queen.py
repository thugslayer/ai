def is_safe(board, row, col, n):
    #column
    for i in range(row):
        if board[i][col] == 1:
            return False

    #left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    #right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(board, row, n, solutions):
    if row == n:
        solution = []
        for r in board:
            solution.append(''.join(['Q' if x == 1 else '.' for x in r]))
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n, solutions)
            board[row][col] = 0  

def n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens(board, 0, n, solutions)
    return solutions

n = int(input("Enter the value of N (number of queens): "))
solutions = n_queens(n)

print(f"\nNumber of solutions: {len(solutions)}\n")
for i, sol in enumerate(solutions, start=1):
    print(f"Solution #{i}:")
    for row in sol:
        print(row)
    print()
