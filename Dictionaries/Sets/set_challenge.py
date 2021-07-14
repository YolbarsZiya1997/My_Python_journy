# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

text = input("Speak up boi ! ")
alphabetically_sorted = set()

for letters in text.casefold():
    if letters not in "aeiou" and letters.isalnum():
        alphabetically_sorted.add(letters)

print(sorted(alphabetically_sorted))

# lets do it using sets

sample_text = input("Hello sweetie: ")

vowels = frozenset("aeiou")
final_set = set(sample_text).difference(vowels)

print(sorted(final_set))

# which I think using a set is much much easier 