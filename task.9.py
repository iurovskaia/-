N = int (input())
A=[int(x) for x in input().split()]
min1 = float('inf')
for i in range(1, len(A)):
    if A[i] < min1:
        min1 = A[i]
        n=i=1
B = A.pop(n)
min2 = float('inf')
for i in range(1, len(B)):
    if B[i] < min2:
        min2 = B[i]
print(min1, min2)