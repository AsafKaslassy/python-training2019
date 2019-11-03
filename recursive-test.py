# An example of a recursive function to
# find the factorial of a number
num = 4

def calc_factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        print(x)
        return (x * calc_factorial(x-1))

print("The factorial of", num, "is", calc_factorial(num))