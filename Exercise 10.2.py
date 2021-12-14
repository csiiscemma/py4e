name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
li = list()
for line in handle:
    if not line.startswith('From '): continue
    hours = line.split()[5].split(":")[0]
    li.append(hours)
di = {i:li.count(i) for i in li}
for key, value in sorted(di.items()):
    print(key, value)
