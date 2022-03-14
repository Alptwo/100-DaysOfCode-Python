import pandas

squirrel_data = pandas.read_csv("Central_Park_Squirrel_Data_Project_csv/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrel_color_data = squirrel_data["Primary Fur Color"]

num_of_black_fur = 0
num_of_cinnomon_fur = 0
num_of_gray_fur = 0

#could also used num_of_gray_fur = len(squirrel_data[squirrel_color_data == "Gray"]) etc.

for color_data in squirrel_color_data:
    if(color_data == "Black"):
        num_of_black_fur +=1
    elif(color_data == "Gray"):
        num_of_gray_fur +=1
    elif(color_data == "Cinnamon"):
        num_of_cinnomon_fur +=1

fur_data_dict = {
    "Primary Fur Color": ["Black", "Gray", "Cinnamon"],
    "Numbers": [num_of_black_fur, num_of_gray_fur, num_of_cinnomon_fur]
}

fur_data_table = pandas.DataFrame(fur_data_dict)

fur_data_table.to_csv("Fur_data.csv")