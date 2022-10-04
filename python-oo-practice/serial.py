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
    def __init__(self, start):
        "Create serial generator from start point"
        self.start = start
        self.original = start
    
    def __repr__(self):
        return f"This is a serial generator that starts at {self.original}"
    
    def generate(self):
        "Returns serial number"
        temp = self.start
        self.start += 1
        return temp
        
    
    def reset(self):
        "Resets counter to original start point."
        self.start = self.original



