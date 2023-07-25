from math import sqrt

def get_primes(numbers: list):
    for num in numbers:
        if num <= 1:
            continue

        for divisor in range(2, int(sqrt(num)) + 1):
            if num % divisor == 0:
                break
        else:
            yield num

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))