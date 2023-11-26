n = int(input())

s = [input() for _ in range(n)]

ans = 0

h = [s[i].count("o") for i in range(n)]
w = [0 for _ in range(n)]
for i in range(n):
    for j in range(n):
        if s[j][i] == "o":
            w[i] += 1

for i in range(n):
    for j in range(n):
        if s[i][j] == "x": continue
        ans += (h[i] - 1) * (w[j] - 1)

print(ans)
