
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    chessboard = []
    for _ in range(n):
        row = list(map(int, input().split()))
        chessboard.append(row)

    max_sum = 0

    # Calculate the maximal sum for each bishop position
    for i in range(n):
        for j in range(m):
            diagonal_sum = chessboard[i][j]

            # Calculate the sum in the top-left direction
            x, y = i - 1, j - 1
            while x >= 0 and y >= 0:
                diagonal_sum += chessboard[x][y]
                x -= 1
                y -= 1

            # Calculate the sum in the top-right direction
            x, y = i - 1, j + 1
            while x >= 0 and y < m:
                diagonal_sum += chessboard[x][y]
                x -= 1
                y += 1

            # Calculate the sum in the bottom-left direction
            x, y = i + 1, j - 1
            while x < n and y >= 0:
                diagonal_sum += chessboard[x][y]
                x += 1
                y -= 1

            # Calculate the sum in the bottom-right direction
            x, y = i + 1, j + 1
            while x < n and y < m:
                diagonal_sum += chessboard[x][y]
                x += 1
                y += 1

            max_sum = max(max_sum, diagonal_sum)

    print(max_sum)

