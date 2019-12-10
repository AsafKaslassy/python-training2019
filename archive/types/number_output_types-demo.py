# http://lifemichael.com/moodle/mod/assign/view.php?id=13975

number = input("Note: Only numbers allowed.\nPlease enter a number:")
result = number

if not result.isdigit():
    print("Please insert a number only!")
else:
    bin_result = int(number)
    print("the binary representation is")
    print("Type of is: {0}".format(type(result)))
    print("Binary: {0:b} (Base 2)".format(bin_result))
    print("Decimal: {0:d} (Base 10)".format(bin_result))
    print("Octa: {0:o} (Base 8)".format(bin_result))
    print("Hex: {0:x} (Base 16)".format(bin_result))
    print("===============================")
    # print("the binary representation is %s" % result)
