""" with open("csv_data_reading/weather_data.csv") as data_file:

    data = data_file.readlines()

    print(data) """


""" import csv

with open("csv_data_reading/weather_data.csv") as data_file:
    data = csv.reader(data_file)

    tempertures = []

    for row in data:
        if row[1] != "temp": 
            tempertures.append(int(row[1]))

    print(tempertures)
 """


import pandas


data = pandas.read_csv("csv_data_reading/weather_data.csv")

print(data["temp"])