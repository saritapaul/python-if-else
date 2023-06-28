# write a python program to input any alphabet and check whether it is alphabet or not.
ch=int(input("enter any character"))
if ch>="a" and ch<="z" or ch>="A" and ch<="Z":
    print("it is alphabet")
else:
    print("it is not an alphabet")