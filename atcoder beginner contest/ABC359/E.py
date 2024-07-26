n = int(input())

h = list(map(int,input().split()))

end = h[-1]

h_dict = {
}

for i in range(n):
    h_dict[h[i]] = i

h_sort = sorted(h)
h_sort_dict = {
}

for i in range(n):
    h_sort_dict[h_sort[i]] = i

cnt = 0

bef = 0
for i in range(n):
