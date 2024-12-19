class Expresion:
    def __init__(self, expresion):
        self.expresion = expresion

    def balancear_parentesis(self):
        pila = []
        for char in self.expresion:
            if char in "({[":
                pila.append(char)
            elif char in ")}]":
                if not pila:
                    return False
                top = pila.pop()
                if char == ")" and top != "(":
                    return False
                if char == "]" and top != "[":
                    return False
                if char == "}" and top != "{":
                    return False
        return len(pila) == 0

    def validar_operadores_operandos(self):
        operadores = "+-*/^"
        prev_char = ""
        for char in self.expresion:
            if char in operadores:
                if prev_char in operadores or prev_char == "" or prev_char in "({[":  # operador seguido de otro operador, inicio o apertura de paréntesis
                    return False
            prev_char = char
        return prev_char not in operadores  # La expresión no debe terminar con un operador

    def construir_arbol(self):
        # Un árbol simple que solo divida la expresión en nodos
        # Para un árbol más completo, se necesitaría un algoritmo como el de Shunting Yard
        return self.expresion

    def validar(self):
        print("Validando expresión...")
        if not self.balancear_parentesis():
            return "Error: Paréntesis desbalanceados"
        if not self.validar_operadores_operandos():
            return "Error: Disposición incorrecta de operadores y operandos"
        print("Expresión válida")
        return self.construir_arbol()

# Casos de prueba
def pruebas():
    expresiones = [
        "((a + b) * c)",  # válida
        "5 * (3 + 2)",  # válida
        "5 * (3 + 2",  # inválida (falta paréntesis de cierre)
        "a + + b",  # inválida (operador repetido)
        "(a + b) * c)",  # inválida (paréntesis desbalanceados)
        "(a + b) * (c + d)"  # válida
    ]

    for expresion in expresiones:
        print(f"Expresion: {expresion}")
        resultado = Expresion(expresion).validar()
        print(f"Resultado: {resultado}\n")

# Ejecutar pruebas
pruebas()
