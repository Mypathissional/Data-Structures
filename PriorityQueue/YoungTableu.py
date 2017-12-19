from interface import implements
import numpy as np
import math
from PriorityQueue import Priority_Queue

class Young_Tableu(implements(Priority_Queue)):

    "Young Tableu implementation of Priority Queue"

    def __init__(self,n):
        self.n = n
        self.table = np.zeros((self.n,self.n))
        self.table.fill(float('inf'))
        self.table_size = self.n*self.n
        self.n_vacant_places = self.table_size

    def is_empty(self):
        " Checks whether Queue is empty "

        return self.table[0][0] == float('inf')

    def min(self):
        """
        :return: the minimum element of the Queue
        """
        return self.table[0][0]

    def __swap(self,a,b):
        return b,a

    def __restore_the_table(self,i,j,dir=1):
        """
        Restores the initial table
        :param i: coordiante in the x direction
        :param j: coordinate in the y direction
        :param dir: if up or left dir is 1 else down or right dir is -1
        :return:
        """
        while True:
            borders = {1: i * j, -1: (self.n - 1 - i) * (self.n - 1 - j)}

            is_border = borders[dir] == 0

            if not is_border:
                maximum = dir*max( dir*self.table[i][j - dir],dir*self.table[i-dir][j ])
                if dir*self.table[i][j] < dir*maximum :
                    if self.table[i][j-dir] == maximum:
                        self.table[i][j], self.table[i][j - dir] = self.__swap(self.table[i][j], self.table[i][j - dir])
                        j -= dir
                    else:
                        self.table[i][j], self.table[i - dir][j] = self.__swap(self.table[i][j], self.table[i - dir][j])
                        i -= dir
                else:
                    break
            else :
                if i > 0 and self.n-1-i>0:
                    if dir*self.table[i][j] < dir*self.table[i - dir][j]:
                        self.table[i][j], self.table[i - dir][j] = self.__swap(self.table[i][j], self.table[i - dir][j])
                        i -= dir
                    else:
                        break
                elif j > 0 and self.n-1-j:
                    if dir*self.table[i][j] < dir*self.table[i][j - dir]:
                        self.table[i][j], self.table[i][j - dir] = self.__swap(self.table[i][j],
                                                                             self.table[i][j - dir])
                        j -= dir
                    else:
                        break
                else:
                    break

    def insert(self,key):
        """
        Inserts the key if place is available and restores the table
        :param key:
        :return:
        """
        if self.n_vacant_places:

            closest_index = int(math.sqrt(self.table_size-self.n_vacant_places))
            self.table[closest_index][closest_index] = key
            self.n_vacant_places -=1
            i,j = closest_index,closest_index
            self.__restore_the_table(i,j)

        else:
            print("Postoy, pogodi, ne stuchi ti v kolesa")

    def find_key(self,key):
        """
        :param key:
        :return: if the key exists return the coordinate tuple, else returns False
        """
        i,j = self.n-1,0

        while j<self.n and i>0:
            if self.table[i][j] == key:
                return (i,j)

            if self.table[i][j]>key:
                i -=1   # move up
            else:
                j +=1   #move right
        return False


    def replace_key(self, key, new_value):
        """
        Change the value of the existing key into new_value
        :param key: existing key
        :param new_value: the new_value of the key
        :return:
        """
        found_ind = self.find_key(key)
        dir = 1 if key>new_value else -1
        if found_ind:
            i,j = found_ind
            self.table[i][j]= new_value
            self.__restore_the_table(i,j,dir=dir)

    def extract_min(self):
        """
        Extracts the min and restores the original table
        :return:
        """
        if not self.is_empty():
            self.n_vacant_places +=1
            self.table[0][0] = float('inf')
            self.__restore_the_table(0,0,dir=-1)


