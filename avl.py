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
  if b:
    b.parent = x
  x.parent = y
  x.height = max(height_node(a), height_node(b)) + 1
  y.height = max(height_node(x), height_node(c)) + 1
  return y
  
def right_rotate(node):
  '''right rotating avl node'''
  y = node
  x = y.left_child    
  a = x.left_child
  b = x.right_child 
  c = y.right_child
  y.left_child = b
  x.right_child = y
  y.parent = x
  if b:
    b.parent = y
  y.height = max(height_node(b), height_node(c)) + 1
  x.height = max(height_node(a), height_node(y)) + 1
  return x
  
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
  elements.append(node)
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
      print "parent"
      print node.parent
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

def get_height_diff(node):
  return height_node(node.left_child) - height_node(node.right_child)
    
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
  diff = abs(get_height_diff(node))
  if diff > 1 and node.left_child and i < node.left_child.data:
    return right_rotate(node)
  if diff > 1 and node.right_child and i > node.right_child.data:
    return left_rotate(node)
  if diff > 1 and node.left_child and i > node.left_child.data:
    left_rotate(node.left_child)
    return right_rotate(node)
  if diff > 1 and node.right_child and i < node.right_child.data:
    right_rotate(node.right_child)
    return left_rotate(node.left_child)
  return node
  
class AvlNode:
  
  def __init__(self, data, parent = None, left_node = None, 
               right_node = None, height = 0):
    self.left_child = left_node
    self.right_child = right_node
    self.height = height
    self.data = data
    self.parent = parent

  def __repr__(self):
    return self.__str__()

  def __str__(self):
    ret_string = "height: " + str(self.height) 
    ret_string += " data: " + str(self.data)
    return ret_string

def main():
  elements = []
  head = AvlNode(10)
  head = insert_node(head, 8)
  head = insert_node(head, 7)
  head = insert_node(head, 6)
  head = insert_node(head, 5)
  head = insert_node(head, 4)
  #insert_node(head, 8)
  #print insert_node(head, 13)
  #print insert_node(head, 14)
  #print insert_node(head, 15)
  print successor(predecessor(head))
  print predecessor(successor(head))
  inorder_traversal(head, elements)
  print elements

if __name__ == '__main__':
  main()
