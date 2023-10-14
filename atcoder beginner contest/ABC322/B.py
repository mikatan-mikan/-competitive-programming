n,m = map(int,input().split())
s = input()#min
t = input()

pre = False
sa = False

if s == t[:n]:#接頭
    pre = True

if s == t[m - n:]:#接尾
    sa = True

if pre and sa: print(0)
elif pre and not sa: print(1)
elif not pre and sa: print(2)
else: print(3)

