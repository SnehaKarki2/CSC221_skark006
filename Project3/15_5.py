import random

class RandomWalk:
    """A class to generate random walks."""
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Determine the direction and distance for a step, then calculate the step."""
        direction = random.choice([1, -1])
        distance = random.choice(range(5))
        step = direction * distance
        return step

    def fill_walk(self):
        """Calculate all the points in the walk using the get_step method."""
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next values for x and y.
            new_x = self.x_values[-1] + x_step
            new_y = self.y_values[-1] + y_step

            self.x_values.append(new_x)
            self.y_values.append(new_y)

# Example usage
if __name__ == "__main__":
    rw = RandomWalk(5000)
    rw.fill_walk()