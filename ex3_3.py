# prompt input
score = input("Enter Score:")
#convert to float
try:
    s = float(score)
except:
    print("Error, please enter a numeric number")
    quit()
#conditional grading
if s>1.0:
    g = "Error, out of range"
elif s>=0.9:
    g = "A"
elif s>=0.8:
    g = "B"
elif s>=0.7:
    g = "C"
elif s>=0.6:
    g = "D"
elif g<0.6:
    g = "F"
elif g<0:
    g = "Error, out of range"
#output
print(g)
