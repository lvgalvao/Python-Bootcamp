# how to work with csv
# import csv
# weather = []
# with open("project 25 brasil game using pandas/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
# print(temperature)

# how to work with csv using pandas
import pandas as pd

data = pd.read_csv("project 25 brasil game using pandas/weather_data.csv")
# print(type(data)) it's a dataframe
# print(type(data["temp"])) it's a dataseries

#calculate de avg creating a function
# temp_list = data["temp"].to_list()
# def avg_manual(list):

#     sum_total = 0
#     for n in list:
#         sum_total += n

#     count_total = 0
#     for i in list:
#         count_total += 1

#     avg = sum_total/count_total

#     return avg

# print(avg_manual(temp_list))

#calculate de avg using pandas
# print(data["temp"].mean())

#find the max value using python
# temp_list = data["temp"].to_list()

# def max_number(list):

#     for n in list:
#         max = 0
#         if n > max:
#             max = n
#     return max

# print(max_number(temp_list))

# monday = data[data.day == "Monday"]

# # print(data[data.temp == data.temp.max()])
# monday_temp = int(monday.temp)
# print(monday_temp)

#create a data frame from scratch

data_dict = {
    "students": [ "amy", "james", "angela"],
    "scores": [76, 56, 65]
}

df = pd.DataFrame(data_dict)
print(df)

df.to_csv("new_data.csv")



