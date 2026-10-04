# Práctica Individual N° 2

**Estudiante:** Edwin Aguilar
**Caso:** Análisis del tiempo de atención de clientes en una farmacia de barrio.

## Estructura
- datos/datos.csv
- scripts/analisis.py
- reporte/informe.txt

## Instalación
pip install pandas numpy

## Ejecución
cd scripts
python analisis.py

## Resultados
Media entre llegadas: 5.9533 min
Media de servicio: 5.1077 min
Outliers entre llegadas: 0
Outliers de servicio: 0

## Criterio
Z = (x - media) / desviación estándar
Outlier fuerte: |Z| > 3

Los datos se generaron con semilla 2026 siguiendo el script recomendado en el reto.
