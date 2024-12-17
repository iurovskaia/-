n=int(input())
D=dict()
for i in range(n):
    x=input()
    if x in D:
        D[x]+=1
    else:
        D[x]=1
A=list(D.values())
A.sort(reverse=True)
k=int(input())
for i in range (k):
    for keys in D:
        if D[keys]==A[i]:
            print (keys, A[i])
            del D[keys]
            break
