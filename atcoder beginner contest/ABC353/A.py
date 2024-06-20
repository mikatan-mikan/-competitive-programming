n = int(input())

h = list(map(int, input().split()))

highest = -1
high = h[0]

for i in range(len(h[1:])):
    if h[i + 1] > high:
        highest = i + 2
        high = h[i + 1]
        break

print(highest)