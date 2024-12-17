a,b = (int(x) for x in input().split())
c,d = (int(x) for x in input().split())
if a == c or b == d or abs(a - c) == abs(b - d):
    print('YES')
else:
    print('NO')
