from Binary_Heap import BinaryHeap
from  YoungTableu import Young_Tableu
import numpy as np
from time import time
n=25000
array = np.random.randint(0,n,n)

heap = BinaryHeap(n+4)
table = Young_Tableu(8000)

start = time()
for i in array:
    heap.insert(i)
end = time()
print 'heap insert' ,end-start

sort = []
start = time()


for i in range(n):
    sort.append(heap.min())
    heap.extract_min()
end = time()
print 'heap sort' ,end-start

print sort



start = time()
for i in array:
    table.insert(i)
end = time()
print 'table insert' ,end-start


sort = []
start = time()


for i in range(n):
    sort.append(table.min())
    table.extract_min()
end = time()
print 'Young sort' ,end-start

print sort
