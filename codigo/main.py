import pandas as pd

filename="calles_de_medellin_con_acoso.csv"

data = pd.read_csv(filename, sep=";")

print(data.shape)
print(data.head(10))