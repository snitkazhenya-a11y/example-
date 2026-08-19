#1
def first_word(text):
    text = text.replace(".", "").replace(",", "").replace("?", "")
    words = text.split()
    return words[0] if words else ""
print(first_word("Hello World"))
print(first_word("greetings, friends"))
print(first_word("don't touch it"))
print(first_word(".., and so on..."))
print(first_word("hi"))
print(first_word("Hello.World"))

#2
import re
def first_word(text):
    match = re.search(r"[a-zA-Z']+", text)
    return match.group(0) if match else ""
print(first_word("Hello World"))
print(first_word("greetings, friends"))
print(first_word("don't touch it"))
print(first_word(".., and so on..."))
print(first_word("hi"))
print(first_word("Hello.World"))