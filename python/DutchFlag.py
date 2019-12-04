one = [1, 2, 3, 2, 3, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3]


def swapPositions(list, pos1, pos2):

    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


def sortArray(array):
    i = 0
    j = 0
    k = len(array)
    while(j < k):
        if array[j] == 1:
            swapPositions(array, i, j)
            i += 1
            j += 1
        elif array[j] == 2:
            j += 1
        elif(array[j] == 3):
            swapPositions(array, j, k-1)
            k -= 1
        print(array)


print(one)
sortArray(one)
print(one)
