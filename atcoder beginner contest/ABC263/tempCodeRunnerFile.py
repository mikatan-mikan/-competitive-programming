from itertools import permutations

N,M = map(int,input().split())

num_list = list(range(1,M + 1))#これの組み合わせから単調増加を探す

out_list = []

for i in permutations(num_list,N):
    for j in range(1,N):
        if i[j - 1] < i[j]:
            if j == N - 1:
                out_list.append(i)
            continue
        else:
            break


for i in out_list:
    print(*i)