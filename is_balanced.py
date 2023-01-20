""" Check the given str bracket balanced or not """


def is_balanced(s: str) -> bool:
    stack = []
    for char in s:
        if char in '{[(':
            stack.append(char)
        elif char in '}])':
            if not stack:
                return False
            elif char == ')' and stack[-1] != '(':
                return False
            elif char == '[' and stack[-1] != ']':
                return False
            elif char == '{' and stack[-1] != '}':
                return False
            stack.pop()

    return not stack


print(is_balanced("{[()]}"))  # True
print(is_balanced("{[(])}"))  # False
print(is_balanced("{{[[(())]]}}"))  # True

