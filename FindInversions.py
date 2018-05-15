def merge(left, right):
    swaps = 0
    result = []
    i, j = 0, 0
    while (len(left) > i and len(right) > j):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            swaps += len(left) - i
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
    return result, swaps


def mergesort(lists):
    if len(lists) < 2:
        return lists, 0
    else:
        middle = (len(lists) // 2)
        left, swaps0 = mergesort(lists[:middle])
        right, swaps1 = mergesort(lists[middle:])
        res, swaps = merge(left, right)
        return res, (swaps + swaps0 + swaps1)


def countInversions(arr):
    # Complete this function
    sort_arr, swaps = mergesort(arr)
    return sort_arr, swaps


if __name__ == '__main__':
    test = [1, 32, 122, 32, 12, 311, 2, 3, 21, 2]
    result, no_swaps = countInversions(test)
    print("sorted array:", result, "swaps:", no_swaps)
