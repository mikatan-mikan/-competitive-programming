a,m,l,r = map(int,input().split())

#基準を0にする
r -= a
l -= a

ans = (r//m - l//m)

#もし0地点に置く必要があるなら
if l%m == 0:
    ans += 1

print(int(ans))

# b_l = l
# b_r = r

# a %= m

# #aが起点
# #mおき
# #lからrまで
# #間における数を求める
# #全部+にする
# r = int((r - a) / m)
# l = int((l - a) / m)
# if b_r <= a and a <= b_l:
#     ans = 1
# else: 
#     ans = 0
# ans += r - l

# print(ans)