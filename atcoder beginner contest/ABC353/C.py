n = int(input())


a = list(map(int,input().split()))

a.sort(reverse=True)

#これを使ってどこまでが%=10**8が必要な範囲かを考える(前に詰めるだけ)
mod_place = len(a) - 1

ans = 0

for i in range(len(a)):
    #最初にmodが必要な範囲を考える
    for j in range(mod_place,i - 1,-1):
        mod_place = j
        if a[i] + a[j] < 10**8:
            continue
        else:
            break
    #modが必要な範囲
    mod_range = mod_place - i if mod_place - i > 0 else 0
    ans += ((a[i] * (len(a) - 1))) - ((10 ** 8) * mod_range)

print(ans)