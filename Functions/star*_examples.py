numbers = (0, 1, 2, 3, 4, 5)

# print(numbers, sep=";")
# print(*numbers, sep=";")
# print(0, 1, 2, 3, 4, 5, sep=";")


def test_star(*args): # the * here helps us to put multiple arguments into our function
    print(args)
    for x in args:
        print(x)


test_star(0, 1, 2, 3, 4, 5)
print()

test_star()