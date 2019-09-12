split_sentence = {}
sentence = input("text: ")
words = sentence.split()
for word in words:
    occurrence = split_sentence.get(word, 0)
    split_sentence[word] = occurrence + 1
words = list(split_sentence.keys())
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}}: {}".format(word, max_length, split_sentence[word]))
