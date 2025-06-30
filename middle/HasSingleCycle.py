# O(n) time | O(1) space
def hasSingleCycle(array):
    num_elements_visited = 0
    current_index = 0
    while num_elements_visited < len(array):
        if num_elements_visited > 0 and current_index == 0:
            return False
        num_elements_visited += 1
        current_index = getNextIdx(current_index, array)
    return current_index == 0


def getNextIdx(current_index, array):
    jump = array[current_index]
    next_index = (current_index + jump) % len(array)
    return next_index if next_index >= 0 else next_index + len(array)
