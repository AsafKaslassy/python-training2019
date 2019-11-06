loops = 0
boolean = True

MAXIMUM = 5
MINIMUM = 1

while (True):
    # 1. First take "." and multiply with <loops>
    print("." * loops, "|")

    if (boolean):
        """
        2. Check if boolean is True, if correct:
            - Add to loop 1
        2.1. Check if less than MAXIMUM
        2.2. If more than MAXIMUM, change boolean to False
        """
        loops += 1
        if (loops > MAXIMUM):
            boolean = False

    else:
        """
        3. Check if boolean is True, if correct:
            - Add to loop 1
        3.1. Check if less than MINIMUM 
        3.2. If less than MINIMUM, change boolean to True
        """
        loops -= 1
        if (loops < MINIMUM):
            boolean = True
    break
