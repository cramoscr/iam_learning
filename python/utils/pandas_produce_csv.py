# pandas_produce_csv.py
# ------------------
# Updated: cramos 28/set/2022
#
# Example of using Pandas library for producing an external CSV file
#
# Notes:
#   a. Pandas must be installed (commonly with pip install pandas)
#   b. It's highly recommended to include column names in the first
#      record of the CSV file
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

# Section 1. Produce CSV file

my_data_dict = {
	"students": ["John", "Maria", "Ines"],
	"scores": [76, 89, 99]
}

my_data = pandas.DataFrame(my_data_dict)
my_data.to_csv("pandas_produce_csv.csv")

print(f'New "pandas_produce_csv.csv" file was generated....')
