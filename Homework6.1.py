import string
start_char, end_char = input(" ").split('-')
all_letters = string.ascii_letters
start_index = all_letters.find(start_char)
end_index = all_letters.find(end_char)
result = all_letters[start_index : end_index + 1]
print(result)