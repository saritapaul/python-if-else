# write a python program to cfind the maximum between three numbers.
num=int(input("enter number"))
num2=int(input("enter number"))
num3=int(input("enter number"))
if num>num2 and num>num3:
    print("num is maximum")
elif num2>num and num2 >num3:
    print("num2 is maximum")
elif num3>num and num3>num2:
    print("num3 is maximum")
else:
    print("no maximum")