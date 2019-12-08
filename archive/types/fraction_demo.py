# Write a simple program that calculates the total of the following fractions: ¾, 1/7, ⅜, 5/9, ⅞ and 13/17.

import fractions
from math import floor

fraction = fractions.Fraction
math_operation = floor
list_of_fraction = (fraction(3, 4), fraction(1, 7), fraction(3, 8), fraction(5, 9))


def fractionsPrintListFunction(fractions_list):
    result = fractions_list
    newresult = 0
    for result in fractions_list:
        newresult += result
        print(result)
    return result


print("Type of fractions in the list:")
print(type(list_of_fraction))

print("List of fractions in the list:")
fractionsPrintListFunction(list_of_fraction)

print("Correct calculation:")
num_result_print = list_of_fraction[0].numerator + \
                   list_of_fraction[1].numerator + \
                   list_of_fraction[2].numerator + \
                   list_of_fraction[3].numerator
deno_result_print = list_of_fraction[0].denominator + \
                    list_of_fraction[1].denominator + \
                    list_of_fraction[2].denominator + \
                    list_of_fraction[3].denominator

result_print = fraction(num_result_print, deno_result_print)
print(result_print)

print("Wrong calculation:")
result_print2 = list_of_fraction[0] + \
                list_of_fraction[1] + \
                list_of_fraction[2] + \
                list_of_fraction[3]
print(result_print2)

print("Devision assignmnent:")
fraction_devision_list = (fraction(3, 4), fraction(1, 2))
result_devision = fraction_devision_list[0] / fraction_devision_list[1]
print(result_devision)
