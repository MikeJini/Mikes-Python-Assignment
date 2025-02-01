list1 = [-1, 200, 9, 100, 1000]
list2 = [-1, 300, 8, 101]

count_list1 = 0
count_list2 = 0

min_range = min(len(list1), len(list2))

for i in range(min_range):

    if list1[i] > list2[i]:
        count_list1 += 1
    elif list1[i] == list2[i]:
        continue
    else:
        count_list2 += 1

if count_list1 > count_list2:
    print("list1 is bigger")
elif count_list1 == count_list2:
    print("list1 equals list2")
else:
    print("list2 is bigger")