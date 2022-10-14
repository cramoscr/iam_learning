# rolling_dice.py
# ------------
# Updated: cramos 26/jun/2022
# Playing with Plotly
# Based on PythonCrashCourse book (page 324)

from plotly.graph_objs import Bar, Layout
from plotly import offline

from rolling_dice_class import Dice 

# Create a D6
dice = Dice()

# Make some rolls and store results in a list
results = []
for roll_num in range(1000):
	result = dice.roll()
	results.append(result)

#print(f"Results: {results}")

# Analize the results
frequencies = dict()
for value in range (1, dice.num_sides+1):
	rslt = results.count(value)
	frequencies[value] = rslt

#print(f"frequencies: {frequencies}")

# Visualize the results
x_values = list(frequencies.keys())
y_values = list(frequencies.values())

#print(f'x_values type: {type(x_values)}')

data = [Bar(x=x_values, y=y_values)]

x_axis_config = {'title':'Reslt'}
y_axis_config = {'title':'Frequency of Result'}

my_layout = Layout(title='Results of rolling one 6-sided DICE, 1000 times', 
	xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
