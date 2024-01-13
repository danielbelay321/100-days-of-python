import csv
import pandas

# with open("002 weather-data.csv") as file:
#     data = csv.reader(file)
#     temprature = []
#
#     for row in data:
#         if row[1] != 'temp':
#             temprature.append(int(row[1]))
#
# print(temprature)
data = pandas.read_csv("002 weather-data.csv")
print(data['temp'])