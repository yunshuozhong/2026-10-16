a,b=map(int,input().split())
if 0<a<=b:
    c=0
    while a<=b:
        c=c+a
        a+=1
    print(c)