sentence = input()

list_sentence = {word:len(word) for word in sentence.split()}
print(list_sentence)