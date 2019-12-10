# http://lifemichael.com/moodle/mod/assign/view.php?id=5189
# https://www.youtube.com/watch?v=dRWdMjLe0aE
'''
variable = A if {condition} else B

result = A if False else B
Also can be seen like:
result = (A if False) (else B)

print("Yes" if True else "No")
'''

a = 3
b = 4


# Standart usage:
def standart_usage():
    helloval = "hello" if b > a else "salam"
    print(helloval)
    haifa = 'haifa' if b > a and b > 0 else 'ramat-gan'
    print(haifa)
    rehovot = 109 if a > b else 'rehovot'
    print(rehovot)
    telaviv = 'tel-aviv' if 'a' in ['a', 'b', 'c', 'd'] else 'rehovot'
    print(telaviv)
    rehovot2 = 'tel-aviv' if 'a' in 'abcd' else 'rehovot'
    print(rehovot2)
    color = 'blue' if 'b' not in "mosh" else 'red'
    print(color)
    winter = 'winter' if a > 2 and a % 2 == 1 else "summer"
    print(winter)
    yahoo = 123 if 'y' not in 'yahoo' else 'x'
    print(yahoo)


# standart_usage() # Uncomment to run.

# Advanced usage:
def advanced_usage():
    helloval = "hello"  # if b > a else "salam"
    print(f'{(helloval if b > a else "salam")}')

    haifa = 'haifa'  # if b > a and b > 0 else 'ramat-gan'
    print(f'{(haifa if b > a and b > 0 else "ramat-gan")}')

    rehovot = 109  # if a > b else 'rehovot'
    print(f'{(rehovot if a > b else "rehovot")}')

    telaviv = 'tel-aviv' if 'a' in ['a', 'b', 'c', 'd'] else 'rehovot'
    print(telaviv)

    rehovot2 = 'tel-aviv' if 'a' in 'abcd' else 'rehovot'
    print(rehovot2)

    color = 'blue' if 'b' not in "mosh" else 'red'
    print(color)

    winter = 'winter' if a > 2 and a % 2 == 1 else "summer"
    print(winter)

    yahoo = 123 if 'y' not in 'yahoo' else 'x'
    print(yahoo)


advanced_usage()


def dict_usage():
    first_place
