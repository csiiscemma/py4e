text = "X-DSPAM-Confidence:    0.8475"
x= text.find(":")
y= text[x+1:]
value=float(y)
print(value)
