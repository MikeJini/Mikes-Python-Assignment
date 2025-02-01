# Question 3 - Check if a word has been entered twice

word_list = []
word = input("Please enter a word: ")

# Run as long as the word hasn't been encountered already
while word not in word_list:
    word_list.append(word)
    word = input("Please enter a word: ")

print(f"You entered the word {word} twice")