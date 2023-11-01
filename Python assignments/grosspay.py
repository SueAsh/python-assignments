#promt the user for hour and rate per hours
hours_worked=float(input("enter the number of hours worked:"))
rate_per_hour=float(input("enter the rate per hour:"))

#calculate the gross pay
gross_pay=hours_worked*rate_per_hour

#print the gross pay
print("gross pay:",gross_pay)
