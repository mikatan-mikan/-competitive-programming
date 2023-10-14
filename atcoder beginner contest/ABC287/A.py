N = int(input())

s = [input() for _ in range(N)]

cnt = 0

for i in range(N):
    if s[i] == "For":
        cnt += 1

if cnt > N // 2:
    print("Yes")
else:
    print("No")