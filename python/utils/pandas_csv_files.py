# pandas_csv_files.py
# ----------------
# Updated: cramos 28/set/2022
#
# Example of using Pandas library for handling CSV files
#
# Notes:
#   a. Pandas must be installed (commonly with pip install pandas)
#   b. It's higly recommended to include column names in the first
#      record of the csv file
#   c. Two main datastructures in Pandas are
#          + DataFrame (multiple column dataset, example CSV file)
#          + Series    (single column dataset)
#   d. Pandas offer plenty of incredibly easy
#         + data formating: (tabular reports, for instance)
#         + data transformation: to_dict, to_list, etc.
#         + statistical/analytical functions
#         + See the documentation for houndred of funtionallity
#               https://pandas.pydata.org/docs/reference/series.html

import pandas

# Section 1. Basis

my_data = pandas.read_csv("pandas_data.csv")
print(f'my_data: \n{my_data} \n')

print(f'temperatures: \n{my_data["temp"]} \n')

print(f'my_data type: \n {type(my_data)} \n')
print(f'temp type: \n{type(my_data["temp"])} \n')

# Section 2. Convertions

my_data_dict = my_data.to_dict()
print(f'my_data_dict: \n{my_data_dict} \n')

my_temp_list = my_data["temp"].to_list()
print(f'my_temp_list: \n{my_temp_list} \n')


# Section 3. Playing with data
# ----------------------------------------

# Getting average using the hard way
my_avg_temp = "{:.2f}".format(sum(my_temp_list) / len(my_temp_list))
print(f'my_avg_temp: {my_avg_temp} \n')

# Getting average using the simple way
my_avg_temp = my_data["temp"].mean()
print(f'my_avg_temp: {my_avg_temp} \n')

my_max_temp = my_data.temp.max()
print(f'my_max_temp: {my_max_temp} \n')


# Section 4. Using the column selector
# ----------------------------------------

# Pandas dinamically converts every column in an attribute
# Note: 
#    be carefull with the column label case style (upper, lower)
print(my_data["condition"])
print(my_data.condition)
print(my_data.temp)
print('\n')

# Section 5. Using the row selector
# ----------------------------------------

print(f'Getting single row: \n {my_data[my_data.day == "Monday"]}')
print(f'Higher temp day: \n {my_data[my_data.temp == my_data.temp.max()]}')

monday = my_data[my_data.day == "Monday"]
print(f'Monday temp: {int(monday.temp)}')


