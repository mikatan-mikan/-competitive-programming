from math import acos, degrees, sqrt


A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
D = list(map(int,input().split()))
#D = 0
#4つの角を定義する
rot = [[A,B,C],[B,C,D],[C,D,A],[D,A,B]]
rot_num = []

for data in rot:
    #二つのベクトルを考える
    fir_bec = [abs(data[0][0] - data[1][0]),abs(data[0][1] - data[1][1])]
    sec_bec = [abs(data[2][0] - data[1][0]),abs(data[2][1] - data[1][1])]
    #print(fir_bec,sec_bec,sqrt((fir_bec[0] ** 2) + (fir_bec[1] ** 2)),sqrt((sec_bec[0] ** 2) + (sec_bec[1] ** 2)),(sec_bec[0] ** 2) + (fir_bec[1] ** 2))
    cos_ = ((fir_bec[0] * fir_bec[1]) + (sec_bec[0] * sec_bec[1])) / (sqrt((fir_bec[0] ** 2) + (fir_bec[1] ** 2)) * sqrt((sec_bec[0] ** 2) + (sec_bec[1] ** 2)))
    #print(cos_)
    rot_num.append(degrees(acos(cos_)))


if 355 <  rot_num[0] + rot_num[1] + rot_num[2] + rot_num[3] < 365:
    print("Yes")
    exit()
print("No")