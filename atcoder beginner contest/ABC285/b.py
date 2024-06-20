N = int(input())

S = input()

for j in range(1,len(S)):
    cnt = 0
    b_flg = False
    for k in range(1,N - j + 1):
        try:
            if S[k - 1] != S[j - 1 + k]:
                cnt += 1
            else:
                print(cnt)
                b_flg = True
                break
        except:
            while True:pass
    if b_flg : continue
    print(cnt)
    