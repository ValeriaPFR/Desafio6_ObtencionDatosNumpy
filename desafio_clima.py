"""
Desafío: Obtención de datos y fundamentos de NumPy
Curso: Fundamentos de Ciencias de Datos
Estudiante: Valeria Fariña Rebolledo
OTEC: Nueva CIASPO
"""

import numpy as np

# =====================================================================
# 1. CARGA DE DATOS CLIMÁTICOS
# =====================================================================
def cargar_temperaturas(nombre_archivo):
    """
    Lee el archivo CSV que contiene las temperaturas en Fahrenheit
    y las convierte en una matriz de NumPy para poder hacer cálculos rápidos.
    """
    try:
        # Carga los números del archivo ignorando las filas de texto de los títulos
        datos = np.genfromtxt(nombre_archivo, delimiter=',', skip_header=1)
        print(f"✅ Archivo '{nombre_archivo}' cargado correctamente.")
        return datos
    except Exception as e:
        print(f"❌ Error al cargar el archivo: {e}")
        return None

# =====================================================================
# 2. CONVERSION DE UNIDADES (FAHRENHEIT A CELSIUS)
# =====================================================================
def convertir_fahrenheit_a_celsius(matriz_f):
    """
    Toma la matriz con temperaturas en Fahrenheit y aplica la fórmula matemática
    para transformar todos los números juntos a grados Celsius.
    """
    return (matriz_f - 32) * 5 / 9

# =====================================================================
# 3. CÁLCULOS ESTADÍSTICOS CON NUMPY
# =====================================================================
def analizar_datos_climaticos(matriz_celsius):
    """
    Saca cuentas automáticas sobre las temperaturas en Celsius usando
    las herramientas matemáticas rápidas de NumPy.
    """
    print("\n========================================")
    print("       MÉTRICAS DEL CLIMA (CELSIUS)     ")
    print("========================================")
    
    # Saca el promedio general de toda la matriz
    promedio = np.mean(matriz_celsius)
    
    # Encuentra la temperatura más alta registrada
    maxima = np.max(matriz_celsius)
    
    # Encuentra la temperatura más baja registrada
    minima = np.min(matriz_celsius)
    
    # Cuenta cuántos días registraron temperaturas consideradas "calurosas" (más de 30°C)
    dias_calurosos = np.sum(matriz_celsius > 30)

    # Muestra los resultados finales en la terminal redondeados a un decimal
    print(f"Temperatura promedio general : {promedio:.1f}°C")
    print(f"Temperatura más alta del año : {maxima:.1f}°C")
    print(f"Temperatura más baja del año : {minima:.1f}°C")
    print(f"Cantidad de días calurosos (>30°C): {dias_calurosos} días")
    print("========================================")

# =====================================================================
# BLOQUE DE CONTROL PRINCIPAL
# =====================================================================
def main():
    # Nombre del archivo que contiene las temperaturas en la carpeta de trabajo
    archivo_datos = "temperaturas_fahrenheit.csv"
    
    # Paso 1: Intentar leer el archivo externo
    temperaturas_f = cargar_temperaturas(archivo_datos)
    
    # Si el archivo se leyó bien, hacemos los cálculos condicionales
    if temperaturas_f is not None:
        # Paso 2: Convertir los datos a nuestra escala local (Celsius)
        temperaturas_c = convertir_fahrenheit_a_celsius(temperaturas_f)
        
        # Paso 3: Analizar los resultados y mostrarlos en la pantalla
        analizar_datos_climaticos(temperaturas_c)

if __name__ == "__main__":
    main()