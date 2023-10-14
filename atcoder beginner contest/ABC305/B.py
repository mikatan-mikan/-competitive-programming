p,q = map(str,input().split())

dis = [3,1,4,1,5,9]

if p > q:
    print(sum(dis[ord(q) - 65:ord(p) - 65]))
else:
    print(sum(dis[ord(p) - 65:ord(q) - 65]))