# http://lifemichael.com/moodle/mod/assign/view.php?id=13975

list_of_numbers = (10, 20)
index = 0
average_list = 0

for i in list_of_numbers:
    print(list_of_numbers[index])

    average_list += list_of_numbers[index]
    index += 1

print((int)(average_list / len(list_of_numbers)))
