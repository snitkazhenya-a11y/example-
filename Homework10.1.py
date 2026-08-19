def sequence(func, first, n):
    current = first
    for _ in range(n):
        yield current
        current = func(current)
def rule(x):
    return x ** 2
print(list(sequence(rule, 2, 4)))