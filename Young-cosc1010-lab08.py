# Ruby Young 
# UWYO COSC 1010
# 10th November
# Lab 08
# Lab Section: 16 
# Sources, people worked with, help given to: Professor Radosevich, Isabella Cardoso


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def adv_convert(num):
    negative = False
    if num[0] == '-':
        negative = True
        num = num.replace('-','')
    if '.' in num:
        numsplit = num.split('.') #[somenumber, somenumber]
        if len(numsplit) == 2 and numsplit[0].isdigit() and numsplit[1].isdigit():
            if negative:
                return -1*float(num)
            else: 
                return float(num)
        else:
            return False
    elif num.isdigit(): 
        if negative:
            return -1*int(num)
        else:
            return int(num)
    return False

print("*" * 75)

# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false


def slope_intercept(m, b, lower_bound_x, upper_bound_x):
    y = []
    if type(lower_bound_x) is int and type(upper_bound_x) is int and int and type(m) is int and type(b) is int and lower_bound_x <= upper_bound_x:
        for x in range(lower_bound_x, upper_bound_x+1):
            y.append((m*x)+b)
    else:
        return False
    return y

print("*" * 75)

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list\]


while True:
    m = input('Enter an integer to be the slope of the linear equation: (or enter exit to stop) ')
    if m.lower() == 'exit':
        break 

    b = input('Enter an integer to be the y-intercept of the linear equation: (or enter exit to stop) ')
    if b.lower() == 'exit':
        break

    lower_bound = input('Enter the lowest x-number you want to solve for: (or enter exit to stop) ')
    if lower_bound.lower() == 'exit':
        break 

    upper_bound = input('Enter the largest x-number you want to solve for: (or enter exit to stop) ')
    if upper_bound.lower() == 'exit':
        break

    m = adv_convert(m) 
    b = adv_convert(b) 
    lower_bound = adv_convert(lower_bound) 
    upper_bound = adv_convert(upper_bound) 

    y = slope_intercept(m, b, lower_bound, upper_bound)
    print(f"The list of all the values for u for given x-range is {y}")


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

#Redo this to make if run for the quadratic formula 


def square_root(a, b, c):
    """Does the square root operation"""
    if type(a) is int and type(b) is int and type(c) is int: 
        x = (b**2)-(4*a*c)
        if x < 0:
            return False
        else: 
            return x ** (1/2)
        #want to make it go into the next function 

def quadratic_formaula(a, b, c):
    """Quadratic formula"""
    if type(a) is int and type(b) is int and type(c) is int: 
        x = square_root(a, b, c)
        if x == False:
            print("The square root is negative")
            print(x)
            return None, None 
        else: 
            y1 = (-b-x)/(2*a)
            y2 = (-b+x)/(2*a)
        return (y1, y2) 
    else:
        return None, None
    
while True:
    a = input('Enter an integer to be the leading co-efficient of the quadratic equation: (or enter exit to stop)')
    if a.lower() == 'exit':
        break 
    b = input("Enter an integer to be the co-efficient of the 'x' term in the parabola: (or enter exit to stop)")
    if b.lower() == 'exit':
        break 
    c = input('Enter an integer to be the y-intercept of the parabola: (or enter exit to stop)')
    if c.lower() == 'exit':
        break 
    
    a = adv_convert(a) 
    b = adv_convert(b) 
    c = adv_convert(c) 
    
    y1, y2 = quadratic_formaula(a, b, c)
    print(f"The two outputs of the quadratic formula are {y1} and {y2}")
