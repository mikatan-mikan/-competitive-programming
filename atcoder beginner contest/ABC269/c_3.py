N = int(input())
n_10 = N
N = bin(N)
all_num = 2**60
print(all_num)

#これをもとに重複パターンの数を削除
double_p = 1
while True:
    if len(N) < 62:
        N = N[:2] + "0" + N[2:]
    else:
        break

#Nから引いていく
for i in range(60):#60桁下から
    if N[1 + 60 - i] == "1":
        print(i for i in range(0,n_10,2 ** (i + 1)))
if double_p == 2^60:
    print("ok")
print(all_num / double_p)
