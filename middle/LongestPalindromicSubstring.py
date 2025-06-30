def getLongestPolindrome(string, left_index, right_index):
    while left_index >= 0 and right_index < len(string):
        if string[left_index] != string[right_index]:
            break
        left_index -= 1
        right_index +=1
    return [left_index + 1, right_index]

# O(n^2) time | O(1) space
def longestPalindromicSubstring(string):
    current_longest = [0, 1]
    for i in range(1, len(string)):
        longest = max( getLongestPolindrome(string, i - 1, i + 1), getLongestPolindrome(string, i - 1, i), key = lambda x: x[1] - x[0])
        current_longest = max(longest, current_longest, key = lambda x: x[1] - x[0])
    return string[current_longest[0]:current_longest[1]]
