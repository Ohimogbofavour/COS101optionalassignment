num_list = [5,6,2,8,3,8,9,2,8,4]

list2 = num_list.copy()

list3 = []

for _ in num_list:
    list3.append(list2[-1])
    list2.pop(-1)

num_list = list3
print(num_list)