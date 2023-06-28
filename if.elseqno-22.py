#A company dedcided to give a bonus of 5% to an employee if hyis/her year of service is more than 5 year .
salary=int(input("enter salary"))
year_of_service=int(input("enter service year"))
if year_of_service>5:
    print(salary*5/100+salary)
else:
    print("no bonus")