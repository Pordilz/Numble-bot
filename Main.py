import itertools


def generate_expressions(numbers):
    if len(numbers) == 1:
        return [(str(numbers[0]), numbers[0])]
    expressions = []
    for i in range(1, len(numbers)):
        left_numbers = numbers[:i]
        right_numbers = numbers[i:]
        left_exprs = generate_expressions(left_numbers)
        right_exprs = generate_expressions(right_numbers)
        for left_expr in left_exprs:
            for right_expr in right_exprs:
                for op in ['+', '-', '*', '/']:
                    if op == '/' and right_expr[1] != 0:
                        division_result = left_expr[1] / right_expr[1]
                        if division_result.is_integer():
                            value = int(division_result)
                            expr_str = "(" + left_expr[0] + " " + op + " " + right_expr[0] + ")"
                            expressions.append((expr_str, value))
                    elif op in ['+', '-', '*']:
                        if op == '+':
                            value = left_expr[1] + right_expr[1]
                        elif op == '-':
                            value = left_expr[1] - right_expr[1]
                        elif op == '*':
                            value = left_expr[1] * right_expr[1]
                        expr_str = "(" + left_expr[0] + " " + op + " " + right_expr[0] + ")"
                        expressions.append((expr_str, value))
    return expressions


def main():
    numbers_str = input("Enter the numbers (comma-separated): ")
    target = int(input("Enter the target answer: "))
    numbers = [int(num.strip()) for num in numbers_str.split(',')]

    for subset_size in range(1, len(numbers) + 1):
        for subset in itertools.combinations(numbers, subset_size):
            for perm in itertools.permutations(subset):
                exprs = generate_expressions(list(perm))
                for expr in exprs:
                    if expr[1] == target:
                        print(expr[0] + " = " + str(target))
                        return
    print("No solution found.")


if __name__ == "__main__":
    main()