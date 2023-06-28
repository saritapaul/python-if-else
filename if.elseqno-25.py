# a student will not allowed to sit in exam if his/her attendance is less than 75%.
a=int(input("enter number of classes held"))
b=int(input("enter number of classes attendance"))
percentage=a*b/100
if percentage>=75:
    print("student allowed to sit in the exam hall")
else:
    print("student is not allowed to sit in exam")