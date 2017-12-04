# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# TEST Cases:
test = [6, 10, 6, 9, 7, 8]  # given
test1 = [0, 1000]  # small-large
test2 = [-4, -5, -10, -3, -2, -1]  # negative
test3 = [-4, -3 - 4, 3, 23, 1, -233, 2]  # neg-pos
test4 = [-1000, 0, 1000, 5, -5, 2, 1, 3]  # array with large neg + large pos
test5 = []  # empty
test6 = [3]  # 1 element array
test7 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # all one int
# array where longest should be len(array) itself
test8 = [1, 2, 2, 2, 2, 2, 2, 1, 1]
testse = [0, 999, 1000]

# helper function to get the amp of a sorted array


def get_amp(array):
    """returns amplitude of sorted array

    [Amplitude of an array is its largest element minus its smallest one]

    Arguments:
        array {[type]} -- [description]

    Returns:
        number -- amplitude of the array (which is already sorted)
                  amplitude of an empty array is 0
    """
    if(array == []):
        return 0
    else:
        return (array[-1] - array[0])


def isQuasi(array):
    """helper function to see if sorted array is quasi constant

    [helper function to see if sorted array is quasi constant]

    Arguments:
        array {[int]} -- [sorted integer array]

    Returns:
        bool -- [True if sorted array is Quasi constant]
    """
    if(get_amp(array) < 2):
        return True
    return False


"""
Logic:
0) Sort the array to greedily get all elements closest in value together
1) Check all bases cases
2) Start with a default length of 1 (as 0 would have been returned anyways so pointless to check again
3) Run two indices (i,j; j<=i) until i = len(array)) to look at subsequences of sorted array
    a) i "extends" the array increases the size of the subsequence being looked at
    b) j "De-Extends" the array, decreasing the size of the array being looked at
4) For each subsequence, check if it's quasi
    a) if yes: check if the length of that subsequence if greater than the length being updates (update if necessary). Extend the subsequence
    b) if no, do nothing but extend
Worst Case: Look at an array of sizze N>2 where you constantly extend and de-extend consecutively -> slowly move through array in slow elements of 2 (O(NlogN))
"""


def solution(A):
    # write your code in Python 2.7
    pass

    # sort the array
    sorted_array = sorted(A)

    # simples cases where the original sorted array is already quasi-constant
    if(isQuasi(sorted_array)):
        return len(sorted_array)
    elif(len(sorted_array) == 0):
        return 0
    elif(len(sorted_array) == 1):
        return 1
    elif(len(sorted_array) == 2):
        if(isQuasi(sorted_array)):
            return 2

    # starting quasi length for testing: default is 1 if sorted_array isn't
    # empty
    longest_length = 1

    i = 1
    j = 0
    while (i < len(sorted_array) + 1 and j <= i):
        if(i - j >= 1):
            if(isQuasi(sorted_array[j:i])):
                if(len(sorted_array[j:i]) > longest_length):
                    longest_length = len(sorted_array[j:i])
                # Extend:
                i += 1
            else:
                # De-Extend:
                j += 1
        else:  # for indexing purposes
            # if(1 > longest_length): #shouldn't ever happen; just extend
            #    longest_length = 1
            # Extend:
            i += 1

    # return the longest length:
    return longest_length


print(solution(test))
print(solution(test1))
print(solution(test2))
print(solution(test3))
print(solution(test4))
print(solution(test5))
print(solution(test6))
print(solution(test7))
print(solution(test8))
print(solution(testse))
