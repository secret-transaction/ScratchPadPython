__author__ = 'Lyndon'

"""
Read on classes: http://www.afterhoursprogramming.com/tutorial/Python/Classes/
Read on Programming Practice: http://legacy.python.org/dev/peps/pep-0008/#introduction
"""


class Calculator(object):

    def __init__(self):
        self.current = 0

    def add(self, amount):
        self.current += amount

    def get_current(self):
        return self.current
