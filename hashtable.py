#hash table with chaining

__author__ == 'devansh.mht@gmail.com'

def hash(i, table_size):
  pass

class Node:
  
  def __init__(self, data = None, next = None):
    self.data = data
    self.next = next

class HashTable:
  
  def __init__(self, size):
    self.size = size
    self.table = [None] * size
    
  def insert(self, i):
    hash_value = hash(i, size)
    head = self.table[hash_value]
    #insert at tail
    if not head:
      node = Node(i, None)
      self.table[hash_value] = node
      return True
    else:
      # if the data is at head
      if head.data == i:
        return False
      prev_node = head
      current_node = head.next
      while current_node:
        if current_node.data == i:
          return False
        prev_node = current_node
        current_node = current_node.next
      node = Node(i, None)
      prev_node.next = node
      return True
      
  def search(self, i):
    hash_value = hash(i, size)
    head = self.table(i, size)
    tmp = head
    while tmp:
      if tmp.data == i:
        return True
      tmp = tmp.next
    return False
  
  def delete(self, i):
    pass
    
