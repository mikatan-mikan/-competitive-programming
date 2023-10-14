n = int(input())

a = [list(input()) for _ in range(n)]

nx = [a[0][0]]
for i in range(n - 1):
    nx.append(a[0][i + 1])
    a[0][i + 1] = nx[-2]

for i in range(n - 1):
    nx.append(a[i + 1][-1])
    a[i + 1][-1] = nx[-2]

for i in range(n - 1):
    nx.append(a[-1][- (i + 2)])
    a[-1][- (i + 2)] = nx[-2]

for i in range(n - 1):
    nx.append(a[-(i + 2)][0])
    a[-(i + 2)][0] = nx[-2]

for i in range(n):
    for j in range(n):
        print(a[i][j],end="")
    print()