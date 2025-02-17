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

        items = [("Task A", 3), ("Task B", 1), ("Task C", 2), ("Task D", 1)]

        print(f'Unpacking and pushing 4 items: {items} onto Priority_queue.\n')

        pq = Priority_queue()
        for i in items:
            pq.push(*i)
        
        print('Popping off ... expected order B, D, C, A')

        while not pq.empty():
            print(pq.pop())

def main():
    Priority_queue.TestMe()

if __name__ == '__main__':
    main()
