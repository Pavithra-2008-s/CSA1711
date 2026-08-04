N = 8

board = [[0] * N for _ in range(N)]

def is_safe(row, col):

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(row):

    if row == N:
        return True

    for col in range(N):

        if is_safe(row, col):

            board[row][col] = 1

            if solve(row + 1):
                return True

            board[row][col] = 0

    return False


solve(0)

for row in board:
    print(row)
