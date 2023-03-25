R, C = map(int, input().split())
B = [list(input().strip()) for i in range(R)]

# 爆弾の位置を取得する
bombs = []
for i in range(R):
    for j in range(C):
        if B[i][j] in "123456789":
            bombs.append((i, j, int(B[i][j])))

# 爆弾の効果範囲を更新する関数
def update_explosion_range(bomb):
    x, y, power = bomb
    for i in range(x - power, x + power + 1):
        if i < 0 or i >= R:
            continue
        for j in range(y - power, y + power + 1):
            if j < 0 or j >= C:
                continue
            if abs(i - x) + abs(j - y) <= power and B[i][j] != "#":
                B[i][j] = "."

# 爆弾の効果範囲を更新する
for bomb in bombs:
    update_explosion_range(bomb)

# 盤面を出力する
for i in range(R):
    print("".join(B[i]))
