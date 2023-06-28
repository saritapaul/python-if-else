#write a program to calculate the electricity bill 
unit=int(input("enter the unit-"))
if unit<=100:
    print("no charge")
elif 100<unit<=200:
    print(unit-100*5)
elif unit>200:
    print(unit-100*10)
else:
    print("no unit")