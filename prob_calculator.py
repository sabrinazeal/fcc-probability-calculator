import random


class Hat:
    """A hat containing colored balls that can be drawn randomly."""

    def __init__(self, **balls):
        """Initializes the hat and its contents."""
        self.contents = []
        for color, amount in balls.items():
            for number in range(0, amount):
                self.contents.append(color)
        self.contents_backup = self.contents[:]

    def draw(self, draw_amount):
        """Draws random balls from the hat."""
        drawn_list = []
        if len(self.contents) < draw_amount:
            return self.contents
        for draw_number in range(0, draw_amount):
            drawn_ball = random.choice(self.contents)
            drawn_list.append(drawn_ball)
            self.contents.remove(drawn_ball)

        return drawn_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """Calculates approximate probability of the given draw occurring."""

    match_count = 0
    for experiment_number in range(0, num_experiments):
        hat.contents = hat.contents_backup[:]
        drawn = hat.draw(num_balls_drawn)
        match = True
        for color, amount in expected_balls.items():
            if drawn.count(color) < amount:
                match = False
        if match:
            match_count += 1

    return match_count / num_experiments
