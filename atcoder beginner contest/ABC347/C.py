n,a,b = map(int,input().split())

d = list(map(int,input().split()))

for i in range(len(d)):
    d[i] = d[i] % (a + b)

#dをソートした後に最も間隔が大きい場所を調べその領域以外の場所がbに入ればいい
d.sort()

dd = ((a + b) - d[-1]) + d[0]
dd_place = 0
for i in range(len(d) - 1):
    if d[i + 1] - d[i] > dd:
        dd = d[i + 1] - d[i]
        dd_place = i + 1

for i in range(dd_place):
    d[i] = d[i] + a + b

d = d[dd_place:] + d[:dd_place]

if max(d) - min(d) < a:
    print("Yes")
else:
    print("No")