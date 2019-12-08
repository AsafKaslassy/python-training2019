def spacing():
    addSpace = "-----------\n"
    print(addSpace)


class ScopeTesting:

    def toplevel(num):
        a = num  # Global variable but inside function only

        def nested():
            nonlocal a  # Adds the non-local variable to this nested function, without this, variable 'a' un-accessible.
            tempA = a
            a += 2
            print(
                f"toplevel, nested(), {tempA} + 2 = {a}")  # tries to print local variable a but its created after this line so exception is raised
            a = 7

        nested()
        print(f"toplevel, not nested() = {a}")

    def toplevel2(num):
        a = num  # variable inside function only

        def nested():
            a = 5 + 2
            print(
                f"toplevel2, nested(), a + 2 = {a}")  # tries to print local variable a but its created after this line so exception is raised

        print(f"toplevel2, not nested() = {a}")
        nested()

    def enclosedScope(num):
        number = num

        def outer(num):
            number = num + 1  # Inner scope

            def inner(num):
                number = num + 2
                print(f"def inner(num):{number}")

            inner(number)  # nested inner level
            print(f"def outer(num):{number}")

        outer(number)  # nested outer level
        print(f"def enclosedScope(num):{number}")  # function level


"""This is a functions initiation."""
spacing()
ScopeTesting.toplevel(5)
spacing()
ScopeTesting.toplevel2(5)
spacing()
ScopeTesting.enclosedScope(5)
spacing()
