class Heap(object):
    """Min Heap:

    Binary Tree with following properties:
    1) Parent is always less in value than children
    2) has height of log(N) (base 2)
    """

    def __init__(self):
        super(Heap, self).__init__()  # for multi-inheritance
        self.heap = [0]
        self.current_size = 0

    def insert(self, value):
        self.heap.append(value)
        self.current_size += 1
        self.restoreHeap(self.current_size)

    def swap(self, i1, i2):
        temp = self.heap[i1]
        self.heap[i1] = self.heap[i2]
        self.heap[i2] = temp

    def restoreHeap(self, size):

        while (size // 2 > 0):
            if(self.heap[size // 2] > self.heap[size]):
                self.swap(size, size // 2)
                size = size // 2
            else:
                break

    def deleteMin(self):
        return_val = self.heap[1]
        self.heap[1] = self.heap[self.current_size]
        self.current_size -= 1
        self.heap.pop()
        self.bubbleDown(1)
        return return_val

    def bubbleDown(self, i):
        while (i * 2 <= self.current_size):
            mc = self.getSmallestChild(i)
            if(self.heap[mc] < self.heap[i]):
                self.swap(i, mc)
                i = mc
            else:
                break

    def getSmallestChild(self, i):
        # don't have to worry about 2*i being larger as this function wouldn't
        # be called
        if(2 * i + 1 > self.current_size):
            return 2 * i
        else:
            smallest = self.heap[2 * i]
            if(self.heap[2 * i + 1] < smallest):
                smallest = self.heap[2 * i + 1]
            return smallest

    def buildHeap(self, array):
        index = len(array) // 2
        self.current_size = len(array)
        self.heap = [0] + array
        while (index > 0):
            self.bubbleDown(index)
            index -= 1


if __name__ == '__main__':
    test = [1, 5, 3, 4, 6, 7, 5, 3]
    print(test)
    Heap = Heap()
    Heap.buildHeap(test)
    print(Heap.heap)
