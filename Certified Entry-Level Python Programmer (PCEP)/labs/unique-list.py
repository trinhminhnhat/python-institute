#3.6.1.9 LAB: Operating with lists - basics
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []

for num in my_list:
    if num not in new_list:
        new_list.append(num)

print("The list with unique elements only:")
print(new_list)
