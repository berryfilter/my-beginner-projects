lst = [1, 0, 1, 2, 0, 1, 3]
def move_zeros(lst):
    number_count = [x for x in lst if x != 0]
    zero_count = [0] * (len(lst) - len(number_count))
    return number_count + zero_count

print(move_zeros(lst))

