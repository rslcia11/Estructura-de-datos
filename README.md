# Estructura-de-datos
Actividad2.3 
**Evaluador de Expresiones Matemáticas**  

**Paso 1: Selección del TDA y Aplicación**  
**TDA seleccionado**: Pila  
**Aplicación**: Evaluación de expresiones matemáticas, capaz de manejar operaciones fundamentales como suma, resta, multiplicación y división.  

**Paso 2: Investigación y Diseño**  
**Diseño de la Pila**: La pila es una estructura de datos basada en el principio LIFO (Last In, First Out), donde el último elemento agregado es el primero en ser retirado. Sus operaciones principales son:  

**Descripción del Proyecto**  
Este proyecto consiste en un programa en Python que implementa un evaluador de expresiones matemáticas utilizando la estructura de datos de una pila. La pila permite gestionar la precedencia de operadores y evaluar expresiones aritméticas, incluso aquellas que incluyen paréntesis. Durante la evaluación, la pila almacena tanto operadores como operandos.  

**Funcionalidades**:  
- Evaluación de expresiones matemáticas con operaciones básicas (+, -, *, /).  
- Manejo adecuado de paréntesis para establecer el orden de las operaciones.  
- Capacidad de procesar expresiones sin espacios entre operandos y operadores.  

**TDA Implementado: Pila**  
La pila es una estructura LIFO que se utiliza en este proyecto para:  
- Almacenar operadores mientras se evalúan operandos.  
- Gestionar los paréntesis que delimitan subexpresiones.  

**Operaciones Implementadas para la Pila**:  
- `push(x)`: Agrega un elemento `x` a la pila.  
- `pop()`: Retira y devuelve el elemento en la parte superior de la pila.  
- `peek()`: Devuelve el elemento superior sin removerlo.  
- `is_empty()`: Comprueba si la pila está vacía.  

**Evaluador de Expresiones**  
El evaluador analiza la expresión de izquierda a derecha. Utiliza la pila para aplicar correctamente la precedencia de los operadores y resuelve las subexpresiones respetando los paréntesis.