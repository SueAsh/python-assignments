#program to calculate discount
amount=float(input("enter the amount"))
if amount>=1000:
    discount=0.05*amount
    print("the discount is",discount)
else:
    print("no discount")
