# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
all = fh.read()
up = all.upper()
print(up)
