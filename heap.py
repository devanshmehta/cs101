"""Contains the heap data structure and 
    algorithm on that data structure."""
    
__author__ = 'devansh.mht@gmail.com'

class Heap(object):
  
  """Heap which consists of numbers"""
  
  def __init__(self, heap = []):
    self.__heap = heap
    
  def build_heap(self):
      """builds the heap"""
      pass
  
  def max_heapify(self, i, max_size = 0):
    """assumes both the left and right subtree 
       are max heapify. Max size is zero if we want to 
       operate on the entire heap"""
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

  def sift_up(self, index):
    parent_index = index // 2
    if self.__heap[parent_index] < self.__heap[index]:
      temp = self.__heap[parent_index]
      self.__heap[parent_index] = self.__heap[index]
      self.__heap[index] = temp
      self.sift_up(parent_index)

  def insert(self, i):
    """inserts element i in the heap"""
    self.__heap.append(i)
    index = len(self.__heap) - 1
    self.sift_up(index)
    
  def peek(self):
    """returns the current max element of the heap. 
       This method does not extract the max element"""
    return self.__heap[1]
  
