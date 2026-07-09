# Desafío: Obtención de Datos y Fundamentos de NumPy

## 📋 Descripción del Proyecto

El sistema está diseñado para interactuar con una base de datos meteorológicos que registra variables térmicas y de humedad. La problemática principal abordada radica en la optimización del rendimiento computacional: en lugar de implementar ciclos iterativos tradicionales (`for` o `while`) que recorren y evalúan los registros uno a uno fila por fila degradando la memoria al escalar el volumen de datos, se utilizó la librería **NumPy**. Esto permite vectorizar las operaciones matemáticas para procesar y transformar toda la estructura de forma simultánea en milisegundos.

El flujo analítico está modularizado en funciones independientes y estructurado en tres fases consecutivas:

1. #*Ingesta y Limpieza de Datos:** Extracción automatizada de los registros desde el archivo fuente `datos_climaticos.csv`.
2. El script discrimina y descarta las filas de encabezado de texto para consolidar una matriz numérica limpia denominada `datos_numericos` con las dimensiones de análisis requeridas.
3. **Transformación y Unificación de Escalas:** Conversión en bloque de los vectores de temperatura desde la escala Celsius a la escala Fahrenheit utilizando operaciones matriciales directas.
4. **Análisis Estadístico y Filtrado:** Obtención de métricas descriptivas fundamentales (promedios generales, máximas y mínimas absolutas) y aplicación de máscaras booleanas para identificar de forma condicional la cantidad exacta de jornadas que superaron el umbral crítico de calor

---

## 🛠️ Tecnologías y Requisitos

* **Lenguaje:** Python 3.14.2
* **Librerías Core:** NumPy 
* **Datos de Entrada:** `datos_climaticos.csv` (18 registros con marcas de tiempo, temperatura en Celsius y humedad relativa).

Para ejecutar este proyecto de forma local, asegúrate de contar con la librería NumPy instalada en tu entorno de trabajo: pip install numpy

## 🚀 Instrucciones de Ejecución Clonar el repositorio localmente:
PowerShell git clone [https://github.com/ValeriaPFR/Desafio6_ObtencionDatosNumpy.git](https://github.com/ValeriaPFR/Desafio6_ObtencionDatosNumpy.git)

Asegurar que el archivo de datos fuente datos_climaticos.csv se encuentre en la raíz del directorio de trabajo.  
Ejecutar el script analítico desde la terminal de comandos:
PowerShell python desafio_clima.py
 
