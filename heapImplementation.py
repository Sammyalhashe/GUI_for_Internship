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
        """
        restores min heap property (use only for insert)
        """
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
        """
        @brief      Builds a heap.

        @param      self   The object
        @param      array  The array

        @return     The heap.
        """
        index = len(array) // 2
        self.current_size = len(array)
        self.heap = [0] + array
        while (index > 0):
            self.bubbleDown(index)
            index -= 1

    def satisfyMinHeapProperty(self, index, current_size):
        """
        @brief      recursive func satisfying min heap property

        @param      self          The object
        @param      index         The index
        @param      current_size  The current size

        @return     { no return val; alters self.heap }
        """
        LC = 2 * index
        RC = 2 * index + 1
        smallest = index
        if(LC <= current_size and self.heap[LC] < self.heap[index]):
            smallest = LC
        if(RC <= current_size and self.heap[RC] < self.heap[smallest]):
            smallest = RC
        if smallest != index:
            self.swap(index, smallest)
            self.satisfyMinHeapProperty(smallest, current_size)

    def HeapSort(self, reverse=True):
        """
        @brief      { function_description }

        @param      self     The object
        @param      reverse  If true sorted in descending order

        @return     { sorted array }
        """
        # array to be returned
        sorted_arr = []
        # defined in constructor for heap
        current_size = self.current_size
        while current_size != 0:
            self.swap(1, current_size)
            sorted_arr.append(self.heap[current_size])
            current_size -= 1
            self.satisfyMinHeapProperty(1, current_size)
        # restore the object heap
        self.buildHeap(sorted_arr)
        return (sorted_arr if reverse else sorted_arr[::-1])


if __name__ == '__main__':
    """
    main block to execute tests
    """
    test = [1, 5, 3, 4, 6, 7, 5, 3]
    print(test)
    Heap = Heap()
    Heap.buildHeap(test)
    print(Heap.heap)
    sorted_arr = Heap.HeapSort()
    print(sorted_arr)
