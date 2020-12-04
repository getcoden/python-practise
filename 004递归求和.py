def sum_numbers(num):
    if num == 1:
        return 1
    return num+sum_numbers(num-1)
re = sum_numbers(3)
print(re)