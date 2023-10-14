S = input()
T = input()

cnt  = 0

while True:
    try:
        S[cnt]
    except: 
        print(cnt + 1)
        break
    if S[cnt] != T[cnt]:
        print(cnt + 1)
        break
    cnt += 1
