"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    ...
    def __init__(self, location):
        "Create serial generator from start point"
        self.words = []
        f = open(location)
        self.words = [x.strip() for x in f]
        
        print(f'{len(self.words)} words read')
    
    def __repr__(self):
        return f"This is a random word generator using a file location"
        
    
    def random(self):
        "Returns random word."
        return "".join(random.choices(self.words))


class SpecialWordFinder(WordFinder):

    def __init__(self, location):
        self.words = []
        f = open(location)
        self.words = [x.strip() for x in f if x.strip() and not x.startswith('#')]
        print(f'{len(self.words)} words read')