"""Module for designing a stack-like data structure to push elements to\
the stack and pop the most frequent element from the stack."""
import collections

class FreqStack:
    """
    A class that implements a frequency stack."""
    def __init__(self):
        """
        Initializes the FreqStack with empty frequency and group dictionaries,
        and sets the maximum frequency to 0.
        """
        self.freq = collections.defaultdict(int)
        self.group = collections.defaultdict(list)
        self.max_freq = 0

    def push(self, x):
        """
        Pushes an element onto the stack."""
        self.freq[x] += 1
        existing_freq = self.freq[x]

        if existing_freq > self.max_freq:
            self.max_freq = existing_freq

        self.group[existing_freq].append(x)

    def pop(self):
        """
        Removes and returns the most frequent element from the stack."""
        x = self.group[self.max_freq].pop()

        self.freq[x] -= 1

        if not self.group[self.max_freq]:
            self.max_freq -= 1

        return x
