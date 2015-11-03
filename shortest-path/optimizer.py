import random
import math

__author__ = 'estensen'


class Optimizer:
    """Optimize a list by sorting it."""
    def __init__(self, max_iterations, penalty_function):
        """Generate a random permutation of elements from 0 to 9.

        Parameters
        ----------
        max_iterations : Number of iterations the class will try to optimize for.
        penalty : Function that tells how good the list is sorted.
        """
        self.x = random.sample(range(0, 10), 10)
        self.max_iterations = max_iterations
        self.penalty_function = penalty_function
        self.penalty_matrix = self.calculate_penalty_matrix()
        self.temperature = 100

    def calculate_penalty_matrix(self):
        """Pregenerate penalty matrix for all elements"""
        m = [[0 for x in range(10)] for x in range(10)]
        for i in range(10):
            for j in range(10):
                m[i][j] = self.penalty_function(i, j)
        return m

    def total_penalty(self, x):
        """Tells how good or bad a list is sorted."""
        # return sum(map(lambda a, b: abs(a - b), x[1:], x[:-1]))
        # return sum(map(self.penalty, x[1:], x[:-1]))
        penalty = 0
        for i in range(9):
            penalty += self.penalty_matrix[x[i]][x[i+1]]
        penalty += self.penalty_matrix[x[9]][x[0]]
        return penalty

    def reduce_penalty(self, use_greedy):
        """Try to reduce penalty by applying one of two sorting algorithms."""
        random_pos = random.sample(range(0, 10), 2)
        pos_1 = random_pos[0]
        pos_2 = random_pos[1]
        y = list(self.x)
        y[pos_1], y[pos_2] = y[pos_2], y[pos_1]
        if use_greedy:
            self.greedy_sort(y)
        else:
            self.simulated_annealing(y)

    def greedy_sort(self, y):
        """Random sort.

        Try at random to switch two elements.
        If the penalty becomes lower this is a good move.
        Replace previous list.
        """
        if self.total_penalty(self.x) > self.total_penalty(y):
            self.x = y

    def simulated_annealing(self, y):
        """Alternative "greedy algorithm" that wont get stuck at a local minima."""
        if self.total_penalty(self.x) + (self.temperature * math.log(1/random.random())) >= self.total_penalty(y):
            # print(self.x)
            # print(self.total_penalty(self.x))
            self.x = y
            self.temperature *= 0.995

    def solve(self, use_greedy):
        """Apply sorting algorithms many times.

        Parameters
        ----------
        use_greedy : If yes use greedy algorithm, if false use simulated_annealing.
        """
        for _ in range(self.max_iterations):
            self.reduce_penalty(use_greedy)


# Testing
def f(a, b): return abs(math.sin((a-b)/10))
o = Optimizer(10000, f)
# for line in o.penalty_matrix:
#     print(line)
o.solve(False)
print(o.total_penalty(o.x))
print(o.x)
