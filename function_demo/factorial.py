def printingMethod(num):
    results = num

    if num == 0:
        return
    else:
        printing = print("{} * {} = {}".format(num, num, results))


def factorial(num):
    """This is factorial function.\n
        Parameters: \
            - num: integer
            - example: factorial(4) or facrotial(num=4)
    """
    if num == 0:
        printingMethod(num)
        return 1
    else:
        printingMethod(num)
        return factorial(num - 1) * num


print(factorial(4))
