my_list = [5, 8, 4, 7]
if len(my_list) > 1:
    new_list = [my_list[-1]] + my_list[:-1]
    print(my_list)
    print(new_list)