n = int(input("Enter the number of words: "))
list = []
for i in range(n):
    x = (input("Enter the word: "))
    list.append(x)
print(list)
length = len(list[0])
temp = list[0]
for i in list:
    if(len(i) > length):
        length = len(i)
    temp = i
print("The word having longest length is:",temp,",and its length is:",length)
