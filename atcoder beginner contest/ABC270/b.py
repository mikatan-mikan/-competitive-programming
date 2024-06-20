x,y,z = map(int,input().split())

#ゴールがマイナスの場合
if x < 0:
    if y < 0:
        if y < x:
            print(abs(x))
            exit()
        if y < z:
            if z < 0:
                print(abs(x))
            else:
                print(2 * abs(z) + abs(x))
        else:
            print(-1)
    else:
        print(abs(x))
else:
    if y > 0:
        if y > x:
            print(abs(x))
            exit()
        if y > z:
            if z > 0:
                print(abs(x))
            else:
                print(2 * abs(z) + abs(x))
        else:
            print(-1)
    else:
        print(abs(x))
