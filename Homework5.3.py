import string
text = input(" ")
for p in string.punctuation:
    text = text.replace(p, "")
words = text.title().replace(" ", "")
hashtag = "#" + words
hashtag = hashtag[:140]
print(hashtag)
