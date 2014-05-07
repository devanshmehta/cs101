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
    values = self.table[hash_value]
  
  def search(self, i):
    hash_value = hash(i, size)
    values = self.table(i, size)
  
  def delete(self, i):
    pass
    
