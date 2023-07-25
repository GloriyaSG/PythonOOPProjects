def vowel_filter(function):
    vowels = ['a', 'e', 'o', 'u', 'i']
    def wrapper():
        return [letter for letter in function() if letter in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]
print(get_letters())