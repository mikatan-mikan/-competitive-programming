c = [list(map(int,input().split())) for _ in range(3)]

#fraction
from fractions import Fraction

#全ての選び方の確率
all = Fraction("1")

#cを集計
num = [c[0],c[1],c[2]]
for i in range(3):
    num.append([c[0][i],c[1][i],c[2][i]])
num.append([c[0][0],c[1][1],c[2][2]])
num.append([c[0][2],c[1][1],c[2][0]])

for i in range(3):
    for j in range(3):
        #任意の場所を選んだ時
            
        for i in range(3):
            for j in range(3):
                #任意の場所を選んでいく

print(all)