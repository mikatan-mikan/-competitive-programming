n,m = map(int,input().split())

muji = m
logo = 0

max_logo = 0

s = input()

#無地(m)から使う貪欲
for i in s:
    if i == "0":
        logo = max_logo
        muji = m
    elif i == "1":
        #無地を一枚使えるなら使う
        if muji > 0:
            muji -= 1
        #無地を一枚使えないならlogoを使う
        else:
            if logo > 0:
                logo -= 1
            else:
                max_logo += 1
    else:
        if logo > 0:
            logo -= 1
        else:
            max_logo += 1

print(max_logo)