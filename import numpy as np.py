import numpy as np

def calculate(lista):
    if len(lista) != 9:
        raise ValueError("La lista debe contener nueve números")
    
    # Convertir la lista en matriz 3x3
    matriz = np.array(lista).reshape(3, 3)
    
    # Calcular estadísticas para cada eje y la matriz aplanada
    resultados = {
        'mean': [
            np.mean(matriz, axis=0).tolist(),  # Eje 0 (columnas)
            np.mean(matriz, axis=1).tolist(),  # Eje 1 (filas)
            np.mean(matriz).tolist()           # Aplanada
        ],
        'variance': [
            np.var(matriz, axis=0).tolist(),
            np.var(matriz, axis=1).tolist(),
            np.var(matriz).tolist()
        ],
        'standard deviation': [
            np.std(matriz, axis=0).tolist(),
            np.std(matriz, axis=1).tolist(),
            np.std(matriz).tolist()
        ],
        'max': [
            np.max(matriz, axis=0).tolist(),
            np.max(matriz, axis=1).tolist(),
            np.max(matriz).tolist()
        ],
        'min': [
            np.min(matriz, axis=0).tolist(),
            np.min(matriz, axis=1).tolist(),
            np.min(matriz).tolist()
        ],
        'sum': [
            np.sum(matriz, axis=0).tolist(),
            np.sum(matriz, axis=1).tolist(),
            np.sum(matriz).tolist()
        ]
    }
    
    return resultados