"""Contains the heap data structure and 
    algorithm on that data structure."""
    
__author__ = 'devansh.mht@gmail.com'

class Heap(object):
  
  """Heap which consists of numbers"""
  
  def __init__(self, heap = [0]):
    self.__heap = heap
    self.heap_size = len(heap) - 1
    
  def build_heap(self):
      """builds the heap"""
      mid = self.heap_size // 2
      for i in xrange(mid, 0, - 1):
        self.max_heapify(i)
    
  def heap_sort(self):
    """sorts the heap"""
    current_size = self.heap_size
    for i in xrange(1, self.heap_size):
      tmp = self.__heap[1]
      self.__heap[1] = self.__heap[current_size]
      self.__heap[current_size] = tmp
      current_size -= 1
      self.max_heapify(1, current_size)      
 
  def max_heapify(self, i, max_size = 0):
    """assumes both the left and right subtree 
       are max heapify. Max size is zero if we want to 
       operate on the entire heap"""
    if max_size == 0:
        max_size = self.heap_size
    if i < 1 or i > max_size:
        return
    left_child = 2 * i
    right_child = left_child + 1
    largest = i
    if (left_child <= max_size and 
        self.__heap[left_child] > self.__heap[largest]):
        largest = left_child
    if (right_child <= max_size and 
        self.__heap[right_child] > self.__heap[largest]):
        largest = right_child
    if largest != i:
        temp = self.__heap[i]
        self.__heap[i] = self.__heap[largest]
        self.__heap[largest] = temp
        self.max_heapify(largest, max_size)

  def extract_max(self):
    """extracts the max element from the heap"""
    max_element = self.__heap[1]
    last_element = self.__heap[-1]
    self.heap_size -= 1
    self.__heap[1] = last_element
    self.max_heapify(1)
    self.__heap.pop()
    return max_element
    
  def sift_up(self, index):
    if index == 1:
      return
    parent_index = index // 2
    if self.__heap[parent_index] < self.__heap[index]:
      temp = self.__heap[parent_index]
      self.__heap[parent_index] = self.__heap[index]
      self.__heap[index] = temp
      self.sift_up(parent_index)

  def insert(self, i):
    """inserts element i in the heap"""
    self.__heap.append(i)
    self.heap_size += 1
    self.sift_up(self.heap_size)
    
  def peek(self):
    """returns the current max element of the heap. 
       This method does not extract the max element"""
    return self.__heap[1]
  
  def print_heap(self):
    """prints the current heap"""
    new_line = False
    num_nodes = 1
    count = 0
    for index in xrange(1, self.heap_size + 1):
      new_line = False
      i = self.__heap[index]
      print i,
      count += 1
      if count == num_nodes:
        num_nodes *= 2
        count = 0 
        print
        new_line = True
    print
    if not new_line:
      print

def main():
  arr = [0,1,2,3,4,5,6,7,]
  heap = Heap(arr)
  heap.print_heap()
  heap.build_heap()
  heap.print_heap()
  print heap.extract_max()
  print heap.extract_max()
  print
  heap.print_heap()
  heap.insert(6)
  heap.insert(7)
  heap.insert(-1)
  heap.print_heap()
  print heap.extract_max()
  print heap.extract_max()
  heap.print_heap()
  heap.heap_sort()
  heap.print_heap()
  heap.build_heap()
  heap.print_heap()

if __name__ == '__main__':  
  main()
