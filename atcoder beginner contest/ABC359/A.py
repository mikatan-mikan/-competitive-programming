n = int(input())

s = [input() for i in range(n)]

cnt = 0

for i in s:
    if i == "Takahashi":
        cnt += 1

print(cnt)