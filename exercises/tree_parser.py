def parser(expression):
    expression = expression.replace(" ", "")
    for n in range(len(expression)):
        if expression[n] in "-+*/":
            if expression[n:n+2] == "**":
                pass
            else:
                n += 1
                if expression[n] in "+*/":
                    raise ValueError("Malformed input: consecutive operators")
    index = 0

    def parser_factor():
        nonlocal index
        if expression[index] == "-":
            index += 1
            return -parser_factor()
        elif expression[index] == "(":
            index += 1
            value = parser_add_sub()
            index += 1
            return value
        else:
            start = index
            while index < len(expression) and expression[index] in "0123456789.":
                index += 1
            return float(expression[start:index])

    def parser_exponent():
        nonlocal index
        result = parser_factor()
        while index < len(expression) and expression[index] == "*" and expression[index + 1] == "*":
            index += 2
            rhs = parser_factor()
            result = result ** rhs
        return result

    def parser_mul_div():
        nonlocal index
        result = parser_exponent()
        while index < len(expression) and expression[index] in "*/":
            op = expression[index]
            index += 1
            rhs = parser_factor()
            result = result * rhs if op == "*" else result / rhs
        return result

    def parser_add_sub():
        nonlocal index
        result = parser_mul_div()
        while index < len(expression) and expression[index] in "+-":
            op = expression[index]
            index += 1
            rhs = parser_mul_div()
            result = result + rhs if op == "+" else result - rhs
        return result

    return parser_add_sub()


print(parser("2**3 * (3+1)"))
