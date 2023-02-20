n = int(input("Enter the no. of numbers: "))
list = []
print("Enter",n,"numbers:")
for i in range(n):
    a = int(input(""))
    list.append(a)
print(list,"\nThe list of squares of the above numbers: ")
list1 = [x**2 for x in list]
print(list1)