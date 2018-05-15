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

# Python implementation of Merge Sort
# nlog(n) always
# merging different though


def Merge_Sort(array):
    temp = [0 for i in range(len(array))]
    mergesort(array, temp, 0, len(array) - 1)


def mergesort(array, temp, leftStart, rightEnd):
    if(leftStart >= rightEnd):
        return
    mid = (leftStart + rightEnd) // 2
    mergesort(array, temp, leftStart, mid)
    mergesort(array, temp, mid + 1, rightEnd)
    merge(array, temp, leftStart, rightEnd)


def merge(array, temp, left, right):
    leftStart = left
    leftEnd = int((left + right) / 2)
    rightStart = leftEnd + 1
    rightEnd = right
    # size = right - left + 1 #len(temp)?

    left_ind = leftStart
    right_ind = rightStart
    index = leftStart

    while(left_ind <= leftEnd and right_ind <= rightEnd):
        if(array[left_ind] < array[right_ind]):
            temp[index] = array[left_ind]
            left_ind += 1
        else:
            temp[index] = array[right_ind]
            right_ind += 1
        index += 1

    # Once one of either left_ind or right_ind goes out of bounds, we have to copy into temp the rest of
    # the elements
    # Note: inly one of these loops will execute as one of right_ind or left_ind will have already reached
    # it's boundary value

    for i in range(left_ind, leftEnd):
        temp[index] = array[i]
        index += 1
    for j in range(right_ind, rightEnd):
        temp[index] = array[j]
        index += 1

    # Copy over the contents of temp back into array:

    for m in range(len(array)):
        array[m] = temp[m]


if __name__ == '__main__':
    t = input()
    for i in range(t):
        test = list(map(lambda x: int(x), input().strip().split(' ')))
        Merge_Sort(test)
        print(test)
