list_of_strings = input().split(",")

result = [i for i in list_of_strings if int(i)%2 == 0]
print(result)