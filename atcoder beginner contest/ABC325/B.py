now_base_time = 0

n = int(input())
w = []
x = []
cnt = [0 for _ in range(24)]#時間ごと

for i in range(n):
    tmp = list(map(int,input().split()))
    w.append(tmp[0])
    x.append(tmp[1])

for i in range(24):
    for j in range(n):
        now_base_time = x[j] + i
        if now_base_time >= 24:
            now_base_time -= 24
        if now_base_time < 18 and now_base_time >= 9:
            cnt[i] += w[j]

print(max(cnt))