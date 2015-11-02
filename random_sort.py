import random

__author__ = 'estensen'


class RandomSort:
    def __init__(self):
        """Generate a random permutation of elements from 0 to 9 and call this x."""
        self.x = random.sample(range(0, 10), 10)
        for _ in range(1000):
            print(self.x)
            print(self.sentence(self.x))
            self.reduce_sentence()

    def sentence(self, x):
        """Tells how good or bad a list is sorted.

        Examples
        --------
        sentence([0, 1, 2]) = 2
        sentence([1, 0, 2]) = 3

        Returns
        -------
        Sum of the difference between elements next to eachother.

        """
        return sum(map(lambda a, b: abs(a - b), x[1:], x[:-1]))

    def reduce_sentence(self):
        """Random sort.

        Try at random to switch two elements.
        If the sentence becomes lower this is a good move.
        Replace previous list.
        """
        random_pos = random.sample(range(0, 10), 2)
        pos_1 = random_pos[0]
        pos_2 = random_pos[1]
        y = list(self.x)
        y[pos_1], y[pos_2] = y[pos_2], y[pos_1]
        if self.sentence(self.x) > self.sentence(y):
            self.x = y

s = RandomSort()
