N = int(input())
a = [int(x) for x in input().split()]
b = [a[-1]]
for i in range (len(a)-1):
    b.append(a[i])
print(b)