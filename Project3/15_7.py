from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

dice = [Die(), Die(), Die()]
rolls = [sum(die.roll() for die in dice) for _ in range(1000)]

max_roll = sum(die.num_sides for die in dice)
frequencies = [rolls.count(value) for value in range(3, max_roll + 1)]

x_values = list(range(3, max_roll + 1))
data = [Bar(x=x_values, y=frequencies)]
layout = Layout(title='Results of Rolling Three D6 Dice 1000 Times',
                xaxis={'title': 'Result'},
                yaxis={'title': 'Frequency of Result'})
fig = {'data': data, 'layout': layout}
offline.plot(fig, filename='three_d6_visual.html')
