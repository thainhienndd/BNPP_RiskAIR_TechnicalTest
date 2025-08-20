# Function to check if a string is balanced ((, {, [, */)
def is_balanced(s: str) -> bool:
    stack = []
    pairs = {')':'(', ']':'[', '}':'{'}
    i = 0
    n = len(s)

    # For each element
    while i < n:
        # Case of a comment: First, we check if a comment has started
        if i+1 < n and s[i] == '/' and s[i+1] == '*':
            # Check if a comment has ended from the start of the comment in the rest of the string
            j = s.find('*/', i+2)
            # Comment has not ended --> return not balanced
            if j == -1:
                return False
            # Restart from end of the comment
            i = j + 2
            continue
        # current caracter
        ch = s[i]
        # check if a symbol has started and append to the list
        if ch in '([{':
            stack.append(ch)
        # If it has ended: check if it has started and check is it is in the right order
        elif ch in ')]}':
            # Case when it is unbalanced (not started or not in right order)
            if not stack or stack[-1] != pairs[ch]:
                return False
            # balanced, so we remove the last element to check for next one
            stack.pop()
        i += 1
    return len(stack) == 0


print(f"Case of a parenthesis balanced: {is_balanced('Hello AIR TECH  (I am Thai-Nhien)')}")
print(f"Case of a square bracket balanced: {is_balanced('Hello AIR TECH  [I am Thai-Nhien]')}")
print(f"Case of a curly bracket balanced: {is_balanced('Hello AIR TECH  {I am Thai-Nhien}')}")
print(f"Case of a comment balanced: {is_balanced('Hello AIR TECH /* I am Thai-Nhien */')}")
print(f"Case of a comment balanced with parenthesis unbalanced inside: {is_balanced('Hello AIR TECH /* (I am Thai-Nhien */')}")
print(f"Case of an unbalanced parenthesis: {is_balanced('Hello AIR TECH (I am Thai-Nhien')}")
print(f"Case of an unbalanced parenthesis because bracket closes parenthesis: {is_balanced('Hello AIR TECH (I am Thai-Nhien}')}")
