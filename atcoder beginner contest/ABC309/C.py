
n,k = map(int,input().split())

med = [list(map(int,input().split())) for _ in range(n)]

l = 0
r = 10 ** 9
mid = r // 2

h = 10 ** 20#k以上で最小
m = 0#k以下で最大
m_d = -1

loop = 0

while True:#mid日目で二分探索
    loop += 1
    sum = 0
    for i in range(len(med)):
        sum += med[i][1] if med[i][0] >= mid else 0
    if sum > k:#錠剤数がライン以上なら
        l = mid
        mid = (l + r) // 2
        if h > sum:
            h = sum
    else:#k上以下である
        r = mid
        mid = (l + r) // 2
        if m <= sum:
            if m < sum or m_d < mid:
                m_d = mid
            m = sum
    if loop == 1000: break

print(m_d)