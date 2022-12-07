import pandas as pd
import re

list_brands = open('./lists/list_models_nvidia.txt','r')
df = pd.read_csv('./tables/KABUM - VGA_NVIDIA 20221206.csv',index_col=0)
df['Produto'] = df['Produto'].str.upper()

brands = list_brands.read().splitlines()

tmp = []

for produto in df['Produto']:
    x = [brand.upper() for brand in brands if brand.upper() in produto]
    tmp.append(x)

df['Marca'] = tmp
df.drop_duplicates(subset=['Marca'])

df.to_csv("./tests/Test01 - loop brands.csv",encoding="utf-8")
print(df)
