"""Python serial number generator."""


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

    def __init__(self, start=0):
        """
        Optional parameter start allows a specific first serial number to be entered

        n = SerialGenerator(100)
        """
        self.start = self.current = start

    def __repr__(self):
        return f"<SerialGenerator start={self.start}, next={self.start+1}>"

    def generate(self):
        """
        Increments start number by 1 and returns the current serial number.
        """
        self.current += 1
        return self.current - 1

    def reset(self):
        """
        Resets start number to original value
        """
        self.current = self.start
