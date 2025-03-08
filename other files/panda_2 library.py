import pandas as pd
data = pd.read_csv("bmi.csv", sep = "\t", index_col = 0)

print(data)