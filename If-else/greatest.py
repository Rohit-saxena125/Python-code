# find the greatest number
a,b,c=map(int,input().split())
if a>b and a>c:
    print(a,"is greater")
elif b>a and b>c:
    print(b,"is greater")
else:
    print(c,"is greater")
