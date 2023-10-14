N = int(input())

S = [input() for _ in range(N)]


for i in range(N):
    if S[i][0] in "HDCS" and S[i][1] in "A23456789TJQK" and S[i] not in S[:i] and S[i] not in S[i + 1:]:
        continue
    else:
        print("No")
        exit()

print("Yes")