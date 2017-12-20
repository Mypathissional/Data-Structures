from PriorityQueue import Priority_Queue
from interface import implements
import numpy as np
import math

class BinaryHeap(implements(Priority_Queue)):

    " Priority Queue Interface "

    def __init__(self,n=1000):
        self.n = n
        self.__X = np.zeros(self.n)
        self.__X.fill(float('inf'))
        self.__X[0] = float('-inf')
        self.__last_index  =0

    def __go_up(self,i):
        parent, child = self.__parent(i), i
        while self.__X[child] < self.__X[parent]:
            self.__X[child], self.__X[parent] = self.__swap(self.__X[child], self.__X[parent])
            child = parent
            parent = self.__parent(child)


    def __go_down(self,i):

        parent, min_child = i, 2 * i + np.argmin(self.__children(i))
        while self.__X[parent] > self.__X[min_child]:
            self.__X[parent], self.__X[min_child] = self.__swap(self.__X[parent], self.__X[min_child])
            parent = min_child
            min_child = 2 * parent + np.argmin(self.__children(parent))

    def __parent(self,i):
        return i/2

    def __left_child(self,i):
        return 2*i

    def __right_child(self,i):
        return 2*i+1

    def __children(self,i):
        return self.__X[2*i:2*i+2]

    def __swap(self,a,b):
        return b,a

    def is_empty(self):
        " checks whether the heap is empty"
        return self.__X[1] == float('inf')

    def insert(self, key):
        """
        Inserts a key into binary heap and restores the heap
        :param key:
        :return:
        """
        if self.n!=self.__last_index+1:
            self.__last_index +=1
            self.__X[self.__last_index] = key
            self.__go_up(self.__last_index)

    def min(self):
        """
        :return: the minimum element of the Queue
        """
        return self.__X[1]

    def replace_key(self,key,new_value):
        i=key
        """
        Change the value of the i-th elemenent in the binary heap into new_value
        :param key: existing key
        :param new_value: the new_value of the key
        :return:

        """

        if i< self.n:
            dir = 1 if new_value > self.__X[i] else -1
            self.__X[i] = new_value
            if dir:
                self.__go_down(i)
            else:
                self.__go_up(i)



    def extract_min(self):
        """
        Extracts the min
        :return:
        """
        if not  self.is_empty():
            self.__X[1] = self.__X[self.__last_index]
            self.__X[self.__last_index] = float('inf')
            self.__go_down(1)
            self.__last_index -=1





