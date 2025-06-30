
# O(n^2) time / O(n) space
def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    N = len(array)
    for i in range(N-2):
        left_index = i + 1
        right_index = N-1
        while left_index < right_index:
            currentSum = array[i] + array[left_index] + array[right_index]
            if currentSum == targetSum:
                triplets.append([array[i], array[left_index], array[right_index]])
                left_index += 1
                right_index -= 1
            elif currentSum < targetSum:
                left_index +=1
            else:
                right_index -= 1
    return triplets

