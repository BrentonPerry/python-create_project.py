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


# Hours worked and the hourly rate can have a fraction in them, like 37.5
# hours or 10.25 hours. Use float() for all three numbers, not int().
# int("37.5") crashes.
#
# Then calculate:
#   gross pay     = hours worked * hourly rate
#   tax withheld  = gross pay * (tax rate / 100)
#   net pay       = gross pay - tax withheld
#
# Then print the four required output lines.
# The exact format is in README.md. Match it exactly or the tests will fail.
#
# Chapters 1 and 2 only. Use variables, input(), arithmetic, type conversion,
# and print(). Do not use if statements, loops, functions, or imports.
# Your code runs top to bottom, once.
