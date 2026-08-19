import string
import keyword
def is_valid_variable_name(name):
    if name in keyword.kwlist:
        return False
    if name[0].isdigit():
        return False
    if any(char.isupper() for char in name):
        return False
    forbidden_chars = string.punctuation.replace('_', '')
    if any(char in forbidden_chars or char.isspace() for char in name):
        return False
    if name.count('_') > 1:
        return False
    if name == "_":
        return True
    return True
user_input = input("Введіть дані перевірки ")
print(is_valid_variable_name(user_input))