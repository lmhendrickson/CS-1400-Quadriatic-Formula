# Written by: Liam Hendrickson 
# Written on: September 21st, 2017
# Purpose:
#         Take inputs of a, b, and c and produce some x by using the quadratic equation
#
#
#
#
import math


def quadratic():
    # Take inputs
    a = float(input("What is your a?  ")) 
    b = float(input("What is your b?  "))
    c = float(input("What is your c?  "))

    #Check a
    if a == 0:
        print("\nError: Invalid value for a; a cannot be 0")

    #Check for squarerootof a negative number
    elif ((b**2) - (4*a*c)) < 0 :
        print("\nError: Squareroot of a negative number")

    #Do sqrt; store is (d)
    else:
        d = math.sqrt((b**2) - (4*a*c))

        #Addition to -b; store in (e)
        e = -b + d

        #Subtraction to -b; store in (f)
        f = -b - d

        #Results of addition; store in (g)
        g = e / (2*a)

        #Results of subtraction; store in (h)
        h = f / (2*a)

        #Print results
        print("\nx =", g, ",", h)
        
        
