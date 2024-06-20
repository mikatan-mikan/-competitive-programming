n,m = map(int,input().split())
c = list(input().split())
d = list(input().split())
p = list(map(int,input().split()))

price = dict()

for i in range(len(d)):
    price[d[i]] = p[i + 1]

price["other"]= p[0]

sum = 0

for i in c:
    if i in price:
        sum += price[i]
    else:
        sum += price["other"]
print(sum)
