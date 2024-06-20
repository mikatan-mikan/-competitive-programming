h,w = map(int,input().split())

a = [list(map(int,input().split())) for _ in range(h)]

w_s = [sum(a[i]) for i in range(h)]#横方向の和
h_s = [sum([a[j][i] for j in range(h)]) for i in range(w)]#縦方向の和

for i in range(h):
    for j in range(w):
        print(w_s[i] + h_s[j] - a[i][j],end=" ")
    print()