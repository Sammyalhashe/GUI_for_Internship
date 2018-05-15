"""

[My insort method to insert an element into an already sorted array and maintain it sorted]
"""


def Insort(x, array, lo=0, hi=None):
    """inserts element into already sorted array

    Arguments:
        x {int} -- element to be inserted
        array {int} -- holds integer elements

    Keyword Arguments:
        lo {int} -- left end of subarray considered in recursive step (default: {0})
        hi {int} -- right end of subarray considered in recursive step (default: {None})

    Returns:
        list -- list with new element inserted (still sorted)
    """

    if (array is None):
        return [x]
    if (array == []):
        return array.append(x)
    if (hi is None):
        hi = len(array) - 1
    if (lo == hi):
        if(x <= array[lo]):
            #array.insert(lo, x)
            array = [x] + array
            # print(array)
            return array
        else:
            #array.insert(hi + 1, x)
            array = array + [x]
            # print(array)
            return array

    mid = hi // 2
    if(x <= array[mid]):
        hi = mid + 1  # convention
        return Insort(x, array[:hi], lo=0, hi=None) + array[hi:]
    else:
        lo = mid + 1
        return array[:lo] + Insort(x, array[lo:], lo=0, hi=None)


if __name__ == '__main__':
    test = [1, 2, 3, 4, 5, 6, 8]
    print(test)
    new = Insort(7, test, lo=0, hi=None)
    print(new)
    news = Insort(2, new)
    print(news)
    news = Insort(8, news)
    print(news)
