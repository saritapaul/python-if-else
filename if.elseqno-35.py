c=int(input("enter price"))
if c>100000:
    print(15/100*c)
elif c>50000 and c<=100000:
    print(10/100*c)
elif c<=50000:
    print(5/100*c)
else:
    print("no tax")