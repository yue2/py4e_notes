text = "X-DSPAM-Confidence:    0.8475"
pos = text.find("0")
length = len(text)
digit = float(text[pos:length])
print(digit)
