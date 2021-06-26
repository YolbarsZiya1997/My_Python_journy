text = "Do not think that you got it all. \nWhen ever you do, think back to this file, \nand see that you weren't even able to wrote this simple code"
print(text)

herip_sanighuch = {}

for letters in text.casefold():
    if letters.isalnum():
        herip_sanighuch[letters] = herip_sanighuch.setdefault(letters, 0) + 1

print(herip_sanighuch)

for letters, qetim in herip_sanighuch.items():
    print(letters, qetim)