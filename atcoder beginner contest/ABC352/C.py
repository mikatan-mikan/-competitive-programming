n = int(input())

sum_ = 0
max_head = -1

#一番上に乗る人が頭が最大
for i in range(n):
    a,b = map(int,input().split())

    sum_ += a
    if b - a > max_head:
        max_head = b - a

print(sum_ + max_head)