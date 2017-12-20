from maxHeapInheritance import maxHeap


class PQ(maxHeap):
    """Put stuff in and take stuff out with Highest priority

    [Inherits from maxHeap class to remove with highest priority]

    Extends:
        maxHeap
    """

    def __init__(self, key=None):
        super().__init__(key)


if __name__ == '__main__':
    pq = PQ()
    print(pq.heap)
    pq.insert(4)
    pq.insert(2)
    pq.insert(6)
    pq.insert(89)
    print(pq.heap)
    pq.deleteMax()
    print(pq.heap)
