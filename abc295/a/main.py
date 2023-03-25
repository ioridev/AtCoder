

# 最初に単語を読み込む
first_word = input().strip()

# もし単語が数値であれば、N として使用する
if first_word.isnumeric():
    n = int(first_word)
    words = input().split()
else:
    words = [first_word] + input().split()

# 以降は前回の例と同じA
keywords = ["and", "not", "that", "the", "you"]

for w in words:
    if w in keywords:
        print("Yes")
        exit()

print("No")
