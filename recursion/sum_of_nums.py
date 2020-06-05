
x = [1, 2, 3, [4, 5, 6], 4, 5, [7, 8, [9, 10]]]

# the input being sent to the function has lists inside lists

def sum_of_all_nums_recursive(nums_and_num_lists: list) -> int:
                             # param is a list - which returns an int
                             # specifying this is optional
    total = 0
    for element in nums_and_num_lists:
        if isinstance(element, int):
            total += element
        elif isinstance(element, list):
            total += sum_of_all_nums_recursive(element)
    return total

print(sum_of_all_nums_recursive(x))
