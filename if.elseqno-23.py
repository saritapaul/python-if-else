# A school has following rules for grading system :
#below 25-F
#25 to 45-E
#45 to 50-D
#50 to 60-C
#60 to 80-B
# above 80-A
num=int(input("enter number"))
if num<25:
    print("grade-F")
elif num>=25 and num<45:
    print("grade-E")
elif num>=45 and num<50:
    print("grade-D")
elif num>=50 and num<60:
    print("grade-C")
elif num>=60 and num<=80:
    print("grade-B")
elif num>80:
    print("grade-A")
else:
    print("not any valid number")