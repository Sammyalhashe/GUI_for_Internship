# Implementation of Quick Sort in Python
# nlog(n) best case; n^2 worst case
from random import random


def Quick_Sort(array):
    quicksort(array, 0, len(array) - 1)


def quicksort(array, left, right):
    if(left >= right):
        return
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


# given an array of ints, find an element in question. If there return True
# If not there, return false


def binarySearch(array, search_int):

    # Sort the array
    Quick_Sort(array)

    # Iterative approach to binary search on the array

    left = 0
    right = len(array) - 1

    while(left <= right):
        mid = left + ((right - left) // 2)  # middle of the array

        if(array[mid] == search_int):
            return True
        elif(search_int < array[mid]):
            right = mid - 1
        else:
            left = mid + 1
    return False
