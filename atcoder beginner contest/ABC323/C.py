n,m = map(int,input().split())

a = list(map(int,input().split()))


sorted_a = a.copy()
for i in range(len(sorted_a)):
    sorted_a[i] = [sorted_a[i],i]
sorted_a = sorted(sorted_a,reverse=True)

s = [input() for _ in range(n)]

score = [0 for _ in range(n)]

for i in range(n):
    score[i] += (i + 1)
    for j in range(m):
        if s[i][j] == "o":
            score[i] += a[j]

top_score = max(score)#この点を超えればいい

for i in range(n):# n人に対して見る
    if score[i] == top_score:#既に最高点なら
        print(0)
        continue
    need = top_score - score[i]
    problem = 0
    for add in sorted_a:
        if s[i][add[1]] == "o":
            continue
        need -= add[0]
        problem += 1
        if need < 0:
            print(problem)
            break