H,W = map(int,input().split())
m = True
S_list = []
for i in range(H):
    S_list.append(input())
    S_list[i] = list(S_list[i])

#oからoの距離を求める
for i in range(H):
    for j in range(W):
        if S_list[i][j] == 'o':
            if m:
                start = (i,j)
                m = False
            else:
                end = (i,j)
                break

sum = 0
sum += abs(start[0]-end[0])
sum += abs(start[1]-end[1])
print(sum)