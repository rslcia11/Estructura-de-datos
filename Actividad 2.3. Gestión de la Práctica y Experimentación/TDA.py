class Pila:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
def prioridad(operador):
    if operador == '+' or operador == '-':
        return 1
    if operador == '*' or operador == '/':
        return 2
    return 0

def evaluar_expresion(expresion):
    pila_operadores = Pila()
    pila_operandos = Pila()
    
    i = 0
    while i < len(expresion):
        char = expresion[i]

        # Filtrar espacios en blanco
        if char == ' ':
            i += 1
            continue
        
        print(f"Procesando: {char}")
        print(f"Pila Operadores: {pila_operadores.items}")
        print(f"Pila Operandos: {pila_operandos.items}")

        if char.isdigit():  # Si es un operando
            num = 0
            while i < len(expresion) and expresion[i].isdigit():
                num = num * 10 + int(expresion[i])
                i += 1
            pila_operandos.push(num)
        elif char == '(':  # Paréntesis de apertura
            pila_operadores.push(char)
            i += 1
        elif char == ')':  # Paréntesis de cierre
            while pila_operadores.peek() != '(':
                operador = pila_operadores.pop()
                operand2 = pila_operandos.pop()
                operand1 = pila_operandos.pop()

                # Asegurarse de que operand1 y operand2 no sean None
                if operand1 is None or operand2 is None:
                    raise ValueError("Error: Operando inválido")

                if operador == '+':
                    pila_operandos.push(operand1 + operand2)
                elif operador == '-':
                    pila_operandos.push(operand1 - operand2)
                elif operador == '*':
                    pila_operandos.push(operand1 * operand2)
                elif operador == '/':
                    pila_operandos.push(operand1 / operand2)
            pila_operadores.pop()  # Elimina '('
            i += 1
        else:  # Es un operador
            while (not pila_operadores.is_empty() and 
                   prioridad(pila_operadores.peek()) >= prioridad(char)):
                operador = pila_operadores.pop()
                operand2 = pila_operandos.pop()
                operand1 = pila_operandos.pop()

                # Asegurarse de que operand1 y operand2 no sean None
                if operand1 is None or operand2 is None:
                    raise ValueError("Error: Operando inválido")

                if operador == '+':
                    pila_operandos.push(operand1 + operand2)
                elif operador == '-':
                    pila_operandos.push(operand1 - operand2)
                elif operador == '*':
                    pila_operandos.push(operand1 * operand2)
                elif operador == '/':
                    pila_operandos.push(operand1 / operand2)
            pila_operadores.push(char)
            i += 1

    while not pila_operadores.is_empty():
        operador = pila_operadores.pop()
        operand2 = pila_operandos.pop()
        operand1 = pila_operandos.pop()

        # Asegurarse de que operand1 y operand2 no sean None
        if operand1 is None or operand2 is None:
            raise ValueError("Error: Operando inválido")

        if operador == '+':
            pila_operandos.push(operand1 + operand2)
        elif operador == '-':
            pila_operandos.push(operand1 - operand2)
        elif operador == '*':
            pila_operandos.push(operand1 * operand2)
        elif operador == '/':
            pila_operandos.push(operand1 / operand2)

    return pila_operandos.pop()

expresion = "3 + 2 * (7 - 5)"
resultado = evaluar_expresion(expresion)
print(f"El resultado es: {resultado}")