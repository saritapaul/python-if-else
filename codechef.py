# t=int(input())
# i=1
# while i<=t:
#     # (n,x,y)=map(int,input().split())
#     n=int(input())
#     x=int(input())
#     y=int(input())
#     b=x*y
#     if (n-b)>0:
#         print("no")
#     else:
#         print("yes")
#     i+=1
t=int(input())
i=1
while i<=t:
    x=int(input())
    y=int(input())
    z=int(input())
    a=400/x
    b=400/y
    c=400/z
    if (a>b) and (a>c):
        print("alice")
    elif (b>a)and (b>c):
        print("bob")
    elif (c>a) and (c>b):
        print("carlie")