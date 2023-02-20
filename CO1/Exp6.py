list1 = [1,2,3,4,5]
list2 = [2,4,6,8,10]
print("list 1=",list1)
print("list 2=",list2)
if (len(list1) == len(list2)):
    print("Both lists have the same length")
else:
    print("Lists have different length")
s1 = 0
s2 = 0
for i in range(len(list1)):
    s1=s1+list1[i]
for j in range(len(list2)):
    s2=s2+list2[j]
print("The sum of list 1 is:",s1)
print("The sum of list 2 is:",s2)
if s1==s2:
    print("Both lists have the same sum")
else:
    print("Both lists have different sums")
print("The common numbers in both lists are: ")
for i in list1:
    for j in list2:
        if i==j:
            print(i)