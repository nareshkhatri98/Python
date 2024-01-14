def sum_list(lst):
    total_sum =0
    for i in lst:
        total_sum = total_sum + i

    return total_sum

result = sum_list([3,4,5,67,7])
print("the sum of the list is :", result)