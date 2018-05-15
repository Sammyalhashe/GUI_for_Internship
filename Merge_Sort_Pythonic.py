'''input
10
"12 4 19 3 2"
"2 8 9 17 7"
"2 3 15 9 4"
"16 10 20 4 17"
"18 11 7 20 12"
"19 1 3 12 9"
"13 5 7 9 6"
"9 18 3 16 10"
"16 18 6 3 9"
"1 10 14 19 6"
'''
# More pythonic implementation of merge sort


def Merge_Sort_Pythonic(array):
    return mergesort_Pythonic(array)


def mergesort_Pythonic(array):
    if(len(array) < 2):
        return array
    # Integer division for middle index
    mid = ((len(array)) // 2)

    # Merge-sort left and right halves
    left = mergesort_Pythonic(array[:mid])
    right = mergesort_Pythonic(array[mid:])
    res = merge(left, right)
    return res


def merge(left, right):
    # size = right - left + 1 #len(temp)?
    i, j, ind = 0, 0, 0
    l, r = len(left), len(right)
    length = l + r
    temp = [0 for i in range(length)]

    while(len(left) > i and len(right) > j):
        if(left[i] < right[j]):
            temp[ind] = left[i]
            i += 1
        else:
            temp[ind] = right[j]
            j += 1

        ind += 1

    # Once one of either left_ind or right_ind goes out of bounds, we have to copy into temp the rest of
    # the elements
    # Note: inly one of these loops will execute as one of right_ind or left_ind will have already reached
    # it's boundary value
        if i == len(left) or j == len(right):
            temp.extend(left[i:] or right[j:])
            break

    return temp


if __name__ == '__main__':
    test = [1, 32, 122, 32, 12, 311, 2, 3, 21, 2]
    result = Merge_Sort_Pythonic(test)
    print(result)
    t = input()
    for i in range(t):
        test = list(map(lambda x: int(x), input().strip().split(' ')))
        tested = Merge_Sort_Pythonic(test)
        print(tested)
