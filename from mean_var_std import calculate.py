from mean_var_std import calculate

# Prueba con el ejemplo dado
try:
    resultado = calculate([0,1,2,3,4,5,6,7,8])
    print("Resultado:")
    for key, value in resultado.items():
        print(f"{key}: {value}")
        
except ValueError as e:
    print(f"Error: {e}")

# Prueba con lista incorrecta
print("\nPrueba con lista de 8 elementos:")
try:
    calculate([0,1,2,3,4,5,6,7])
except ValueError as e:
    print(f"Error esperado: {e}")