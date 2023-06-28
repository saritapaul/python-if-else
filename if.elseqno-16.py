#write a python program to check whether a triangle is equilateral,isosceles or scales triangle
x=int(input("enter angle"))
y=int(input("enter angle"))
z=int(input("enter angle"))
if x==y and y==z and z==x:
    print("it is equilateral")
elif x==y or y==z or z==x:
    print("it is isoscalen")
else:
    print("it is scalen")