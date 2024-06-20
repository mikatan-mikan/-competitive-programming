H,M = map(int,input().split())


#1日の時刻
for i in range(24):
    for j in range(60):
        A = int(H/10)
        B = int(H%10)
        C = int(M/10)
        D = int(M%10)
        if A * 10 + C < 24 and B * 10 + D < 60:
            print(H,M)
            exit()
        if M < 60:
            M += 1
        else:
            M = 0
            H += 1
            if H > 23:
                H = 0
