n = int(input("Enter the no.of first names:"))
print("Enter",n,"first names:")
list = []
for i in range(n):
    x = input()
    list.append(x)
count = 0
for i in list:
    for j in i:
        if 'a' in j:
            count = count+1
print("The occurence of 'a' in the names :",count)