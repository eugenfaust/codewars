def move_zeros(lst: list):
    zeros_count = 0
    clean_array = []
    for i in range(len(lst)):
        if lst[i] == 0:
            zeros_count += 1
        else:
            clean_array.append(lst[i])
    clean_array.extend([0 for _ in range(zeros_count)])
    return clean_array


print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
print(
    move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) == [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0,
                                                                                 0, 0, 0, 0, 0, 0, 0])
print(move_zeros([0, 0]) == [0, 0])
print(move_zeros([0]) == [0])
print(move_zeros([]) == [])
