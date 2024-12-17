N = int (input())
A=[int(x) for x in input().split()]
max = -float('inf')
for i in range(1, len(A)):
    if A[i] > max:
        max = A[i]
print(max)