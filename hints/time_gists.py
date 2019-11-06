from datetime import *


"""
@:type int
@:return This variable returns time formatted: dd-MM-yyyy / HH:MM:SS
@:param The format should be: '%d-%m-%Y / %H:%M:%S'
"""


def timeFormat(theFormat):
    theTime = datetime.today().strftime()
    # date_and_time = '%d-%m-%Y / %H:%M:%S'
    # new_date_and_time = time.strftime('%d-%m-%Y / %H:%M:%S')
    try:
        new_date_and_time = theTime
        return new_date_and_time
    except:
        print("Error Print: ", BaseException.with_traceback())
        return None
    pass

print(timeFormat())
