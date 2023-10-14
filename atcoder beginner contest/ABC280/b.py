N = int(input())

S = list(map(int,input().split()))

sum_num = 0

ans = []

for i in range(N):
    ans.append(S[i] - sum_num)
    sum_num = S[i]

print(*ans)