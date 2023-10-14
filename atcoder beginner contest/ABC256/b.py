#[0,0,0,0]
#P=0
#A = [3,2,4]N=3
#i = 1のとき
#[1,0,0,0]
#[0,0,0,1]
#i = 2のとき
#[1,0,0,1]
#[0,0,1,0]
# P = 1
#・・・
#N回目のとき
#最後にPを出してください

N = int(input())
A_i = list(map(int, input().split()))
P = 0

koma_list = [0 for i in range(N)]

for i in range(N):
    koma_list[i] = 1
    for j in range(N):
        if koma_list[j] != 0:
            koma_list[j] += A_i[i]
            if koma_list[j] > 4:
                P += 1
                koma_list[j] = 0
print(P)