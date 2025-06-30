# O(n*2^n) time | O(n*2^n) space
def powerset_iteration(array):
    subsets = [[]]
    for el in array:
        for i in range(len(subsets)):
            current_subset = subsets[i]
            subsets.append(current_subset + [el])
    return subsets

# O(n*2^n) time | O(n*2^n) space
def powerset_recursion(array, index = None):
    if index is None:
        index = len(array) - 1
    elif index < 0:
        return [[]]
    subsets = powerset_recursion(array, index-1)
    el = array[index]
    for i in range(len(subsets)):
        current_subset = subsets[i]
        subsets.append(current_subset + [el])
    return subsets
