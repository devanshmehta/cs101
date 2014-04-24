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
    
def set_node_height(node):
  if node == None:
    return
  left_height = height_node(node.left_child)
  right_height = height_node(node.right_child)
  node.height = max(left_height, right_height) + 1

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
    return -1
  else:
    left_height = height(node.left_child)
    right_height = height(node.right_child)
    return max(left_height, right_height) + 1

def inorder_traversal(node, elements = []):
  """inorder traversal of avl tree"""
  if not node:
    return
  inorder_traversal(node.left_child, elements)
  elements.append(node.data)
  inorder_traversal(node.right_child, elements)
  
def find_min(node):
  if not node:
    return None
  tmp = node
  while tmp.left_child:
    tmp = tmp.left_child
  return tmp

def find_max(node):
  if not node:
    return None
  tmp = node
  while tmp.right_child:
    tmp = tmp.right_child
  return tmp

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
  if i < node.data:
    node.left_child = insert_node(node.left_child, i)
    node.left_child.parent = node
  else:
    node.right_child = insert_node(node.right_child, i)    
    node.right_child.parent = node
  set_node_height(node)
  return node
  #fix avl tree

class AvlNode:
  
  def __init__(self, data, parent = None, left_node = None, 
               right_node = None, height = 0):
    self.left_child = left_node
    self.right_child = right_node
    self.height = height
    self.data = data
    self.parent = parent

  def __str__(self):
    ret_string = "height: " + str(self.height) 
    ret_string += " data: " + str(self.data)
    return ret_string

def main():
  elements = []
  head = AvlNode(10)
  insert_node(head, 11)
  insert_node(head, 9)
  insert_node(head, 12)
  insert_node(head, 8)
  print predecessor(successor(head))
  print successor(predecessor(head))
  inorder_traversal(head, elements)
  print elements

if __name__ == '__main__':
  main()
