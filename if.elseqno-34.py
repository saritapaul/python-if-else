#write a python program to check last digit of a number is divisible by 3 or not.
num=int(input("enter number"))
if num>0:
    a=num%10
    b=a%3
    print("lst digit is divisible by 3")
else:
    print("not divisible")