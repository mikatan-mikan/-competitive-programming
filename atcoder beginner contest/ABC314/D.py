n = int(input())
s = list(input())
q = int(input())


query = [0 for _ in range(q)]

last_change = 0

l = list(range(len(query)))

for i in l:
    tmp = list(input().split())
    tmp[0] = int(tmp[0])
    tmp[1] = int(tmp[1])
    if tmp[0] == 2 or tmp[0] == 3:
        last_change = i
    query[i] = tmp

for i in l:
    #int に 変換
    if query[i][0] == 1:
        s[query[i][1] - 1] = str(query[i][2])
    else:
        if last_change != i:
            continue#最後以外の変換は無視してよい
        if query[i][0] == 2:
            for i in range(len(s)):
                s[i] = s[i].lower()
        elif query[i][0] == 3:
            for i in range(len(s)):
                s[i] = s[i].upper()


print(*s,sep="")