import pandas as pd
import numpy as np

df = pd.read_csv("../datos/datos.csv")

for columna in ["tiempo_entre_llegadas_min", "tiempo_servicio_min"]:
    x = df[columna]
    media = x.mean()
    mediana = x.median()
    desviacion = x.std(ddof=1)
    z = (x - media) / desviacion
    outliers = df.loc[np.abs(z) > 3, ["id_cliente", columna]]

    print("\nVariable:", columna)
    print(f"Media: {media:.4f} min")
    print(f"Mediana: {mediana:.4f} min")
    print(f"Desviacion estandar: {desviacion:.4f} min")
    print(f"Minimo: {x.min():.2f} min")
    print(f"Maximo: {x.max():.2f} min")
    print(f"Outliers |Z| > 3: {len(outliers)}")
    if len(outliers):
        print(outliers.to_string(index=False))
