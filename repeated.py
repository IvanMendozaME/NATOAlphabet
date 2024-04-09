list1 = ['3', '6', '5', '8', '33', '12', '7', '4', '72', '2', '42', '13']
list2 = ['3', '6', '13', '5', '7', '89', '12', '3', '33', '34', '1', '344', '42']
result = []
for i in list2:
    if i in list1:
        print(i)
        result.append(i)

print(result)