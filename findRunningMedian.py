#!/bin/python3


''' Helper Methods '''


def getLeftChildIndex(index):
  return (2 * index) + 1


def getRightChildIndex(index):
  return (index + 1) * 2


def getParentIndex(index):
  if(index == 1 or index == 2):
    return 0
  elif(index % 2 == 0):
    return int((index - 2) / 2)
  else:
    return int(((index - 2) / 2) + 0.5)  # ceil of the result


def swap(heapy, Index, childNodeIndex):
  temp = heapy[Index]
  heapy[Index] = heapy[childNodeIndex]
  heapy[childNodeIndex] = temp


'''#######################################################################'''

''' Build Heap '''


def heapify(heap):
  length = len(heap) - 1
  for i in range(getParentIndex(length), -1, -1):
    satisfyHeapProperty(heap, i, length)


'''#######################################################################'''

''' Satisfy heap Property '''


def satisfyHeapProperty(heapArray, Index, size):
  LC = getLeftChildIndex(Index)
  RC = getRightChildIndex(Index)

  if (LC <= size and heapArray[LC] > heapArray[Index]):
    largest = LC
  else:
    largest = Index
  if(RC <= size and heapArray[RC] > heapArray[largest]):
    largest = RC
  if(largest != Index):
    swap(heapArray, Index, largest)
    satisfyHeapProperty(heapArray, largest, size)


'''#######################################################################'''

''' Heap Sort '''


def heapsort(array):
  heapsize = len(array) - 1
  heapify(array)
  for i in range(heapsize, -1, -1):
    swap(array, 0, heapsize)
    heapsize -= 1
    satisfyHeapProperty(array, 0, heapsize)


'''#######################################################################'''

''' QuickSort '''


def quicksort(x):
  if len(x) == 1 or len(x) == 0:
    return x
  else:
    pivot = x[0]
    i = 0
    for j in range(len(x) - 1):
      if x[j + 1] < pivot:
        x[j + 1], x[i + 1] = x[i + 1], x[j + 1]
        i += 1
    x[0], x[i] = x[i], x[0]
    first_part = quicksort(x[:i])
    second_part = quicksort(x[i + 1:])
    first_part.append(x[i])
    return first_part + second_part


'''#######################################################################'''

''' MergeSort '''


def merge(left, right):
  if not len(left) or not len(right):
    return left or right

  result = []
  i, j = 0, 0
  while (len(result) < len(left) + len(right)):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
    if i == len(left) or j == len(right):
      result.extend(left[i:] or right[j:])
      break

  return result


def mergesort(list):
  if len(list) < 2:
    return list

  middle = int(len(list) / 2)
  left = mergesort(list[:middle])
  right = mergesort(list[middle:])

  return merge(left, right)


'''#######################################################################'''
''' HELP '''
from bisect import insort


def median(a):
  if len(a) % 2 == 0:
    l = a[len(a) // 2]
    r = a[(len(a) // 2) - 1]
    med = (l + r) / 2.0

  elif len(a) % 2 != 0:
    med = a[len(a) // 2]
  return med


if __name__ == '__main__':
  heap = []
  for _ in range(int(input())):
    insort(heap, int(input()))
    print(float(median(heap)))
'''#######################################################################'''

#n = int(input().strip())
#a = []
#left_heap = []
#right_heap = []
#a_i = 0
# for a_i in range(n):
#   a_t = int(input().strip())
#   a.append(a_t)

# heapsort(a)
# if(len(a)%2 == 0):
#     middle2 = int(len(a)/2)
#     middle1 = int(middle2-1)
#     median = (a[middle2]+a[middle1])/2
# else:
#     median = a[int(len(a)/2 -0.5)]
# print(float(median))
