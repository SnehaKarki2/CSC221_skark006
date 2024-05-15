from die import Die
from plotly.graph_objs import Bar, Layout
from plotly.offline import plot

# Create two D8 dice.
die_1 = Die(num_sides=8)
die_2 = Die(num_sides=8)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results using Plotly.
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]
layout = Layout(title='Results of Rolling Two D8 Dice 1000 Times',
                xaxis={'title': 'Result', 'dtick': 1},
                yaxis={'title': 'Frequency of Result'})
fig = {'data': data, 'layout': layout}
plot(fig, filename='dice_rolls.html')
