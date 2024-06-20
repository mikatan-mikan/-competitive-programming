n = int(input())

from math import sqrt

point = [list(map(int,input().split())) for _ in range(n)]


for i in range(n):
    max_length = -1
    place = -1
    for j in range(n):
        if i == j:
            continue
        if max_length < sqrt((point[i][0] - point[j][0])**2 + (point[i][1] - point[j][1])**2):
            max_length = sqrt((point[i][0] - point[j][0])**2 + (point[i][1] - point[j][1])**2)
            place = j + 1
    print(place)