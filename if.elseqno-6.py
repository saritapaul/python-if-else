# write a python program to check whether a year is leap year or not.
year=int(input("enter any year"))
if year%4==0:
    print("it is a leap year")
elif year%100!=0 and year%400==0:
    print("it is leap year and century year")
else:
    print("it is not a leap year")