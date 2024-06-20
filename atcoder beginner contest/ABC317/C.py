n,d,p = map(int,input().split())

f = sorted(list(map(int,input().split())),reverse=True)

buy_path = 0
cost = 0

for i in range(n):
    #毎回の費用を加算してd日ごとにそれより安ければ周遊を買う
    buy_path += f[i]
    if (i + 1) % d == 0 or i == n - 1:
        cost += min(buy_path,p)
        buy_path = 0


print(cost)