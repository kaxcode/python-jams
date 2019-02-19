import random
import string


class Robot(object):
    def __init__(self, name=None):
        if name is None:
            name = self.generate_name()

        self.name = self.generate_name()

    def reset(self):
        self.name = self.generate_name()

    def generate_name(self):
        letters = ''.join(random.sample(string.ascii_uppercase, 2))
        numbers = ''.join(random.sample(string.digits, 3))
        return letters + numbers
