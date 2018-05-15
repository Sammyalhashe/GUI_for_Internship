def array_left_rotation(a, k):
    new_array = [0] * len(a)

    for i in range(len(a)):
        new_array[i - k] = a[i]
    return new_array


#n, k = map(int, input().strip().split(' '))
#a = list(map(int, input().strip().split(' ')))
a, k = [1, 2, 3, 4, 5, 6, 7, 8], 3
answer = array_left_rotation(a, k)
print(*answer, sep=' ')
