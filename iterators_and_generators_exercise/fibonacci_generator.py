def fibonacci():
    first, second = 0, 1
    while True:
        yield first
        first, second = second, first + second


generator = fibonacci()
for i in range(5):
    print(next(generator))



