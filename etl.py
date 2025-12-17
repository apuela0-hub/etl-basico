import pandas as pd

pd.read_csv("datos.txt").to_excel("resultado.xlsx", index=False)

print("listo")
