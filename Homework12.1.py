def prime_generator(limit):
    for number in range(2, limit + 1):
        is_prime = True
        for divisor in range(2, int(number**0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            yield number
print(list(prime_generator(10)))