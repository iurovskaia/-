N = int(input())
a = [int(x) for x in input().split()]
X= int(input())
count=0
for i in range (len(a)):
    if a[i]==X:
        count+=1
print (count)