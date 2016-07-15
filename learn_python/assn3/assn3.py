"""
4.6 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. Award time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of time-and-a-half in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use raw_input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function.
"""

"""
code copied over from assn2.1 to be wrapped in a function
"""

def computepay():
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
            return total_pay
    except:
        return "Sorry, bad data."

p = computepay()
print p
