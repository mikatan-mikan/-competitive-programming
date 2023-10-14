from itertools import product

list_ = range(1,int(input()) + 1)
list_ = list(product(list_,2))
sum = 0

print(list_)

for i in range(len(list_)):
    if type((list_[i][0] * list_[i][1]) ** 1/2) == int:
        sum += 1
    print((list_[i][0] * list_[i][1]) ** 1/2)

print(sum)