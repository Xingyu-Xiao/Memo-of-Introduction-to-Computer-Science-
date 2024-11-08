def operator(op, x, y):
    if op == '*':
        return x * y
    elif op == '/':
        return x / y
    elif op == '-':
        return x - y
    elif op == '+':
        return x + y


def solution(a):
    stack = []
    tokens = list(a.split())
    tokens.reverse()
    for token in tokens:
        try:
            stack.append(float(token))
        except ValueError:
            x = stack.pop()
            y = stack.pop()
            stack.append(operator(token, x, y))
    return f'{stack[0]:.6f}'


print(solution(input()))
