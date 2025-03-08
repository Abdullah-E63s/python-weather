import pandas as pd

coulmns = ["mariya", "batman", "spongebob"]
titled_coulmns = {"name" : coulmns,
                  "height": [1.67, 1.9, 0.25],
                  "weight" : [54, 100, 1]}
data  = pd.DataFrame(titled_coulmns)
select_coulmns = data["weight"] [1]# for the weight coulmns
select_rows = data.iloc[1] ["weight"]

bmi = []
# formula of bmi
# wieght / height**2
data["bmi"] = data["weight"]/(data["height"]**2)

#data["bmi"] = bmi
data.to_csv("bmi.csv", sep ="\t")


#print(coulmns)
print(data)
# print(select_rows)
