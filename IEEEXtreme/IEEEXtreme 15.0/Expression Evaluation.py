def shunting_yard(expression):
    """Shunting-yard algorithm to parse expressions"""

    precedence = {
        "-": 1,
        "+": 1,
        "*": 2,
        "(": 3,
        ")": 3
    }

    output = []
    operators = []
    is_number = False

    for i in range(len(expression)):
        token = expression[i]

        if token.isdigit():
            if is_number:
                output[-1] += token

            else:
                output.append(token)

            is_number = True

        else:
            is_number = False

        if token in ("*", "+", "-"):
            while len(operators) != 0 and operators[-1] != "(" and precedence[operators[-1]] >= precedence[token]:
                output.append(operators.pop())

            operators.append(token)

        elif token == "(":
            if len(operators) == 0 and len(output) != 0:
                return "invalid"

            operators.append(token)

        elif token == ")":
            if len(output) == 0 or (i + 1 < len(expression) and expression[i + 1].isdigit()):
                return "invalid"

            if len(operators) != 0:
                try:
                    while operators[-1] != "(":
                        output.append(operators.pop())

                except Exception:
                    return "invalid"

                if operators[-1] != "(":
                    return "invalid"

            operators.pop()

    for operator in operators[::-1]:
        if operator == "(":
            return "invalid"

        output.append(operator)

    # Parse and calculate RPN

    stack = []

    for token in output:
        try:
            if token == "*":
                stack.append(stack.pop() * stack.pop())

            elif token == "+":
                stack.append(stack.pop() + stack.pop())

            elif token == "-":
                stack.append(-(stack.pop() - stack.pop()))

            else:
                stack.append(int(token))

        except Exception:
            return "invalid"

    if len(stack) == 0:
        return "invalid"

    return stack[0] % 1000000007


T = int(input())  # Number of test cases

for t in range(T):
    expression = input()

    print(shunting_yard(expression))
