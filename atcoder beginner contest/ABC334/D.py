n,q = map(int,input().split())

#そりをコストの小さい順に
r = sorted(list(map(int,input().split())))

#累積和
sum_ = [0 for _ in range(n + 1)]
for i in range(1,n + 1):
    sum_[i] = sum_[i - 1] + r[i - 1]

set_sum = set(sum_)

for i in range(q):
    query = int(input())
    #2分探索で現在より小さい中から最大のものを見つける
    isNext = False
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if sum_[mid] >= query:
            right = mid
        else:
            left = mid + 1
            if sum_[mid + 1] > query:
                isNext = True
                break
    print(left - int(isNext))