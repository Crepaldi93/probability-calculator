import copy
import random
# Consider using the modules imported above.

class Hat:

    # A hat will always be created with at least one ball. The arguments passed into the hat object upon creation should be converted to a `contents` instance variable. `contents` should be a list of strings containing one item for each ball in the hat. Each item in the list should be a color name representing a single ball of that color. For example, if your hat is `{"red": 2, "blue": 1}`, `contents` should be `["red", "red", "blue"]`.

    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            self.contents += v * [k]

    # The `Hat` class should have a `draw` method that accepts an argument indicating the number of balls to draw from the hat. This method should remove balls at random from `contents` and return those balls as a list of strings. The balls should not go back into the hat during the draw, similar to an urn experiment without replacement. If the number of balls to draw exceeds the available quantity, return all the balls.

    def draw(self, number):
        balls = []

        if number >= len(self.contents):
            balls = self.contents
        else:
            for n in range(number):
                balls += [self.contents.pop(random.randrange(len(self.contents)))]

        return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    matches = 0

    for n in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = dict()
        for ball in hat_copy.draw(num_balls_drawn):
            drawn_balls[ball] = drawn_balls.get(ball, 0) + 1


        for k, v in expected_balls.items():
            if k not in drawn_balls.keys() or expected_balls[k] > drawn_balls[k]:
                matches -= 1
                break

        matches += 1

    probability = matches / num_experiments

    return probability
