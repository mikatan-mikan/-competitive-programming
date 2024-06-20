N,K = map(int, input().split())
A_list = input().split(" ")
B_list = input().split(" ")
A_list = [int(i) for i in A_list]
B_list = [int(i) for i in B_list]

count = 0
max_deli = max(A_list)

for i in range(len(B_list)):
    if A_list[B_list[i] - 1] == max_deli:
        print("Yes")
        exit()

print("No")

