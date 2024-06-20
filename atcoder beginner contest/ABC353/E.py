n = int(input())
s = list(input().split())

letter = {}

for i in s:
    now = ""
    for j in i:
        now = f"{[now,j]}"
        if now not in letter:
            letter[now] = 1
        else:
            letter[now] += 1

ans = 0

for i in range(n - 1):
    sum_ = 0
    now = ""
    del_ = ""
    for j in range(len(s[i])):
        #自分自身をdictから削除
        del_ = "".join([del_,s[i][j]])
        letter[del_] -= 1
    it_ans = 0
    for j in range(len(s[i]) - 1, -1,-1):
        now = "".join([s[i][j],now])
        tmp = letter[now] - sum_
        it_ans += (tmp) * (j + 1)
        sum_ += tmp
    ans += it_ans

print(ans)