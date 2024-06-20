# 貪欲に小さいものをくっつける以外なさそう・・・？
n = int(input())

from collections import deque

s_c = deque()
size_set = set()
double_slime = dict()#合成後のスライムを保管しておく

sum_slime = 0
max_size = 0

for i in range(n):
    inp = list(map(int,input().split()))
    size_set.add(inp[0])
    sum_slime += inp[1]
    s_c.append(inp)
    if max_size < inp[0]:
        max_size = inp[0]

#サイズでソート
s_c = sorted(s_c)
i = 0
for i in range(n):# 貪欲に小さいものをくっつける
    if s_c[i][0] in double_slime:#もし、合成後のスライムとさらに合成出来そうなら
        s_c[i][1] += double_slime.pop(s_c[i][0])#その数を写しておく
    if s_c[i][1] >= 2:
        add = s_c[i][1] // 2
        sum_slime -= add#消えた分のスライムを減算する
        #合成後のスライムを保管
        #繰り返し、addを2で割り1以下になれば合成終了
        if s_c[i][0] * 2 not in double_slime:
            double_slime[s_c[i][0] * 2] = add
        else:
            double_slime[s_c[i][0] * 2] += add
        now = s_c[i][0] * 2
        while True:
            if double_slime[now] >= 2:# どんどん奥に持っていく
                if now * 2 not in double_slime:
                    double_slime[now * 2] = double_slime[now] // 2#存在しないならそのまま代入
                else:
                    double_slime[now * 2] += double_slime[now] // 2#するなら加算
                sum_slime -= double_slime[now] // 2
                double_slime[now] = double_slime[now] % 2
                now = now * 2
            else:
                break
        if s_c[i][1] % 2 == 1:
            s_c[i][1] = 1
        else:
            s_c[i][1] = 0


    
print(sum_slime)