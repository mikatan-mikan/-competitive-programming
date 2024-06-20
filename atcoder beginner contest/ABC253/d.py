n,a,b = map(int,input().split())
sum = (n*(n+1))//2
print(sum)
sum -= ((n*(n+1))//2)//a
if b % 3 == 0:
    n_ = n
elif b % 3 == 1:
    n_ = n -1
elif b %3 == 2:
    n_ = n -2
sum -= ((n_*(n_+1))//2)//b
print(sum,(n_*(n_+1))//2//b)
sum += ((n*(n+1))//2)//(a*b)
print(sum,((n*(n+1))//2)//(a*b))

print(sum)