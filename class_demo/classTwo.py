
class Rectangle:
    def __init__(self, w, h):
        """ This method receives numbers from Rectangle class.

        Parameters:
            arg1 (int): height: height counter
            arg2 (int): width: width counter

        Returns:
            int: width * height
        """
        self.width = w
        self.height = h

    def area(self):
        """
        This method calculates numbers from Rectangle class.

        Parameters:
            arg1 (int): height: height counter
            arg2 (int): width: width counter

        @return: Returns:
            int: width * height
        """
        return self.width * self.height