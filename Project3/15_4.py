# Same as ModifiedRandomWalk.py File

import random

class RandomWalk:
    """A class to generate random walks."""
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""
        while len(self.x_values) < self.num_points:
            x_direction = random.choice([1, -1])
            x_distance = random.choice(range(5))
            x_step = x_direction * x_distance

            y_direction = random.choice([1, -1])
            y_distance = random.choice(range(5))
            y_step = y_direction * y_distance

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next values for x and y.
            new_x = self.x_values[-1] + x_step
            new_y = self.y_values[-1] + y_step

            self.x_values.append(new_x)
            self.y_values.append(new_y)