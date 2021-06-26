# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}
 
# Text string
text = "Later in the course, you'll see how to use the collections Counter class."
for letters in text.casefold():
    if letters.isalnum():
        word_count[letters] = word_count.setdefault(letters, 0) +1

print(word_count)
# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)
