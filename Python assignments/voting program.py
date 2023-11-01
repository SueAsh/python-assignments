#program to calculate eligibility to vote
age=int(input("enter your age:"))
nationality=input("enter your nationality:")
if nationality and age>=18:
    print("eligible for voting")
else:
    print("not eligible for voting")
