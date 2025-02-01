# Question 3 EXTRA - check if a letter has been entered three times, account for lowercase/uppercase

word_dict = {}
word = input("Please enter a word: ").lower()

# If the word has been encountered once (not in dict) or twice (logged as one in dict)
while word not in word_dict or word_dict[word] != 2:

    # If the word isnt in the dict, add it
    if word not in word_dict:
        word_dict[word] = 1

    # If the word is in the dict, append the existing value
    else:
        word_dict[word] += 1

    word = input("Please enter a word: ").lower()

print(f"You entered the word {word} 3 times")