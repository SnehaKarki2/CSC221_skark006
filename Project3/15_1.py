import matplotlib.pyplot as plt

plt.style.use('dark_background')

small_range = range(1, 6)
small_cubes = [x ** 3 for x in small_range]

large_range = range(1, 5001)
large_cubes = [x ** 3 for x in large_range]

fig, ax = plt.subplots()

ax.plot(small_range, small_cubes, label='Cubics of 1-5', marker='o', linestyle='--', color='cyan')

ax.plot(large_range, large_cubes, label='Cubics of 1-5000', color='magenta')

ax.set_xlabel('Natural Numbers')
ax.set_ylabel('Cubic Values')

ax.set_title('Comparison of Cubic Numbers')

ax.legend()

plt.show()
