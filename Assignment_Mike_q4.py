# Question number 4 - Find which list has more bigger numbers

list1 = [-1, 200, 9, 100, 1000]
list2 = [-1, 300, 8, 101]

count_list1 = 0
count_list2 = 0

min_range = min(len(list1), len(list2))

# Iterate over the minimum length of the lists
for i in range(min_range):

    # if list1's number is bigger than list2
    if list1[i] > list2[i]:
        count_list1 += 1

    # if the numbers are equal, do nothing
    elif list1[i] == list2[i]:
        continue

    # if list2's number is bigger than list1
    else:
        count_list2 += 1

if count_list1 > count_list2:
    print("list1 is bigger")

elif count_list1 == count_list2:
    print("list1 equals list2")

else:
    print("list2 is bigger")