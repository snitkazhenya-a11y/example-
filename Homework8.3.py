def find_unique_value(numbers: list) -> list:
    for num in numbers:
        if numbers.count(num) == 1:
            return num
print(find_unique_value([1, 3, 1, 1]))
print(find_unique_value([4, 3, 4, 5, 3, 3, 3]))
print(find_unique_value([5, 2, 5, 5, 1.5]))