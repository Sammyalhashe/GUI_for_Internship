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
# Implementation of Quick Sort in Python
# nlog(n) best case; n^2 worst case
try:
    from random import random
except ImportError as e:
    print(e)


def Quick_Sort(array):
    quicksort(array, 0, len(array) - 1)


def quicksort(array, left, right):
    if(left >= right):
        return
    # random() returns in range [0.0,1.0)
    pivot = array[int(random() * len(array))]
    index = partition(array, left, right, pivot)
    quicksort(array, left, index - 1)
    quicksort(array, index, right)


def partition(array, left, right, pivot):
    while(left <= right):
        while(array[left] < pivot):
            left += 1
        while(array[right] > pivot):
            right -= 1
        if(left <= right):
            swap(array, left, right)
            left += 1
            right -= 1
    return left  # index of the partition in array


def swap(array, left, right):
    array[left], array[right] = array[right], array[left]


if __name__ == '__main__':
    test = [1, 4, 3, 5, 6, 32, 432, 1, 123, 32, 2, 43]
    print(test)
    Quick_Sort(test)
    print(test)
    t = input()
    for i in range(t):
        test = list(map(lambda x: int(x), input().strip().split(' ')))
        Quick_Sort(test)
        print(test)
