"""Balanced binary tree. AVL Tree"""

__author__ = 'devansh.mht@gmail.com'

def max(a, b):
  if a > b:
    return a
  else:
    return b

def height_node(node):
  if node == None:
    return -1
  else:
    return node.height
    
def set_height_node(node):
  if node == None:
    return
  node.height = max(height_node(node.left_child), height_node(node.right_child)) + 1

def left_rotate(node):
  '''left rotating avl node'''
  x = node
  y = x.right_child
  a = x.left_child
  b = y.left_child
  c = y.right_child
  y.left_child = x
  x.right_child = b
  x.height = max(a.height, b.height) + 1
  y.height = max(x.height, c.height) + 1
  
def right_rotate(node):
  '''right rotating avl node'''
  y = node
  x = y.left_child
  a = x.left_child
  b = x.right_child 
  c = y.right_child
  y.left_child = b
  x.right_child = y
  y.height = max(b.height, c.height) + 1
  x.height = max(a.height, y.height) + 1
  
def height(node):
  if node == None:
    return 0
  else:
    left_height = height(node.left_child)
    right_height = height(node.right_child)
    return max(left_height, right_height) + 1

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
      return None
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
      return None
    else:
      parent = node.parent
      if parent.right_child == node:
        return parent
      else:
        return find_first_right_parent(parent)
        
  if node.left_child:
    return find_max(node.left_child)
  else:
    return find_first_right_parent(node)
    
def insert_node(node, i):
  if node == None:
    return AvlNode(i)
  if node.data < i:
    insert_node(node.left_child, i)
  else:
    return insert_node(node.right_child, i)
  set_node_height(node)
  //fix avl tree

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
  
  def sort_tree(self):
    sorted_elements = []
    inorder_traversal(self.head, sorted_elements)
    return sorted_elements
