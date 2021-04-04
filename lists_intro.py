computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]
print(computer_parts)

#computer_parts[3] = "trackball"
print(computer_parts[3:])

computer_parts[3:] = ["trackball"]
# what is gonna happen is that the content of the iterable is 
# going to be added to the list 
print(computer_parts)

