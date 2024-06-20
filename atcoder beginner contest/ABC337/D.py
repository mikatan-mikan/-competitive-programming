h,w,k = map(int,input().split())

s = [input() for _ in range(h)]

ans = 10 ** 9

dp = [[[-1,-1] for _ in range(h)] for _ in range(w)]
        
print(ans if ans != 10 ** 9 else -1)