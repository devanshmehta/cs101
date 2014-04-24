"""Balanced binary tree. AVL Tree"""

__author__ = 'devansh.mht@gmail.com'

class AvlNode:
  
  def __init__(self, data, left_node = None, right_node = None, height = 0):
    self.left_node = left_node
    self.right_node = right_node
    self.height = height
    self.data = data

class AvlTree:
  
  def __init__(self):
    self.head = None
  
  def insert(self, i):
    pass
  
  def delete(self, i):
    pass
  
  def find_min(self):
    pass
  
  def find_max(self):
    pass
  
  def successor(self):
    pass
  
  def predecessor(self):
    pass
  
  def sort_tree(self):
    pass
