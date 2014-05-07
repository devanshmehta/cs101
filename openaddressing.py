# open addressing hash table implementation

__author__ = 'devansh.mht@gmail.com'

def hash(value, index):
  pass

class OpenAddressing:
  
  def __init__(self, size):
    self.size = size
    self.table = [] * size;
    self.delete_me  = [] * size
    
  def insert(self, i):
    """inserts i in the hash table"""
    index = 0
    while index < self.size:
      hash_value = hash(i, index)
      if not self.table[hash_value] or self.delete_me[hash_value]:
        self.table[hash_value] = i
        return True
    return False
  
  def delete(self, i):
    pass
  
  def search(self, i):
    pass
