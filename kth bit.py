import math
t=int(input())
for i in range(t):
    n,k=map(int(),input())
    p=math.pow(2,k)
    p=int(p)
    c=(n|p)
    print(c)