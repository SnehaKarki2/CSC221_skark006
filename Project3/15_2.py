import matplotlib.pyplot as plt

initial_range = range(1, 6)
initial_cubes = [x ** 3 for x in initial_range]

extensive_range = range(1, 5001)
extensive_cubes = [x ** 3 for x in extensive_range]

fig, ax = plt.subplots()

ax.plot(initial_range, initial_cubes, label='Cubes of 1-5', color='deepskyblue', marker='o')
ax.plot(extensive_range, extensive_cubes, label='Cubes of 1-5000', color='coral')

ax.set_xlabel('Natural Numbers')
ax.set_ylabel('Cubes')
ax.set_title('Visualization of Cubic Numbers')
ax.legend()

plt.show()
