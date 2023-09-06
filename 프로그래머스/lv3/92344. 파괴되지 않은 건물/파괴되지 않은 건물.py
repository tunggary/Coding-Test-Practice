def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    sum_board = [[0]*(m+1) for _ in range(n+1)]

    for t, r1, c1, r2, c2, degree in skill:
        sum_board[r1][c1] += degree if t == 2 else (-1) * degree
        sum_board[r1][c2 + 1] += degree if t == 1 else (-1) * degree
        sum_board[r2 + 1][c1] += degree if t == 1 else (-1) * degree
        sum_board[r2 + 1][c2 + 1] += degree if t == 2 else (-1) * degree

    for i in range(n):
        for j in range(m):
            sum_board[i][j+1] += sum_board[i][j]

    for i in range(n):
        for j in range(m):
            sum_board[i+1][j] += sum_board[i][j]

    for i in range(n):
        for j in range(m):
            if board[i][j] + sum_board[i][j] > 0:
                answer += 1

    return answer