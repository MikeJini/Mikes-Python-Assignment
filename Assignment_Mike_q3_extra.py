word_dict = {}
word = input("Please enter a word: ").lower()

while word not in word_dict or word_dict[word] != 2:

    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1

    word = input("Please enter a word: ").lower()

print(f"You entered the word {word} 3 times")