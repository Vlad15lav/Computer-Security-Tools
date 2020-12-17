class Curve:
    def __init__(self, a, b, n):
        self.a, self.b, self.n = a, b, n

    def __repr__(self):
        return "y² = x³{0}x{1} mod {2}".format(self.__form(self.a), self.__form(self.b), self.n)

    @staticmethod
    def __form(input):
        return "+" + str(input) if input >= 0 else str(input)