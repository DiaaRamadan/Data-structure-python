from stack.stack_by_linkedlist import Stack


def evaluate_post_fix(input_list):
    """
    Evaluate the postfix expression to find the answer
    Args:
       input_list(list): List containing the postfix expression
    Returns:
       int: Postfix expression solution
    """
    stack = Stack()
    for item in input_list:
        if item == '*' or item == '/' or item == '+' or item == '-':
            output = int(sign_handler(item, stack.pop(), stack.pop()))
            stack.push(output)
        else:
            stack.push(item)

    return stack.pop()


def sign_handler(sign, second, first):
    return eval(f"{first} {sign} {second}")


print(evaluate_post_fix(["4", "13", "5", "/", "+"]))

