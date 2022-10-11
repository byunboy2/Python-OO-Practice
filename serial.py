class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """ Declare and initialize three variables. First two are assigned the
        start input and count is assigned -1 """
        self.start = start
        self.current_increment = -1

    def __repr__(self):
        return f"""Current start is ${self.start}, current_increment is
        ${self.current_increment} , and serial number is ${self.start +
        self.current_increment} """

    def generate(self):
        """ Increment count return current serial number """
        self.current_increment += 1
        return self.start + self.current_increment

    def reset(self):
        """ Reassign original values to each respective variables """
        self.current_increment = -1
