#worked ex 5.1

#intializaiton
entry = None
count = 0
sum = 0
ave = 0
while True:
    entry = input("Enter a number:")
    if entry == "done":
        break
    try:
        number = float(entry)
    except:
        print("Invalid input")
        continue
    count = count+1
    sum = sum + number
    ave = sum/count

print(count, sum, ave)
