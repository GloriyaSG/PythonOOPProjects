class custom_range:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.stop:
            raise StopIteration
        else:
            current = self.start
            self.start += 1
            return current

one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)