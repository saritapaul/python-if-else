#A shop keeper will give discount of 10% if the cost of the purchased quantity it more than 1000,ask user for quantity ,suppose one unit will cost100 judge and printtotal cost for user.
quantity=int(input("enter quantity"))
if quantity>1000:
    print(quantity-(10*quantity)/100)
else:
    print("no quantity")