my_list = [2]
for k in range(3, 200, 2):
    i = 0
    while k > my_list[i]:
        if k % my_list[i] == 0:
            break
        if my_list[i] * 2 > k:
           my_list.append(k)
           break
        i +=1
summa = sum(my_list)
print(my_list)
print(summa)
