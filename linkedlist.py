# Linked list implementation in python 

__author__ = 'devansh.mht@gmail.com'

class Node:
    
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return "data: {0}".format(self.data)
                               
class LinkedList:

    def __init__(self, head = None):
        self.head = head
        self.tail = None

    def __len__(self):
        count = 0
        for i in self:
            count += 1
        return count

    def __iter__(self):
        tmp = self.head
        while tmp is not None:
            yield tmp
            tmp = tmp.next

    def add(self, data):
        '''adds node to the end of the list'''
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        return node

    def find(self, data):
        for i in self:
            if i.data == data:
                return i
        return None

if __name__ == '__main__':
    l = LinkedList()
    l.add(1)
    l.add(3)
    l.add(79)
    l.add(5)
    print len(l)
    print l.find(79)
