#input
# get the name of the file and open it
name = input('Enter file:')
handle = open(name, 'r')
counts = dict()

#processing
#count word frequency
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# find the most common word
bigcount = None
bigword = None
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

#output
print(bigword, bigcount)

# Code: http://www.py4e.com/code3/words.py
