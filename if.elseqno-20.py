#  write a python program to input electricity unit charges and calculate total electricity billaccordeing to the given condition
#for 1st 50 unit Rs-0.50/unit.
unit=int(input("enter amount"))
if unit<=50:
    print(unit*0.50+20/100)
elif unit>=50 and unit<=150:
    print(unit*0.75+20/100)
elif unit>=150 and unit<=250:
    print(unit*1.20+20/100)
elif unit>=250:
    print(unit*1.50+20/100)
else:
    print("no charge")