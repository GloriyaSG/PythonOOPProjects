class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.sequence) < self.number:
