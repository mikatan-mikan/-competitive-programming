N = int(input())
A = []
ans_tmp = ""
max_ = 0

for i in range(N):
    A.append(list(input()))
    for j in range(N):
        A[i][j] = int(A[i][j])


for i in range(N):#全てのマスを起点として(全探索)
    for j in range(N):
        for k in range(8):
            for l in range(N):#n-1回移動する
                x = l
                y = l
                if x + j >= N:
                    x -= N
                if y + i >= N:
                    y -= N
                minus_x = j - x 
                minus_y = i - y 
                if minus_y < 0:
                    minus_y += N - 1
                if minus_x < 0:
                    minus_x += N - 1
                if k == 0:
                    ans_tmp += str(A[i + y][j])
                elif k == 1:
                    ans_tmp += str(A[i][j + x])
                elif k == 2:
                    ans_tmp += str(A[minus_y][j])
                elif k == 3:
                    print(minus_x,k,l,i,j)
                    ans_tmp += str(A[i][minus_x])
                elif k == 4:
                    ans_tmp += str(A[i + y][j + x])
                elif k == 5:
                    ans_tmp += str(A[i + y][minus_x])
                elif k == 6:
                    ans_tmp += str(A[minus_y][j + x])
                elif k == 7:
                    ans_tmp += str(A[minus_y][minus_x])
            print(ans_tmp)
            if max_ < int(ans_tmp):
                max_ = int(ans_tmp)
            ans_tmp = ""

print(max_)

10
1239871323
2139023423
7292032191
7383495028
8263950372
7380493843
1423143213
1432514312
2143153125
3125316374


4 
9870
9803
#0274
1234