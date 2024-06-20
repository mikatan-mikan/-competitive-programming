#n*mまでにnの倍数はm個,mの倍数はn個(但しn,mは互いに素)
#n*mは省くのでm - 1,n - 1
n,m,k = map(int,input().split())

#nが大きくなるように
if m > n:
    n,m = m,n

#n,mからn*mに含まれる倍数の数
block = (m - 1) + (n - 1)

#(k // block):kの中に含まれるblockの数
#ansを加算してちょうどブロック分出なかった部分を計算
ans = (k // (block)) * ((n) * (m))
k %= (block)

n_,m_ = 0,0

#kは十分に小さいので順にみればよい
for i in range(k):
    if n_ < m_:
        n_ += n
    else:
        m_ += m
    if n_ == m_:#あり得ない・・・？
        m_ += m

ans = ans + max(n_,m_)
if k == 0:
    ans -= m

print(ans)