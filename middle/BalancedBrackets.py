# O(n) time | O(n) space
def balancedBrackets(string):
    stack = []
    brackets_opened = '([{'
    brackets_closed = ')]}'
    brackets_hash = {')': '(', ']': '[', '}': '{'}
    for el in string:
        if el in brackets_opened:
            stack.append(el)
        elif el in brackets_closed:
            if len(stack) == 0 :
                return False
            if stack[-1] == brackets_hash[el]:
                stack.pop()
            else:
                return False
    return len(stack) == 0
