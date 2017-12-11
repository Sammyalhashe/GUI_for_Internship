from maxHeapInheritance import maxHeap


class PQ(maxHeap):
    """[summary]

    [description]

    Extends:
        maxHeap
    """

    def __init__(self, key=None):
        super().__init__(key)


if __name__ == '__main__':
    pq = PQ()
    print(pq.heap)
