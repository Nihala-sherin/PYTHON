start = int(input("Enter the current year: "))
end = int(input("Enter the end year: "))
print("The leap years between the two years entered are:")
for i in range(start,end+1):
    if (i%4==0 and i%100!=0 or i%400==0):
        print(i)


