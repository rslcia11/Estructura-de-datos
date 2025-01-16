import heapq
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Generar datos sintéticos para entrenamiento del modelo
np.random.seed(42)
num_samples = 1000
task_types = np.random.randint(1, 5, size=num_samples)  # Tipos de tareas (1 a 4)
complexities = np.random.uniform(0.5, 5.0, size=num_samples)  # Complejidad (0.5 a 5.0)
wait_times = (complexities * task_types + np.random.normal(scale=2, size=num_samples))  # Tiempo de espera simulado

# Preparar datos para el modelo
X = np.stack([task_types, complexities], axis=1)
y = wait_times

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_val, y_train, y_val = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Definir el modelo de predicción
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(32, activation='relu'),
    Dense(1, activation='linear')  # Salida de regresión
])

model.compile(optimizer='adam', loss='mae', metrics=['mae'])
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_val, y_val), verbose=1)

# Visualizar el entrenamiento
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Entrenamiento del Modelo')
plt.xlabel('Épocas')
plt.ylabel('MAE')
plt.legend()
plt.show()

# Implementar la cola de prioridad
class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def push(self, task_id, priority):
        heapq.heappush(self.heap, (priority, task_id))
    
    def pop(self):
        return heapq.heappop(self.heap) if self.heap else None
    
    def is_empty(self):
        return len(self.heap) == 0

# Crear simulación de tareas
tasks = [
    {"id": i, "type": np.random.randint(1, 5), "complexity": np.random.uniform(0.5, 5.0)}
    for i in range(20)
]

queue = PriorityQueue()

# Predecir prioridades con el modelo
for task in tasks:
    task_features = scaler.transform([[task['type'], task['complexity']]])
    predicted_wait_time = model.predict(task_features)[0][0]
    queue.push(task['id'], predicted_wait_time)

# Procesar las tareas en orden de prioridad
print("Procesando tareas en orden de prioridad:")
while not queue.is_empty():
    priority, task_id = queue.pop()
    print(f"Tarea {task_id} con prioridad estimada: {priority:.2f}")
