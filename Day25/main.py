# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     counter = 0
#     for row in data:
#         if counter > 0:
#             temperatures.append(int(row[1]))
#         counter += 1
#
#     print(temperatures)


# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
#
# average = sum(temp_list)/ len(temp_list)
# print(temp_list)
# print(average)
#
# max = data["temp"].idxmax()
# #print(max)
# #print(data[data.index == max])
# monday = data[data.day == "Monday"]
# print(monday.condition)
# to_fahrenheit = 1.8000 * (monday.temp) + 32.00
# print(f"C: {monday.temp}")
# print(f"F: {to_fahrenheit}")

#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data2 = pandas.DataFrame(data_dict)
# data2.to_csv("new_data.csv")
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors = data["Primary Fur Color"].to_list()
# print(colors)

color_counts = {
    "colors": ["Gray", "Cinnamon", "Black"],
    "counts": [0, 0, 0]
}
#print(color_counts["Gray"] + 1)

# for color in colors:
#     if color in color_counts["colors"]:
#         index = color_counts["colors"].index(color)
#         color_counts["counts"][index] += 1

#print(color_counts)

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

color_counts["counts"][0] = gray_squirrels_count
color_counts["counts"][1] = red_squirrels_count
color_counts["counts"][2] = black_squirrels_count

data2 = pandas.DataFrame(color_counts)
data2.to_csv("squirrel_count.csv")