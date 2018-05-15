def is_matched(expression):
    pairs = {'{': '}', '[': ']', '(': ')'}
    sk = []
    if (len(expression) % 2 != 0):
        return False
    for c in expression:
        if c in pairs:
            sk.append(pairs[c])
        elif not sk or c != sk.pop():
            return False
    return not sk


t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression):
        print("YES")
    else:
        print("NO")
