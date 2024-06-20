n = int(input())

s = [input() for _ in range(n)]

win_cnt = [0 for _ in range(n)]

for i in range(n):
    for j in range(i,n):
        if s[i][j] == "o":
            win_cnt[i] += 1
        elif s[i][j] == "x":
            win_cnt[j] += 1

now = max(win_cnt)

while True:
    for i in range(n):
        if win_cnt[i] == now:
            print(i + 1,end = " ")
    now -= 1
    if now == -1:
        break