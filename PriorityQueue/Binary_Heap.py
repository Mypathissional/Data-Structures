from PriorityQueue import Priority_Queue
from interface import implements

class  Binary_Heap(implements(Priority_Queue)):
    "Binary Heap implementation of Priority Queue"
    class Node:
        def __init__(self,value,right=None,left=None):
            self.value = value
            self.right = right
            self.left = left

    def __init__(self,root=None):
        self.root = root


    def is_empty(self):
        " Checks whether Queue is empty "
        return self.root is None

    def insert(self, key):
        """
        Insert a key into Queue
        :param key:
        :return:
        """
        if self.root:

        else:
            self.root = Binary_Heap.Node(key)

    def min(self):
        """
        :return: the minimum element of the Queue
        """
        pass

    def replace_key(self,key,new_value):
        """
        Change the value of the key into new_value
        :param key: existing key
        :param new_value: the new_value of the key
        :return:
        """
        pass

    def extract_min(self):
        """
        Extracts the min
        :return:
        """
