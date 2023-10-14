n = int(input())

fs = sorted([list(map(int,input().split())) for _ in range(n)], key=lambda x:x[1], reverse=True)

max_ = 0

for i in range(1,n):
    if fs[0][0] == fs[i][0]:
        if fs[0][1] + (fs[i][1] // 2) > max_:
            max_ = fs[0][1] + (fs[i][1] // 2)
        continue
    if fs[0][1] + fs[i][1] > max_:
        max_ = fs[0][1] + fs[i][1]

next_ = 0

for i in range(1,n):
    if fs[0][0] != fs[i][0]:
        next_ = i

for i in range(1,n):
    if i == next_:
        continue
    if fs[next_][0] == fs[next_][0]:
        if fs[next_][1] + (fs[i][1] // 2) > max_:
            max_ = fs[next_][1] + (fs[i][1] // 2)
        continue
    if fs[next_][1] + fs[i][1] > max_:
        max_ = fs[next_][1] + fs[i][1]

print(max_)