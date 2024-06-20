from math import sqrt

from collections import deque

ans = deque()

for i in range(10**14):
    if sqrt(i) == int(sqrt(i)):
        ans.append(i)
        if i % 1000000 == 0:
            print(i)

#ファイル書き込み
with open("ans.txt","w") as f:
    for i in ans:
        f.write(str(i) + "\n")