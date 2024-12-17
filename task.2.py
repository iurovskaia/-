a,b,c = (int(x) for x in input().split())
if a<b+c and b<a+c and c<a+b and a>abs(b-c) and b>abs(a-c) and c>abs(a-b):
    print('YES')
else:
    print('NO')