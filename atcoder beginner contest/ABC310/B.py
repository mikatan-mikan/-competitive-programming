n,m = map(int,input().split())

data = [list(map(int,input().split())) for _ in range(n)]

def yes():
    print("Yes")
    exit()

for i in range(n):
    for j in range(n):
        if i == j: continue
        if data[j][0] <= data[i][0]:
            is_break = False
            for k in range(data[i][1]):
                if i == 3 and j == 1:
                    pass
                if data[i][k + 2] not in data[j][2:]:
                    is_break = True
                    break#含まれていない要素がある
            if not is_break:
                if data[i][0] > data[j][0]:
                    yes()
                elif data[j][1] > data[i][1]:
                    yes()

print("No")