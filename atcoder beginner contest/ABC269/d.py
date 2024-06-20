N = int(input())

place = []

for i in range(N):
    place.append(tuple(map(int,input().split())))

place_set = set(place.copy())


def place_search(in_place):
    global now_ans,check_list
    if (in_place[0] - 1,in_place[1] - 1) in place_set and check_list[in_place[0] - 1 + 1][in_place[1] - 1 + 1] == 0:
        check_list[in_place[0] - 1 + 1][in_place[1] - 1 + 1] = 1
        now_ans += 1
        place_search((in_place[0] - 1,in_place[1] - 1))
    if (in_place[0] - 1,in_place[1]) in place_set and check_list[in_place[0] - 1 + 1][in_place[1] + 1] == 0:
        check_list[in_place[0] - 1 + 1][in_place[1] + 1] = 1
        now_ans += 1
        place_search((in_place[0] - 1,in_place[1]))
    if (in_place[0],in_place[1] - 1) in place_set and check_list[in_place[0] + 1][in_place[1] - 1 + 1] == 0:
        check_list[in_place[0] + 1][in_place[1] - 1 + 1] = 1
        now_ans += 1
        place_search((in_place[0],in_place[1] - 1))
    if (in_place[0] + 1,in_place[1]) in place_set and check_list[in_place[0] + 1 + 1][in_place[1] + 1] == 0:
        check_list[in_place[0] + 1 + 1][in_place[1] + 1] = 1
        now_ans += 1
        place_search((in_place[0] + 1,in_place[1]))
    if (in_place[0],in_place[1] + 1) in place_set and check_list[in_place[0] + 1][in_place[1] + 1 + 1] == 0:
        check_list[in_place[0] + 1][in_place[1] + 1 + 1] = 1
        now_ans += 1
        place_search((in_place[0],in_place[1] + 1))
    if (in_place[0] + 1,in_place[1] + 1) in place_set and check_list[in_place[0] + 1 + 1][in_place[1] + 1 + 1] == 0:
        check_list[in_place[0] + 1 + 1][in_place[1] + 1 + 1] = 1
        now_ans += 1
        place_search((in_place[0] + 1,in_place[1] + 1))


check_list_base = [[0 for i in range(12)] for j in range(12)]

max = 0
for i in range(len(place)):#それぞれの場所から始める
    now_ans = 1
    check_list = check_list_base.copy()
    check_list[place[i][0]][place[i][1]] = 1
    place_search(place[i])
    if max < now_ans:
        max = now_ans
        print(check_list)

print(max)