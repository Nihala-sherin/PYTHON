col1 = ['red', 'blue', 'yellow']
col2 = ['green', 'blue']
print(col1)
print(col2)
print("The colours present in first list and not in the second list are:")
for i in range(len(col1)):
    if col1[i] not in col2:
        print(col1[i])
