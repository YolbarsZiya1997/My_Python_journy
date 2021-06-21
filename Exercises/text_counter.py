word_count = {}

text = "Later in the course, you'll see how to use the collections Counter class."


for letters in text.casefold():
    if letters.isalnum():
        word_count[letters] = word_count.setdefault(letters, 0) + 1
    
for letter, count in sorted(word_count.items()):
    print(letter, count)



    



        
