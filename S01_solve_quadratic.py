'''
Author: Armstrong Subero
Program: solve_quadratic.py
Description:
 solves quadratic equations using the
 quadratic formula
 '''

# import square root function
from math import sqrt

#----------------------------------------
# Function solves quadratic equations
# using the quadratic formula
#----------------------------------------
def quad(a, b, c):
    x1 = (-b + sqrt(b**2-4*a*c))/ (2*a)
    x2 = (-b - sqrt(b**2-4*a*c))/ (2*a)
    
    return (x1, x2)


# test to solve 2x^2 + 7x - 15 = 0
# solve for x
result = quad(2, 7, -15)
print(result)