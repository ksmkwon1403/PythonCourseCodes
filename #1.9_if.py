def plus(a, b):
    if type(b) == int or type(b) == float:
        return a + b
    else:
        return None

print(plus(1, 3.12351))