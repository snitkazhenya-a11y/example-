def popular_words(text, words):
    text = text.lower() .split()
    result = {}
    for word in words:
        result[word] = text.count(word)
    return result
text = ("""When I was One
        I had just begun
        When I was Two
        I was nearly new""")
words = ["i", "was", "three", "near"]
print(popular_words(text, words))
