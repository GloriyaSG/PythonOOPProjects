def tags(params):
    def decorator(func):
        def wrapper(*args):
            return f"<{params}>{func(*args)}</{params}>"
        return wrapper
    return decorator



@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))