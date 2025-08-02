def operator(number, operator, reuslt):
    if operator == "+":
        result += int(number)
    elif operator == "-":
        result -= int(number)
    elif operator == "*":
        result *= int(number)
    else:
        result /= int(number)
    return result


def parser(expression, index):
    current_number = 0
    current_result = 0
    current_operator = "+"

    while index < len(expression):
        char = expression[index]

        if char.isdigit():
            current_number = current_number * 10 + int(char)

        elif char == "(":
            current_number, index = parser(expression, index + 1)

        elif char in "+-*/":
            current_result = operator(
                current_number, current_operator, current_result)
            current_operator = char
            current_number = 0

        elif char == ")":
            current_result = operator(
                current_number, current_operator, current_result)
            return current_result, index + 1

        index += 1

    current_result = operator(current_number, current_operator, current_result)
    return current_result, index


def apply_calc(expression):
    result, _ = parser(expression.replace(" ", ""), 0)
    return result
