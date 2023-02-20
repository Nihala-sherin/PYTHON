n = int(input("Enter the no. of numbers:"))
list=[]
print("Enter",n,"integer numbers:")
for i in range(n):
    x = int(input(""))
    if x>100:
        list.append("over")
    else:
        list.append(x)
print(list)