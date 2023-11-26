n,q = map(int,input().split())

a:list[int] = list(map(int,input().split()))
set_a = dict()

for i in a:
    if i not in set_a:
        set_a[i] = 1
    else:
        set_a[i] += 1

#空き場所を管理する
from sortedcontainers import SortedList
air:list[int] = SortedList()
for i in range(0,5*(10**5)):
    if i not in set_a:#set_aに存在しないなら空き場所として記憶
        air.add(i)

now_mex:int = air[0]
air.pop(0)

for _ in range(q):
    i,x = map(int,input().split())
    set_a[a[i - 1]] -= 1
    if set_a[a[i - 1]] == 0:
        del set_a[a[i - 1]]
        if now_mex > a[i - 1]:
            air.add(now_mex)
            now_mex = a[i - 1]#空き場所に即座に移動
        else:
            #削除したなら空き場所になる
            air.add(a[i - 1])
    a[i - 1] = x
    if x not in set_a:
        set_a[x] = 1
        #新たに作ったなら空き場所から取り除く
        air.discard(x)
    else:
        set_a[x] += 1
    #mexを探す
    if now_mex in set_a:
        now_mex = air[0]
        air.pop(0)
    print(now_mex)