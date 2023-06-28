# write a python program to check whether a triangle is valid or not.
a=int(input("enter first angle"))
b=int(input("enter second angle"))
c=int(input("enter third angle"))
total=a+b+c
if total==180:
    print("it is a valid triangle")
else:
    print("it is not a valid triangle")