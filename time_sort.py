import time
import random
def timer(sort, A):
    start_time = time.time()
    A = sort(A)
    end_time = time.time()
    res = end_time - start_time
    return res
def bubble_sort(A):
    for j in range (1,len(A)):
        for i in range (0, len(A)-j):
            if A[i]>A[i+1]:
                A[i],A[i+1]=A[i+1],A[i]
    return A
def find_max_number(A):
    n=0
    for i in range (len(A)):
        if A[i]>=A[n]:
            n=i
    return n
def selection_sort(A):
    for i in range(len(A)-1):
        m=find_max_number(A[:len(A)-i])
        f=len(A)-1-i
        A[m],A[f]=A[f],A[m]
def insertion_sort(A):
    for i in range(1,len(A)):
        j=i
        while j>0 and A[j-1]>A[j]:
            A[j],A[j-1]=A[j-1],A[j]
            j-=1
counts=[i for i in range (1,500)]
res_time_bubble=[]
res_time_select=[]
res_time_insertion=[]
for n in range (1,500):
    random_numbers = [random.randint(0, 10) for i in range(n)]
    res_time_bubble.append(timer(bubble_sort, random_numbers))
    res_time_select.append(timer(selection_sort, random_numbers))
    res_time_insertion.append(timer(insertion_sort, random_numbers))
import numpy as np
import matplotlib.pyplot as plt
x = np.array(counts)
y1 = np.array(res_time_bubble)
y2=np.array(res_time_select)
y3=np.array(res_time_insertion)
plt.scatter(x, y1, color='blue')
plt.scatter(x, y2, color='red')
plt.scatter(x, y3, color='green')
plt.grid()

plt.show()
