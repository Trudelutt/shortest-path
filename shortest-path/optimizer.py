import random

__author__ = 'estensen'


class Optimizer:
    """Optimize a list by sorting it."""
    def __init__(self, max_iterations, compute_contribution):
        """Generate a random permutation of elements from 0 to 9 and call this x."""
        self.x = random.sample(range(0, 10), 10)
        self.max_iterations = max_iterations
        self.compute_contribution = compute_contribution

    def penalty(self, x):
        """Tells how good or bad a list is sorted.

        Examples
        --------
        penalty([0, 1, 2]) = 2
        penalty([1, 0, 2]) = 3

        Returns
        -------
        Sum of the difference between elements next to eachother.
        """
        return sum(map(lambda a, b: abs(a - b), x[1:], x[:-1]))

        # return sum(map(lambda a, b: abs(a - b), x[1:], x[:-1])) / len(x)

    def reduce_penalty(self):
        """Random sort.

        Try at random to switch two elements.
        If the penalty becomes lower this is a good move.
        Replace previous list.
        """
        random_pos = random.sample(range(0, 10), 2)  # Generate two unique numbers in the intervall [0, 10]
        pos_1 = random_pos[0]
        pos_2 = random_pos[1]
        y = list(self.x)
        y[pos_1], y[pos_2] = y[pos_2], y[pos_1]
        if self.penalty(self.x) > self.penalty(y):
            self.x = y

    def solve(self, use_greedy):
        """Apply random sort many times."""
        if use_greedy:
            for _ in range(self.max_iterations):
                print(self.x)
                print(self.penalty(self.x))
                self.reduce_penalty()
        else:
            ...

# Test random sort
o = Optimizer(1000, 0)
o.solve(True)