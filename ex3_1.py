hrs = input("Enter Hours:")
h = float(hrs)
pay = 0
rate = 10.5
if h<=40:
    pay = h*rate
else:
	pay = 40*rate + 1.5*rate*(h-40)

print(pay)
