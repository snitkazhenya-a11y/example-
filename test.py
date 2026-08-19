def spin_words(sentence: str) -> str:
    return " ".join(
        word[::-1] if len(word) >= 5 else word
        for word in sentence.split()
    )
print(spin_words("Hey fellow warriors"))
print(spin_words("This is a test"))
print(spin_words("This is another test"))