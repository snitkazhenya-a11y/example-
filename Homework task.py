#1. Рядки

def get_string_length(text: str) -> int:
    return len(text)
my_text = "Ну що, розпочнемо"
length = get_string_length(my_text)
print(f"Довжина рядка {length}")

def combine_strings(str1: str, str2: str) -> str:
    return str1 + str2
first_line = "Почнем" " "
second_line = "Писати"
result = combine_strings(first_line, second_line)
print (result)

#2.Числа
def get_square(number: int | float) -> int | float:
    return number ** 2
print(get_square(7))
print(get_square(3.5))

def get_sum(a: int, b: int) -> int:
    return a + b
print(get_sum(8, 15))

def divide_number(a: int, b: int) -> int:
    quotient = a // b
    remainder = a % b
    return quotient, remainder
result = divide_number(10, 13)
print(result)

#3. Списки
def get_average(numbers: list) -> float:
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
my_numbers = [15, 23, 30, 36, 43, 50]
result = get_average(my_numbers)
print(f"Середнє: {result}")

def get_common_elements(list1: list, list2: list) -> list:
    return list(set(list1).intersection(list2))
a = [3, 4, 7, 9, 12]
b = [5, 7, 9, 15]
common = get_common_elements(a, b)
print(f"the same: {common}")

#4. Словники
def print_dict_keys(my_dict: dict) -> list:
    print("Всі відомі ключі")
    for key in my_dict.keys():
        print(key)
user = {
    "name": "Євгеній",
    "age": "43",
    "city": "Львів"
}
print_dict_keys(user)


def merge_dicts(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result
d1 = {"a": 3, "b": 5}
d2 = {"c": 4, "d": 6}
print(merge_dicts(d1, d2))

#5.Множини
def merge_sets(set1: set, set2: set) -> set:
    return set1.union(set2)
a = {1, 2, 3}
b = {4, 5, 6}
result = merge_sets(a, b)
print(result)


def check_is_subset(subset: set, my_set: set) -> bool:
    return subset <= my_set
small = {1, 2, 3}
big = {4, 5, 6, 7}
other = {1, 8}
print(check_is_subset(small, big))
print(check_is_subset(other, big))

#6. Умовні вирази та цикли
def check_even_add(number: int) -> None:
    if number % 2 == 0:
        print(number)
    else:
        print(number)
check_even_add(5)
check_even_add(6)

def get_even_numbers_loop(numbers: list[int]) -> list[int]:
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result
print(get_even_numbers_loop([12, 16, 22, 28, 33, 44]))

#7. Лямбда
check_parity = lambda x: "парне" if x % 2 == 0 else "не парне"
print(check_parity(0))
print(check_parity(3))
print(check_parity(6))