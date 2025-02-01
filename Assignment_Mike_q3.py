word_list = []
word = input("Please enter a word: ")

while word not in word_list:
    word_list.append(word)
    word = input("Please enter a word: ")

print(f"You entered the word {word} twice")