#in this lesson we are going to learn about error handling


while True:
    try:
        x = int(input("Please enter a number: "))
        print(x+x*5)
        break
    except ValueError:
             print("Oops!  That was no valid number.  Try again...")
