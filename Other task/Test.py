my_list = [34, 82.6, "Darth Vader", 17, "Hannibal"]
my_list2 = []
my_list2.append(my_list[0])
my_list2.append(my_list[-1])
my_list2.append(len(my_list))
my_tuple = tuple(my_list2)
# print(my_tuple)


def count_low_high(num_list):
    high = 0
    low = 0
    if len(num_list) == 0:
        print("FALSE. List is empty.")
        return None
    for n in num_list:
        if n > 50 or n % 3 == 0:
            high += 1
        else:
            low += 1
    new_list = []
    new_list.append(low)
    new_list.append(high)
    print(new_list)
    return new_list


num_list = []
count_low_high(num_list)
