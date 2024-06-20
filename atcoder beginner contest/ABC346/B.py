w,b = map(int,input().split())

key = "wbwbwwbwbwbw" * 100

key_sum = [[0,0] for _ in range(len(key))]

W,B = 1,0

key_sum[0][W] = 1
#wとbの累積和
for i in range(len(key)):
    if key[i] == "w":
        key_sum[i][W] = key_sum[i - 1][W] + 1
        key_sum[i][B] = key_sum[i - 1][B]
    else:
        key_sum[i][W] = key_sum[i - 1][W]
        key_sum[i][B] = key_sum[i - 1][B] + 1

#累積和の中にwとbの数が一致する部分があるかを調べる
for i in range(len(key)):
    for j in range(i,len(key)):
        if key_sum[j][W] - key_sum[i][W] == w and key_sum[j][B] - key_sum[i][B] == b:
            print("Yes")
            exit()

print("No")