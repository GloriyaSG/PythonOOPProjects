from collections import deque

def reverse_text(string):
    string = deque(reversed(string))
    while string:
        yield string.popleft()

for char in reverse_text("step"):
    print(char, end='')