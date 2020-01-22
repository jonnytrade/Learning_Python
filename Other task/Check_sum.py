def check_sum(num_list):
    lenght = len(num_list)
    k = 0
    for i in range (len(num_list)):
        while k != lenght:
            if num_list[i] + num_list[k] == 0:
                print("Done",num_list)
                return True
            k += 1
        k = 0
    print("Fail",num_list)


num_list = [10, 7, 3, 5, 8, -7, 12]
check_sum(num_list)
