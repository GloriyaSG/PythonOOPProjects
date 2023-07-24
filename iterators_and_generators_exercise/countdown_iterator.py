class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.end = 0
        self.current = self.count + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == self.end:
            raise StopIteration
        self.current -= 1
        return self.current


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
