s = list(input())

from collections import deque

dat = deque(["none","none","none"])

#文字を前から入れてその時"ABC"が最後尾に存在すれば削除し、無くなるまで消す
for i in s:
    dat.append(i)
    while True:
        if dat[-3] == "A" and dat[-2] == "B" and dat[-1] == "C":
            dat.pop()
            dat.pop()
            dat.pop()
        else:
            break


dat.popleft()
dat.popleft()
dat.popleft()
print(*dat,sep="")