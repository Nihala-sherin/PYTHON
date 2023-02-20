s = str(input("Enter a line of text: "))
words = s.split()
count = dict()
for x in words:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1
print(count)


