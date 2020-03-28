hrs = input("Enter Hours:")
sr = input("Enter Rate:")
pay = 0
try:
    h = float(hrs)
    r = float(sr)
except:
    print("Error, please enter a numeric number")
    quit()
    
print(h, r)
if h<=40:
    pay = h*r
else:
	pay = 40*r + 1.5*r*(h-40)

print(pay)
