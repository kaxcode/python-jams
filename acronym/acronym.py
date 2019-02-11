def abbreviate(words):
    split_words = words.replace("-", " ").replace("_", "").split()
    words = [w.replace('-', ' ') for w in split_words]
    letters = [word[0] for word in words]
    return("".join(letters).upper())
