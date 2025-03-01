import streamlit as st
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

def find_expression(numbers, target):
    for subset_size in range(1, len(numbers) + 1):
        for subset in itertools.combinations(numbers, subset_size):
            for perm in itertools.permutations(subset):
                exprs = generate_expressions(list(perm))
                for expr in exprs:
                    if expr[1] == target:
                        return expr[0]
    return None

def main():
    st.title("Expression Generator")
    st.write("Enter numbers and a target to find a mathematical expression that equals the target.")

    numbers_str = st.text_input("Enter the numbers (comma-separated):", "1,2,3")
    target = st.number_input("Enter the target answer:", value=6, step=1, format="%d")

    if st.button("Find Expression"):
        try:
            numbers_list = [num.strip() for num in numbers_str.split(',')]
            numbers = [int(num) for num in numbers_list if num]
            expression = find_expression(numbers, target)
            if expression:
                st.write(expression + " = " + str(target))
            else:
                st.write("No solution found.")
        except ValueError:
            st.write("Invalid input. Please enter valid numbers and target.")

if __name__ == "__main__":
    main()