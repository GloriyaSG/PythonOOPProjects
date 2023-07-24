class vowels:
    def __init__(self, string):
        self.string = string
        self.vowels_all = ['a', 'e', 'i', 'o', 'u', 'y']
        self.current = -1
        self.end_idx = len(self.string) - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current > self.end_idx:
            raise StopIteration()
        if self.string[self.current].lower() in self.vowels_all:
            return self.string[self.current]
        return self.__next__()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
