to_test = [8,5,2,6,9,3,1,4,7,0]

for i in range(len(to_test)):
    compare = to_test[i]
    j = i - 1

    while j >= 0 and compare < to_test[j]:
        to_test[j + 1] = to_test[j]
        j = j - 1
    to_test[j + 1] = compare

print(to_test)
