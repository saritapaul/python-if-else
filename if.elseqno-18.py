#write a python program tp input marks of five subject physics,chemistry,biology,mathmatics,and computer.calculate percentage and grade according to following.
#percentage>=80%:grade-B
#percentage>=70%:grade-C
#percentage>=60%:grade-D
#percentage>=50%:grade-E
physics=int(input("enter mark"))
chemistry=int(input("enter mark"))
biology=int(input("enter mark"))
mathematics=int(input("enter mark"))
computer=int(input("enter mark"))
total=physics+chemistry+biology+mathematics+computer
percentage=total/500*100
if percentage>=90:
    print("grade-A")
elif percentage>=80:
    print("grade-B")
elif percentage>=70:
    print("grade-C")
elif percentage>=60:
    print("grade-D")
elif percentage>=40:
    print("grade-E")
elif percentage<40:
    print("grade-F")
else:
    print("fail")    