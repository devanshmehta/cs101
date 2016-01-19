# This module contains two implementations of union find data structure
# 1) LinkedList and 2) forest

import collections
import linkedlist

__author__ = 'devansh.mht@gmail.com'

class LinkedList: 

    '''LinkedList implementation for union disjoint'''

    def __init__(self):
        self.members = {}

    def make_set(self, i):
        if i in self.members: 
            raise ValueError("{0} is already present".format(i))
        li = linkedlist.LinkedList()
        li.add(i)
        self.members[i] = li

    def _find(self, x):
        '''finds the leader of x'''
        if x not in self.members:
            return None
        li = self.members[x]
        return li

    def find(self, x):
        '''finds the leader of x'''
        return self._find(x).head.data
    
    def union(self, x, y):
        if x not in self.members:
            raise ValueError("{0} is not present".format(x))
        if y not in self.members:
            raise ValueError("{0} is not present".format(y))
        leaderX = self._find(x)
        leaderY = self._find(y)
        if leaderX == leaderY:
            return
        for i in leaderY:
            leaderX.add(i.data)
            self.members[i.data] = leaderX

if __name__ == '__main__':
   uf = LinkedList()
   for i in xrange(100):
       uf.make_set(i)
   
   uf.union(1, 3)
   print uf.find(3)
   uf.union(2, 8)
   uf.union(3, 8)
   print uf.find(8)

class Forest:
    
    '''Forest implementation of union disjoint'''

    def __init__(self):
        pass
    
    def find(self, x):
        pass

    def union(self, x, y):
        pass
