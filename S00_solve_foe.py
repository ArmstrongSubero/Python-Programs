'''
Author: Armstrong Subero
Program: solve_foe.py
Description:
 solves first order equations of the form 
 ax + b = cx + d
 '''

#----------------------------------------
# Function solves first order equations
#----------------------------------------
def equation(a, b, c, d):
    return (d -b) / (a-c)


# test to solve 2x + 5 = 13
# solve for x
result = equation(2, 5, 0, 13)
print(result)