# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures)

# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print("\n")
# print(data["temp"])
# print(f"{type(data)} -> Table cell is referred as dataframe")
# print(f"{type(data['temp'])} -> Table column is referred as Series")

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].tolist()
# print(temp_list)
#
# print("Average = {}".format(sum(temp_list) / len(temp_list)))
# print("Mean = {}".format(data["temp"].mean()))
# print("Maximum = {}".format(data["temp"].max()))

# Get Data in Columns
# print(data["condition"])
# print(data.condition)

# Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# student_data = pandas.DataFrame(data_dict)
# print(student_data)
# student_data.to_csv("student_data.csv")
