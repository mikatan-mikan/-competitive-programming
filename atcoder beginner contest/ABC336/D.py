n = int(input())

a = list(map(int,input().split()))

#それぞれのaが作ることのできる最大長を考える。
a_m = [0] * (n + 1)
#スタート位置を保持
a_st = [0] * (n + 1)


for i in range(1,n + 1):
    a_m[i] = a_m[i - 1] + 1
    a_st[i] = a_st[i - 1]#スタート位置が変わらない場合
    #その場所(a[i])がスタート位置から見て数字が不足しているならスタート位置を変えるしかない
    #現在地点 - スタート地点 が a[i - 1]よりも大きい場合
    if (i - 1) - a_st[i] >= a[i - 1]:
        a_st[i] = (i) - a[i - 1]
        a_m[i] = i - a_st[i]


a_m_back = [0] * (n + 2)
a_st = [n - 1] * (n + 2)

#逆向きに同じことをする
for i in range(n,0,-1):
    a_m_back[i] = a_m_back[i + 1] + 1
    a_st[i] = a_st[i + 1]
    #現在地点(一番右からの値) - スタート地点(一番右からの値) が a[i - 1]よりも大きい場合
    if ((n - i) - ((n - 1) - a_st[i])) >= a[i - 1]:
        a_st[i] = i - a[i - 1]
        a_m_back[i] = i - a_st[i]

#a_mとa_m_backを両方見て最も大きい数字を採用
max_num = -1
for i in range(1,n + 1):
    if max_num < min(a_m[i],a_m_back[i]):
        max_num = min(a_m[i],a_m_back[i])

print(max_num)