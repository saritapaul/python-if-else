#write a python program to calculate profit or loss.
actual_cost=int(input("enter amount"))
sale_cost=int(input("enter amount"))
if actual_cost<sale_cost:
    print("profit")
elif actual_cost>sale_cost:
    print("loss")
else:
    print("no profit and loss")