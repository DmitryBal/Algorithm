# O(n^3) time | O(n^2) space
def fourNumberSum(array, target_sum):
    all_pair_sums = {}
    quadruplets = []
    for i in range(1, len(array)-1):
        for j in range(i+1, len(array)):
            current_sum = array[i] + array[j]
            difference = target_sum - current_sum
            if difference in all_pair_sums:
                for pair in all_pair_sums[difference]:
                    quadruplets.append(pair + [array[i], array[j]])
        for k in range(0, i):
            current_sum = array[i] + array[k]
            if current_sum not in all_pair_sums:
                all_pair_sums[current_sum] = [[array[k], array[i]]]
            else:
                all_pair_sums[current_sum].append([array[k], array[i]])
    return quadruplets
