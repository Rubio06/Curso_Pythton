import pandas as pd
import numpy as np

data = pd.read_csv('train.csv', index_col=0)

print(data)

print(data.describe())
print(data.info())

set_gen = set(data["Gender"].to_list())
set_history = set(data["family_history_with_overweight"].to_list())

print(set_gen)
print(set_history)

# 1. Tratamiendo de valores
data["Gender"] = data["Gender"].apply(lambda x: np.nan if x < 0 else x)
data["family_history_with_overweight"] = data["family_history_with_overweight"].apply(lambda x: np.nan if x < 0 else x)

# 2. Valores faltantes
for column in ["Gender","family_history_with_overweight"]:
    median_value = data[column].median()
    data[column].fillna(median_value, inplace=True)
    data = data.metodo(inplace=False)

# 3. Mapeo de datos
gender_maping = {
    "Male": "Maculino",
    "Female": "Femenino"
}

# Casteo de tipos
data["Gender"].replace(gender_maping, inplace=True)
data["Gender"] = data["Gender"].astype("string")

print(data)




    
    




