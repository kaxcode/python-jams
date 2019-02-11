def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return not (set(alphabet.upper()) - set(sentence.upper()))
