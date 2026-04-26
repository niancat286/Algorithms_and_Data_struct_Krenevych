

class MaxHeap:

    def __init__(self,array: list[int]):
        self._items: list[int] = array
        self.bulid_heap()

    def bulid_heap(self):
        for i in range(len(self._items) // 2, -1 , -1):
            self.siftDown(i,len(self._items))

    def insert(self,item: int):
        self._items.append(item)
        self.siftUp(len(self._items) - 1)

    def extract_maximum(self) -> int:
        self.swap(0,-1)
        item = self._items.pop()
        self.siftDown(0,len(self._items))
        return item

    def parent(self,idx: int) -> int:
        return (idx - 1) // 2

    def leftChild(self,idx: int) -> int:
        return 2*idx + 1

    def rightChild(self,idx: int ) -> int:
        return 2*idx + 2

    def swap(self,idx1,idx2):
        self._items[idx1],self._items[idx2] = self._items[idx2], self._items[idx1]


    def siftUp(self,idx):
        i = idx
        while i > 0:
            parent = self.parent(i)
            if self._items[parent] >= self._items[i]:
                break
            self.swap(i,parent)
            i = parent

    def siftDown(self,idx, end):
        i = idx
        while self.leftChild(i) < end:
            left = self.leftChild(i)
            right = self.rightChild(i)
            if right < end and self._items[left] < self._items[right]:
                max_child = right
            else:
                max_child = left

            if self._items[max_child] <= self._items[i]:
                break

            self.swap(i,max_child)
            i = max_child

    def heap_sort(self):
        n = len(self._items)
        for i in range(1,n):
            self.swap(0,n-i)
            self.siftDown(0,n - i)




if __name__ == "__main__":
    with open("../../HW19_Bin_Heap/input.txt") as f:
        array = list(map(int,f.readline().split()))
        heap = MaxHeap(array)
        heap.heap_sort()
        print(*heap._items)
