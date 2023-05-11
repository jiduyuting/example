a=eval(input())
if a==0:
    print("0")
elif a>0:
    n=[]
    for i in range(a):
        b=int(input())
        n.append(b)
    sum(n)
    c=sum(n)/len(n)
    p=sum(i>=c for i in n)
    print(p)
else:
    print("illegal input")