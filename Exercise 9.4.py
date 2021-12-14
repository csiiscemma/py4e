name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts=dict()
for line in handle:
    if not line.startswith('From '): continue
    words = line.split()
    words = words[1]
    counts[words] = counts.get(words,0) + 1
print(words, counts[words])
