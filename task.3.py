a,b,c = (int(x) for x in input().split())
if a == 0:
    if b!= 0:
        print(-c/b)
    if c!= 0:
        print('-')
    else:
        print('all')
else:
    D = b**2 - 4 * a * c
    if D == 0:
        print (-b / (2 * a))
    if D > 0:
        print ((-b - D**0.5)/ (2 * a) , (-b - D**0.5)/ (2 * a))