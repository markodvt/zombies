import heapq

class Priority_queue:
    '''Priority 1 is a higher priority than Priority 2, etc. Ties go to the oldest item with the same (lowest) priority, so it respects FIFO among items with equal priority.
    '''
    def __init__(self):
        self._data = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._data, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._data)[-1]

    def empty(self):
        return not self._data

    @classmethod
    def TestMe(cls):
        print(f'{'='*40}\nTesting class: {cls.__name__}\n{'='*40}')
        print(f'Pushing 4 items (Item A, Item B, Item C, Item D) onto Priority_queue ... with priorities 3, 1, 2, 1')

        pq = Priority_queue()
        pq.push("Task A", 3)
        pq.push("Task B", 1)
        pq.push("Task C", 2)
        pq.push("Task D", 1)
        
        print('Popping off ... expected order B, D, C, A')

        while not pq.empty():
            print(pq.pop())
        # Expected output:
        # Task B
        # Task D
        # Task C
        # Task A

def main():
    Priority_queue.TestMe()

if __name__ == '__main__':
    main()
