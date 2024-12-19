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
def merge(A,B):
    C = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i]<=B[j]:
            C.append(A[i])
            i+=1
        else:
            C.append(B[j])
            j+=1
    C += A[i:] + B[j:]
    return C
def merge_sort(A):
    if len(A) < 2:
        return A
    mid = len(A)//2
    left = A[:mid]
    right = A[mid:]
    return merge(merge_sort(left), merge_sort(right))
def qsort (A, left=0, right=None):
    if right is None:
        right = len(A) -1
    if left >= right:
        return
    i = left
    j = right
    pivot = A[left]
    while i <= j:
        while A[i] < pivot :
            i += 1
        while A[j] > pivot :
            j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
    qsort(A, left, j)
    qsort(A, i, right)
counts=[i for i in range (1,500)]
res_time_bubble=[]
res_time_select=[]
res_time_insertion=[]
res_time_merge=[]
res_time_qsort=[]
for n in range (1,500):
    random_numbers = [random.randint(0, 10) for i in range(n)]
    res_time_bubble.append(timer(bubble_sort, random_numbers))
    res_time_select.append(timer(selection_sort, random_numbers))
    res_time_insertion.append(timer(insertion_sort, random_numbers))
    res_time_merge.append(timer(merge_sort, random_numbers))
    res_time_qsort.append(timer(qsort, random_numbers))
import numpy as np
import matplotlib.pyplot as plt

x = np.array(counts)
y1 = np.array(res_time_bubble)
y2=np.array(res_time_select)
y3=np.array(res_time_insertion)
y4=np.array(res_time_merge)
y5=np.array(res_time_qsort)
mean_y1 = np.mean(y1)
mean_y2 = np.mean(y2)
mean_y3 = np.mean(y3)
mean_y4 = np.mean(y4)
mean_y5 = np.mean(y5)
plt.axhline(mean_y1, color='blue', linestyle='--')
plt.axhline(mean_y2, color='red', linestyle='--')
plt.axhline(mean_y3, color='green', linestyle='--')
plt.axhline(mean_y4, color='black', linestyle='--')
plt.axhline(mean_y5, color='yellow', linestyle='--')
plt.scatter(x, y1, color='blue', label='bubble sort')
plt.scatter(x, y2, color='red', label='select')
plt.scatter(x, y3, color='green',label='insertion')
plt.scatter(x, y4, color='black' , label='merge')
plt.scatter(x, y5, color='yellow', label='quicksort')
plt.xlabel('количество элементов')
plt.ylabel('время сортировки')
plt.title('Зависимость скорости сортировок от количества элементов списка')
plt.legend()
plt.grid()
plt.show()
