class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_operator(char):
    return char in {'+', '-', '*', '/'}

def precedence(op):
    if op in {'+', '-'}:
        return 1
    if op in {'*', '/'}:
        return 2
    return 0

def build_expression_tree(expression):
    def parse_expression(tokens):
        stack = []
        output = []
        for token in tokens:
            if token.isdigit():
                output.append(Node(int(token)))
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(Node(stack.pop()))
                stack.pop()  # Remove '('
            elif is_operator(token):
                while stack and stack[-1] != '(' and precedence(stack[-1]) >= precedence(token):
                    output.append(Node(stack.pop()))
                stack.append(token)
        
        while stack:
            output.append(Node(stack.pop()))
        
        return output

    def build_tree(postfix):
        stack = []
        for node in postfix:
            if is_operator(node.value):
                node.right = stack.pop()
                node.left = stack.pop()
            stack.append(node)
        return stack[0]

    tokens = [char for char in expression if char != ' ']
    postfix = parse_expression(tokens)
    return build_tree(postfix)

def evaluate_tree(node):
    if isinstance(node.value, int):
        return node.value
    
    left_value = evaluate_tree(node.left)
    right_value = evaluate_tree(node.right)
    
    if node.value == '+':
        return left_value + right_value
    elif node.value == '-':
        return left_value - right_value
    elif node.value == '*':
        return left_value * right_value
    elif node.value == '/':
        return left_value / right_value

# Ejemplo de uso
expression = "3 + 5 * (2 - 8)"
tree = build_expression_tree(expression)
result = evaluate_tree(tree)
print(f"El resultado de {expression} es: {result}")

# Función para imprimir el árbol (para visualización)
def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print(' ' * 4 * level + str(node.value))
        print_tree(node.left, level + 1)

print("\nEstructura del árbol:")
print_tree(tree)

