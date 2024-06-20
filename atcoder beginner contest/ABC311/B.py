n,d = map(int,input().split())

s = [input() for i in range(n)]

m = 0

def h(i):
    for j in range(n):
        if s[j][i] == "o":
            continue
        else:
            return 0
    return 1

cnt = 0

for i in range(d):
    if h(i):
        cnt += 1
        if m < cnt:
            m = cnt
    else:
        cnt = 0

print(m)