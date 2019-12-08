import sys
import os
from hints.time_gists import timeFormat

firstNumber = 2
secondNumber = 3
secondNumber.date = 22

def multiFunc(firstNumber, secondNumber):
    multiResult = firstNumber * secondNumber
    time = timeFormat('%d-%m-%Y / %H:%M:%S')
    print(time)
    return multiResult
    pass

print("The multiply result is: %d" + multiFunc(firstNumber, secondNumber))
