N = int(input())
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
for i in range(60):#60桁上から走査
    if N[2 + i] == "0":
        double_p *= 2
        print(double_p)
        
if double_p == 2^60:
    print("ok")
print(all_num / double_p)
