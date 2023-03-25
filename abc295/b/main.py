# 入力を読み込む
R, C = map(int, input().split())
board = [input() for _ in range(R)]

# 爆発をシミュレートする
def explode(board, R, C):
    new_board = [['.' for _ in range(C)] for _ in range(R)]
    
    for r in range(R):
        for c in range(C):
            if board[r][c] == '#':
                new_board[r][c] = '#'
            elif board[r][c].isdigit():
                power = int(board[r][c])
                for dr in range(-power, power+1):
                    for dc in range(-power, power+1):
                        if abs(dr) + abs(dc) <= power:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < R and 0 <= nc < C:
                                new_board[nr][nc] = '.'
    return new_board

# 結果を出力する
new_board = explode(board, R, C)
for row in new_board:
    print("".join(row))
