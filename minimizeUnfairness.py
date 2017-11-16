"""Greedy Algorithm minimizes unfairness of an array by choosing K values

unfairness == max(x0,x1,...,xk)-min(x0,x1,...,xk)

Variables:
    int: N -> number of elements in list
    int: K -> number of list elements to choose
    list: vals -> list to minimize unfairness

Example Input:
    10 (N)
    4 (K)
    (The Rest are list elements)
    1
    2
    3
    4
    10
    20
    30
    40
    100
    200

Example Output:
    3 (the minimum unfairness)
"""


def calcUnfairness(reduced_array):
    return (reduced_array[-1] - reduced_array[0])


def minimizeUnfairness(n, k, arr):
    unfairness = (arr[k - 1] - arr[0])

    if len(arr) == k or len(arr) == 1:
        unfairness = calcUnfairness(arr)
    else:
        for i in range(1, n - (k - 1)):
            if((arr[i + k - 1] - arr[i]) < unfairness):
                unfairness = (arr[i + k - 1] - arr[i])
            if(unfairness == 0):
                break
    print(unfairness)

    # First Greedy Idea: Farthest from average remove and test again
    # average = int(sum(arr)/len(arr))
    # ldev = int(abs(arr[-1]-average))
    # sdev = int(abs(arr[0]-average))

    # if (ldev>=sdev):
    #    sorts.pop()
    #    return minimizeUnfairness(k,sorts)
    # else:
    #    sorts.pop(0)
    #    return minimizeUnfairness(k,sorts)


if __name__ == '__main__':
    N = int(input().strip())
    K = int(input().strip())

    vals = []
    for i in range(N):
        vals.append(int(input().strip()))

    if(K == 0):
        print("Should at least be 1")
    else:
        reduced_arr = minimizeUnfairness(N, K, sorted(vals))