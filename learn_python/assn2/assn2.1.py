"""
3.1 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use raw_input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.
"""

hrs = raw_input("Enter Hours: ")
rate = raw_input("Enter rate of pay: ")

try:
   h = float(hrs)
except:
   print "Hours entered should be a number."

try:
   r = float(rate)
except:
   print "Rate entered should be a number."



try:
    if h <= 40:
        print r * h
    else:
        ot = h - 40
        ot_pay = ot * (r * 1.5)
        total_pay = (r * 40) + ot_pay
        print total_pay
except:
    print "Sorry, bad data."
