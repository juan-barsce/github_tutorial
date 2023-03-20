

def sandbox_function():
    return 5

def is_even_number(x: int):
    if type(x) is int:
        return x % 2 == 0
    else:
        raise ValueError('Incorrect input type')

