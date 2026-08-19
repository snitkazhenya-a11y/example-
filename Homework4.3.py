import random
n = random.randint(1, 10)
my_list = [random.randint(1, 10) for _ in range(n)]
print(my_list)
new_list = [my_list[0], my_list[2], my_list[-2]]
print(new_list)