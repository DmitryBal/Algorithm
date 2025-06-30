# O(nlog(n) + mLog(m)) time | O(1) space
def smallestDifference(arr1, arr2):
    arr1.sort()
    arr2.sort()
    index_1 = 0
    index_2 = 0
    smallest = float("inf")
    smallest_pair = []
    while index_1 < len(arr1) and index_2 < len(arr2):
        first_num = arr1[index_1]
        second_num = arr2[index_2]
        if first_num < second_num:
            current = second_num - first_num
            index_1 += 1
        elif second_num < first_num:
            current = first_num - second_num
            index_2 += 1
        else:
            return [first_num, second_num]
        if smallest > current:
            smallest = current
            smallest_pair = [first_num, second_num]
    return smallest_pair

