#take the age 3 people by user and deteermined oldest and youngest among them.
age=int(input("enter age-"))
age1=int(input("enter age1-"))
age2=int(input("enter age2-"))
if age>age1 and age>age2 and age1<age2:
    print("age is oldest and age1 is youngest")
elif age1>age and age1>age2 and age2<age1:
    print("age1 is oldest and age2 is youngest")
elif age2>age and age2>age1 and age<age2:
    print("age2 id oldest and age is youngest")
elif age1>age and age1>age2 and age2<age:
    print("age1 is oldest and age2 is youngest")
elif age2>age and age2>age1 and age1<age:
    print("age2 is oldest and age1 is youngest")
elif age2>age and age2>age1 and age<age1:
    print("age2 is oldest and age is youngest")
else:
    print("no oldest and youngest")