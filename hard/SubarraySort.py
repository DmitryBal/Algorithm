def isOutOfOrder(i, num, array):
    if i == 0:
        return num > array[i + 1]
    if i == len(array) - 1:
        return num < array[i - 1]
    return num > array[i + 1] or num < array[i - 1]

# O(n) time | O(1) spaceЙ
def subarraySort(array):
    min_out_of_order = float("inf")
    max_out_of_order = float("-inf")
    for i in range(len(array)):
        num = array[i]
        if isOutOfOrder(i, num, array):
            min_out_of_order = min(min_out_of_order, num)
            max_out_of_order = max(max_out_of_order, num)
    if min_out_of_order == float("inf"):
        return [-1, -1]
    subarray_left_index = 0
    while min_out_of_order >= array[subarray_left_index]:
        subarray_left_index += 1
    subarray_right_index = len(array) - 1
    while max_out_of_order <= array[subarray_right_index]:
        subarray_right_index -= 1
    return [subarray_left_index, subarray_right_index]

print(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))
