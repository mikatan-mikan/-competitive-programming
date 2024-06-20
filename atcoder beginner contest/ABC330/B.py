n,l,r = map(int,input().split())
a = list(map(int,input().split()))

for i in range(n):
    # |x - a[i]| <= |y - a[i]|を満たすxを探す(yは任意の整数)
    #yを決定する(|y - a[i]|を最小にする)
    y = a[i]
    if y < l:y = l
    elif y > r:y = r
    print(y,end = " ")