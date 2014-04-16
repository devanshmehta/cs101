"""Contains the heap data structure and 
    algorithm on that data structure."""
    
__author__ = 'devansh.mht@gmail.com'

class Heap(object):
  
  """Heap which consists of numbers"""
  
  def __init__(self):
    self.__heap = []
    
  def build_heap(self):
      """builds the heap"""
      pass
  
  def max_heapify(self, i):
    """assumes both the left and right subtree 
       are max heapify"""
    if i < 1 or i >= len(self.__heap):
        return
    left_child = 2 * i
    right_child = (2 * i) + 1
    largest = i
    if self.__heap[left_child] > self.__heap[largest]:
        largest = left_child
    if self.__heap[right_child] > self.__heap[largest]:
        largest = right_child
    if largest != i:
        temp = self.__heap[i]
        self.__heap[i] = self.__heap[largest]
        self.__heap[largest] = temp
        self.max_heapify(largest)

  def extract_max(self):
    """extracts the max element from the heap"""
    pass
    
  def insert(self, i):
    """inserts element i in the heap"""
    pass
  
  def peek(self):
    """returns the current max element of the heap. 
       This method does not extract the max element"""
       pass
  
