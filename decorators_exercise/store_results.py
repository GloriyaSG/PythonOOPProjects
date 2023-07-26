

def store_results(func):
    FILE = "results.txt"

    def wrapper(*args):
        with open(FILE, "a") as file:
            file.write(f"Function {func.__name__} was called. Result: {func(*args)}\n")
        return func(*args)
    return wrapper


@store_results
def add(a, b):
    return a + b\



@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)