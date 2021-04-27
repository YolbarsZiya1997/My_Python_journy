def multiply(x, y):
    """
    Multiply the two given parameters x and y
    param: x , y 
    return: x*y
    """
    result = x * y
    return result


def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    """
    Return true if the input is a palindrome
    param: string 
    return: True or False
    """
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
    """
    Identifies a sentence to see if it is palindrome or not a
    needs the is_palindrome function to work
    param: sentence 
    return: True or False
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)


answer = multiply(18,3)
print(answer)



# word = input("Please enter a word to check: ")
# if palindrome_sentence(word): # to cancel the case sensitivity
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))


# answer = multiply(9.0,9.0)
# print(answer)

# print()

# for val in range(1,5):
#     two_times = multiply(2, val)
#     print(two_times)
    
