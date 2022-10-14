# csv_files.py
# ---------
# Updated: cramos 28/set/2022
#
# Example of using CSV library for reading CSV files
# Notes:
#   a. CSV library is included as built-in on Python
#   b. 

import csv

with open("csv_weather_data.csv") as my_file:
	my_data = csv.reader(my_file)
	temperatures = []
	for row in my_data:
		#print(row)
		temperatures.append(int(row[1]))

	print(temperatures)

