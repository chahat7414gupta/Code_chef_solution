#### Solution of Sum it Problem Code:SUMM , Contest Code:START72

t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if (x+y==z):
        print('YES')
    else:
        print('NO')