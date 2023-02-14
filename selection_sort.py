to_test = [8,5,2,6,9,3,1,4,7,0]

test = to_test # for + for loop
for i in range(len(test)):
    min = i
    for j in range(i + 1, len(test)):
        if test[min] > test[j]:
            min = j
    if min != i:
        test[min], test[i] = test[i], test[min]

print(test)

my_list = to_test #for + while loop
for i in range(len(my_list)):
    min = i
    x = i
    while x + 1 < len(my_list):
        x += 1
        j = x
        if my_list[min] > my_list[j]:
            min = j
    if min != i:
        my_list[min], my_list[i] = my_list[i], my_list[min]

print(my_list)