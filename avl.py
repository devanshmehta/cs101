"""Balanced binary tree. AVL Tree"""

__author__ = 'devansh.mht@gmail.com'

def height(node):
  if node == None:
    return 0
  else:
    left_height = height(node.left_child) + 1
    right_height = height(node.right_child) + 1
    if left_height > right_height:
      return left_height
    else: 
      return right_height

def inorder_traversal(node, elements = []):
  """inorder traversal of avl tree"""
  if not node:
    return
  inorder_traversal(node.left_child)
  elements.append(node.data)
  inorder_traversal(node.right_child)
  
def find_min(node):
  if not node:
    return -1
  tmp = node
  while tmp.left_child:
    tmp = tmp.left_child
  return tmp.data
  
def successor(node):
  """successor of the node. returns -1 if there is no successor"""
  def find_first_left_parent(node):
    if not node.parent:
      return -1
    else:
      parent = node.parent
      if parent.left_child == node:
        return parent
      else:
        return find_first_left_parent(parent)
        
  if node.right_child:
    return find_min(node.right_child)
  else:
    return find_first_left_parent(node)
    
def predecessor(node):
  """predecessor of the node. returns -1 if there is no predecessor"""
  def find_first_right_parent(node):
    if not node.parent:
      return -1
    else:
      parent = node.parent
      if parent.right_child == node:
        return parent.data
      else:
        find_first_right_parent(parent)
        
  if node.left_child:
    return find_max(node.left_child)
  else:
    return find_first_right_parent(node)

class AvlNode:
  
  def __init__(self, data, parent = None, left_node = None, 
               right_node = None, height = 0):
    self.left_node = left_node
    self.right_node = right_node
    self.height = height
    self.data = data
    self.parent = parent

class AvlTree:
  
  def __init__(self):
    self.head = None
  
  def insert(self, i):
    pass
  
  def delete(self, i):
    pass
  
  def find_min(self):
    node = self.head
    while node:
      node = node.left_child
    return node.data
  
  def find_max(self):
    node = self.head
    while node:
      node = node.right_child
    return node.data
  
  def predecessor(self):
    pass
  
  def sort_tree(self):
    sorted_elements = []
    inorder_traversal(self.head, sorted_elements)
    return sorted_elements
