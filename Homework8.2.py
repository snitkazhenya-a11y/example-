def is_palindrome(text: str) -> bool:
    clean_text = "".join(char.lower() for char in text if char.isalnum())
    return clean_text == clean_text[::-1]
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("OP"))
print(is_palindrome("a."))
print(is_palindrome("aurora"))