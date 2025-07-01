# O(n) time | O(n) space
def largestRange(array):
    best_range = []
    longest_len = 0
    visited = {}
    for el in array:
        visited[el] = True
    for el in array:
        if not visited[el]:
            continue
        visited[el] = False
        current_len = 1 
        left = el - 1
        right = el + 1
        while left in visited:
            visited[left] = False
            current_len += 1
            left -= 1
        while right in visited:
            visited[right] = False
            current_len += 1
            right += 1
        if current_len > longest_len:
            longest_len = current_len
            best_range = [left + 1, right - 1]
    return  best_range
