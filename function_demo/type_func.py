""" Global variables """

decimalType = 12.5
stringType = "abc"
arrayType = [4, 2, 53, "abnc"]
dictType = {'one': 'The One', 'two': 'Two Files'}
tupleType = (1, 'abc', 23, "A")
setType = {'a', 'b', 'c'}
booleanType = True

typesArray = [decimalType, stringType, arrayType, dictType, tupleType, setType, booleanType]

def showTypes(arraysize):
    """ This method prints all types of variables. """
    count = 0
    while count < arraysize:
        arrayposition = typesArray[count]
        print("Type of {} is: {}".format(arrayposition, type(arrayposition)))
        count += 1
        pass

arraySize = len(typesArray).numerator
showTypes(arraySize)
