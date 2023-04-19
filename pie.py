import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

# read the data from the CSV file
data_in = pd.read_csv('HomeDHM.csv')

# prompt the user to enter a day and the labels to include in the pie chart
day = int(input("Enter a day (between 1 and 350): "))

labels = input("Enter labels to include in the pie chart, separated by commas: ").split(",")

data = data_in[data_in['day'] == day] 

data = data.sum()

#print(data)

# retrieve the data for the given day
day_data = data

# retrieve the values for the selected labels
values = [day_data[label] for label in labels]

# create the pie chart
data = go.Pie(labels=labels, values=values)

# specify the layout of the pie chart
layout = go.Layout(title=f'Pie Chart for Day {day}')

# create the figure with the pie chart data and layout
fig = go.Figure(data=[data], layout=layout)

# plot the figure in an interactive mode
pyo.plot(fig, filename='interactive_pie_chart.html', auto_open=True)
