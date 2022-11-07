import pandas as pd
import numpy as np

CSV = "project 25 us gaming using pandas/Input/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
df = pd.read_csv(CSV)

# print(df)

# task - save a new csv file with the count group by colors

# print(df["Primary Fur Color"])

# df.head(10)

# # find all the values in that column Primary Fur Color
# print(df["Primary Fur Color"].drop_duplicates())

# 0          NaN
# 2         Gray
# 5     Cinnamon
# 37       Black

# print(df[df["Primary Fur Color"]]="Gray".count())

gray_squirrels = len(df[df["Primary Fur Color"] == "Gray"])
gray_squirrels_2 = len[df["Primary Fur Color"] == "Gray"]

print(gray_squirrels)
print(gray_squirrels_2)

# cinnamon_squirrels = len(df[df["Primary Fur Color"] == "Cinnamon"])
# black_squirrels = len(df[df["Primary Fur Color"] == "Black"])

# data_dict = {
#     "Fur Color": [ "Gray", "Cinnamon", "Black"],
#     "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels]
# }

# df_colors = pd.DataFrame(data_dict)
# df_colors.to_csv("squirrel_count_no_index.csv", index=False)