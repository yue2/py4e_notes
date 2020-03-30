#Write a program that repeatedly prompts a user for integer numbers
#until the user enters 'done'.
#Once 'done' is entered, print out the largest and smallest of the numbers.
#If the user enters anything other than a valid number catch it with
#a try/except and put out an appropriate message and ignore the number.
#Enter 7, 2, bob, 10, and 4 and match the output below.

#initalize
smallest = None
largest = None
entry = None

#loop
while True:
    entry = input("Enter an integer:")
    if entry == "done":
        break
    try:
        number = int(entry)
    except:
        print("Invalid input")
        continue
    if number>largest:
        largest = number
    elif smallest == None:
        smallest = number
    elif number<smallest:
        smallest = number

#output
print("Maximum is", largest)
print("Minimum is", smallest)
