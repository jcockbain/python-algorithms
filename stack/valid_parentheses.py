def isValid(s):
    brackets = {
        "}": "{",
        "]": "[",
        ")": "(",
    }
    opening = brackets.values()
    stack = []
    for c in s:
        if c in opening:
            stack.append(c)
        elif c in brackets:
            if len(stack) == 0 or stack[-1] != brackets[c]:
                return False
            stack.pop()
    if len(stack) > 0:
        return False
    return True
