def multiply(x, y):
    result = x * y
    return result


def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)


word = input("Please enter a word to check: ")
if palindrome_sentence(word): # to cancel the case sensitivity
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))


# answer = multiply(9.0,9.0)
# print(answer)

# print()

# for val in range(1,5):
#     two_times = multiply(2, val)
#     print(two_times)
    
