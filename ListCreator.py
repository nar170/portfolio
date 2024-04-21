l = []

# This is what I would do if I was assigned it
# Except I added in error handling cause I was bored
#The Goal of this is to build a list by asking the user what number they want to add

while True:
    try:
        number = int(input("Enter a value: "))
        if number == 0:
            print("Exit value entered. Process ending.")
            print(l)
            break
        else:
            l.append(number)
        print(l)
    except ValueError:
        print("STOP THAT STOP IT NOW ENTER A NUMBER!!!!!!!!!!!!!!")


