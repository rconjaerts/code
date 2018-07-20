class Min_Heap:
    def __init__(self):
        self.heap = []

    def heapify_up(self):
        curr_i = len(self.heap)-1
        upwards = True
        while upwards and not curr_i == 0:
            parent = self.get_parent(curr_i)
            if self.heap[parent] > self.heap[curr_i]:
                self.heap[parent], self.heap[curr_i] = self.heap[curr_i], self.heap[parent]
                curr_i = parent
            else:
                upwards = False
    
    def heapify_down(self):
        curr_i = 0
        downwards = True
        while downwards:
            curr_small = curr_i
            left = self.get_left_child(curr_i)            
            if left < len(self.heap) and self.heap[left] < self.heap[curr_small]:
                curr_small = left

            right = self.get_right_child(curr_i)
            if right < len(self.heap) and self.heap[right] < self.heap[curr_small]:
                curr_small = right
            
            if curr_small == curr_i:
                downwards = False
            elif curr_small == left:
                self.heap[curr_i], self.heap[left] = self.heap[left], self.heap[curr_i]
                curr_i = left
            else:
                self.heap[curr_i], self.heap[right] = self.heap[right], self.heap[curr_i]
                curr_i = right

    def add(self, new_val):
        self.heap.append(new_val)
        self.heapify_up()
    
    def remove(self):
        min = self.heap.pop(0)
        if self.heap:
            self.heap = [self.heap[-1]]+self.heap[:-1]
            self.heapify_down()
        return min
    
    def get_parent(self, i):
        return int(i/2)
    
    def get_left_child(self, i):
        return 2*i
    
    def get_right_child(self, i):
        return 2*i+1

    def heapify_list(self, l):
        for v in l:
            self.add(v)
    
h = Min_Heap()
h.heapify_list([4,6,9,2,4,5,33,6,19])
print(h.heap)
while h.heap:
    print(h.remove())