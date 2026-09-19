# Name: Brenton Perry
# Date: 2026-09-18
# Course: COMP 163
# Project 1: Paycheck Calculator
# Help: ChatGPT helped me understand the assignment requirements, like making a minimum of three commits, and checking that my formatting was readable and proper.

# Read four values from the user, in this order:
#   1. Employee name
employee_name = input("Employee name: ")
#   2. Hours worked
hours_worked = float(input("Hours worked: "))
#   3. Hourly rate
hourly_rate = float(input("Hourly rate: "))
#   4. Tax rate, as a percent (for example, 10 means 10%)
tax_rate = float(input("Tax rate: "))


# Then calculate:
#   gross pay     = hours worked * hourly rate
gross_pay = hours_worked * hourly_rate
#   tax withheld  = gross pay * (tax rate / 100)
tax_withheld = gross_pay * (tax_rate / 100)
#   net pay       = gross pay - tax withheld
net_pay = gross_pay - tax_withheld


# Then print the four required output lines.
print(f"Employee: {employee_name}")
print(f"Gross pay: ${gross_pay:.2f}")
print(f"Tax withheld: ${tax_withheld:.2f}")
print(f"Net pay: ${net_pay:.2f}")
