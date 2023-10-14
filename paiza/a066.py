n = int(input())
s = set()

for i in range(n):
    in_ = list(map(int,input().split()))
    s |= set(range(in_[0],in_[1] + 1))
    if len(s) == 100000:
        break

max_ = 0
cnt = 0

for i in range(100000):
    if i in s:
        cnt += 1
        if cnt > max_:
            max_ = cnt
    else:
        cnt = 0

print(max_)