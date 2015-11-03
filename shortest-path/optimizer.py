# import modules here

__author__ = 'estensen'


class Optimizer:
    """."""
    def __init__(self, max_iterations, contributions):
        """."""
        self.max_iterations = max_iterations
        self.contributions = contributions
        # self.contributions_matrix = contributions(x[i], x[j]) = abs(math.sin((x[i]-x[j])/10))

    def solve(self):
        """."""
