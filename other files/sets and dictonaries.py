sentance = input("""enter a sentence to count its word frequency :""")
word_f = {}
words = sentance.lower().split()

for word in words:
    word = word.strip('.,!?')
    if word in word_f:
        word_f[word] += 1
    else:
        word_f[word] = 1

for word, count in word_f.items():
    print(f" the word '{word}' occured : {count} times")