num=int(input("enter no-"))
num2=int(input("enter no-"))
operator=input("enter operator")
if operator=="+":
    print(num+num2)
elif operator=="-":
    print(num-num2)
elif operator=="*":
    print(num*num2 )
elif operator=="**":
    print(num**num2)
elif operator=="/":
    print(num/num2)
elif operator=="//":
    print(num//num2)
elif operator=="%":
    print(num%num2)
else:
    print("no operator")