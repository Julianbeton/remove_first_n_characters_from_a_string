# Exercise 4: Remove first n characters from a string

# Write a program to remove characters from a string starting from zero up to n and return a new string.

# For example:
# remove_chars("pynative", 4) so output must be tive. Here, we need to remove the first four characters from a string.
# remove_chars("pynative", 2) so output must be native. Here, we need to remove the first two characters from a string.

# Note: n must be less than the length of the string.

word = input("Enter a valid word: ")
print("The word is", word)

number_of_remove_characters = int(input("Enter how many first characters you want to remove in your word: "))
print("Number of the first characters you want to remove in your word:", number_of_remove_characters)

length_of_the_word = len(word)

for i in range(number_of_remove_characters, length_of_the_word, 1):
    print("\033[1;32;40m",word[i])