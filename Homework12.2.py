def generate_cobe_numbers(limit):
    number = 2
    while number ** 3 <= limit:
        yield number ** 3
        number += 1
print(list(generate_cobe_numbers(10)))
print(list(generate_cobe_numbers(100)))
print(list(generate_cobe_numbers(1000)))